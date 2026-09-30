# Use a lightweight, official Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy our requirements file and install the PySNMP library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our Python script into the container
COPY simulator.py .

# Expose UDP port 161 (The universal standard for SNMP traffic)
EXPOSE 161/udp

# Command to run our simulator
CMD ["python", "simulator.py"]