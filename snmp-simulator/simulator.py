import asyncio
import random
from pysnmp.entity import engine, config
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.smi import instrum, builder, exval
from pysnmp.proto.api import v2c

# Network data remains global so both the loop and the controller can access it
network_data = {
    'uptime': 0,
    'incoming_traffic': 1000,
    'outgoing_traffic': 1000
}

class CustomMibController(instrum.MibInstrumController):
    def readVars(self, vars, acInfo=(None, None)):
        results = []
        for oid, val in vars:
            oid_str = str(oid)
            if '1.3.6.1.2.1.1.3' in oid_str:
                # CHANGED: exval to v2c
                results.append((oid, v2c.TimeTicks(network_data['uptime'])))
            elif '1.3.6.1.2.1.2.2.1.10' in oid_str:
                # CHANGED: exval to v2c
                results.append((oid, v2c.Counter32(network_data['incoming_traffic'])))
            elif '1.3.6.1.2.1.2.2.1.16' in oid_str:
                # CHANGED: exval to v2c
                results.append((oid, v2c.Counter32(network_data['outgoing_traffic'])))
            else:
                # KEPT: exval (This is an exception value)
                results.append((oid, exval.noSuchObject))
        return results

async def update_traffic_data():
    while True:
        network_data['uptime'] += 100 
        network_data['incoming_traffic'] += random.randint(5000, 25000) 
        network_data['outgoing_traffic'] += random.randint(1000, 8000)
        await asyncio.sleep(1)

# Move all SNMP initialization INSIDE main()
async def main():
    # flush=True forces Docker to show logs immediately
    print("Initializing SNMP Engine...", flush=True) 
    
    snmpEngine = engine.SnmpEngine()
    
    config.addTransport(
        snmpEngine,
        udp.domainName,
        udp.UdpTransport().openServerMode(('0.0.0.0', 161))
    )
    
    config.addV1System(snmpEngine, 'my-area', 'public')
    config.addVacmUser(snmpEngine, 2, 'my-area', 'noAuthNoPriv', (1, 3, 6), (1, 3, 6))
    
    snmpContext = context.SnmpContext(snmpEngine)
    snmpContext.unregisterContextName(v2c.OctetString(''))
    snmpContext.registerContextName(
        v2c.OctetString(''), 
        CustomMibController(builder.MibBuilder())
    )
    
    cmdrsp.GetCommandResponder(snmpEngine, snmpContext)
    
    print("Starting Python SNMP Simulator on port 161...", flush=True)
    
    # Start the background data generator
    asyncio.create_task(update_traffic_data())
    
    # Keep the container running forever
    loop = asyncio.get_running_loop()
    await loop.create_future()

if __name__ == '__main__':
    asyncio.run(main())