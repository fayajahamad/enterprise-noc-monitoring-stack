# Enterprise NOC Monitoring & Observability Stack

## Project Overview
A containerized network operations center (NOC) monitoring stack designed to provide real-time observability into network telemetry and hardware health. This project simulates live network routing traffic and captures physical host metrics, visualizing the entire infrastructure lifecycle in a single Grafana dashboard.

## Architecture & Tech Stack
Infrastructure: Docker, Docker Compose
Telemetry & Metrics: Prometheus, PromQL, Node Exporter
Custom Network Agent: Python (SNMP traffic simulation)
Visualization & Alerting: Grafana

## Key Features
Unified Dashboard: Blends time-series network flow waves with precise hardware capacity gauges (CPU, RAM, Disk).
Custom SNMP Telemetry: Python-based agent generating real-time incoming/outgoing traffic and uptime metrics.
Automated Incident Detection: Live alerting pipeline that continuously evaluates network heartbeats and automatically flags simulated router outages.

## How to Run
1. Clone the repository: `git clone https://github.com/fayajahamad/enterprise-noc-monitoring-stack.git`
2. Navigate to the directory and start the stack: `docker-compose up -d`
3. Access the Grafana dashboard at `http://localhost:3000`

## Detailed Telemetry Metrics
<img width="1523" height="538" alt="Screenshot 2026-09-30 102959" src="https://github.com/user-attachments/assets/e1acf83a-9b09-4576-ad0c-c42351591160" />
<img width="1707" height="617" alt="Screenshot 2026-09-30 102911" src="https://github.com/user-attachments/assets/203fc29b-0759-4f73-82c7-56912c2117b3" />
<img width="1522" height="697" alt="Screenshot 2026-09-30 102831" src="https://github.com/user-attachments/assets/eebc7145-2383-4444-8eb1-1b52a378eb38" />
<img width="1380" height="687" alt="Screenshot 2026-09-30 102704" src="https://github.com/user-attachments/assets/3e7ee007-9e5e-4030-95fc-103e93a80f82" />
<img width="1703" height="617" alt="Screenshot 2026-09-30 102616" src="https://github.com/user-attachments/assets/8dbf9e7b-025b-4f92-ab58-f3d368f12844" />
<img width="1582" height="662" alt="Screenshot 2026-09-30 102458" src="https://github.com/user-attachments/assets/ee891b63-b5f5-43a7-8481-141588fd12b3" />
<img width="1588" height="666" alt="Screenshot 2026-09-30 102401" src="https://github.com/user-attachments/assets/81a4ba8f-459f-4491-b30a-193f3c4eb835" />
<img width="1716" height="737" alt="Screenshot 2026-09-30 102329" src="https://github.com/user-attachments/assets/d96ea608-f04c-4a3b-8a8e-7f135ad531eb" />
<img width="1646" height="663" alt="Screenshot 2026-09-30 102245" src="https://github.com/user-attachments/assets/491cdde9-859a-41c7-ba69-ed8604f4bb1b" />
<img width="1817" height="732" alt="Screenshot 2026-09-30 102218" src="https://github.com/user-attachments/assets/376f125d-5e0e-442e-93c4-4cb784614d2b" />
<img width="1817" height="731" alt="Screenshot 2026-09-30 102137" src="https://github.com/user-attachments/assets/c284286d-d09e-4549-8a7b-06ef09fa343d" />
<img width="1597" height="782" alt="Screenshot 2026-09-30 101636" src="https://github.com/user-attachments/assets/161aad8e-b6b6-4195-88ad-c795b4e74098" />
<img width="1643" height="772" alt="Screenshot 2026-09-30 101544" src="https://github.com/user-attachments/assets/19940473-a01f-476a-a4fe-8a8ed44aaac5" />
<img width="1372" height="645" alt="Screenshot 2026-09-30 103127" src="https://github.com/user-attachments/assets/2a237593-82f2-4639-8058-4a6600e74b52" />
<img width="1530" height="730" alt="Screenshot 2026-09-30 103058" src="https://github.com/user-attachments/assets/a61a6ece-4808-447d-a9af-7aa7f7ba2dbf" />
