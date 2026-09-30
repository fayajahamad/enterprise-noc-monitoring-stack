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
