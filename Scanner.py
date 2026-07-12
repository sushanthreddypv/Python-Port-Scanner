import socket
import time
import csv

print("=" * 40)
print("        PYTHON PORT SCANNER")
print("=" * 40)

# Get target IP address
target = input("Enter IP Address or Hostname: ")

# Validate hostname/IP
try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("❌ Invalid IP address or hostname.")
    exit()

# Get port range
try:
    start_port = int(input("Enter Starting Port: "))
    end_port = int(input("Enter Ending Port: "))
except ValueError:
    print("❌ Please enter valid port numbers.")
    exit()

# Validate port range
if start_port < 0 or end_port > 65535:
    print("❌ Port numbers must be between 0 and 65535.")
    exit()

if start_port > end_port:
    print("❌ Starting port cannot be greater than ending port.")
    exit()

print(f"\nScanning {target} ({target_ip})...")
print("-" * 40)

# Set timeout
socket.setdefaulttimeout(1)

# Start timer
start_time = time.time()

open_ports = 0

# Open CSV file
with open("scan_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # CSV Header
    writer.writerow(["Port", "Service", "Status"])

    # Scan ports
    for port in range(start_port, end_port + 1):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            result = s.connect_ex((target_ip, port))

            if result == 0:
                open_ports += 1

                try:
                    service_name = socket.getservbyport(port)
                except OSError:
                    service_name = "Unknown Service"

                writer.writerow([port, service_name, "Open"])

                print(f"[OPEN] Port {port:<5} | Service: {service_name}")

# End timer
end_time = time.time()
total_time = end_time - start_time

print("\n" + "=" * 40)
print("SCAN SUMMARY")
print("=" * 40)
print(f"Target           : {target}")
print(f"Resolved IP      : {target_ip}")
print(f"Port Range       : {start_port} - {end_port}")
print(f"Open Ports Found : {open_ports}")
print(f"Time Taken       : {total_time:.2f} seconds")
print("Results Saved    : scan_results.csv")
print("=" * 40)