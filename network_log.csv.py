from scapy.all import sniff, IP
import csv
import os
from datetime import datetime

LOG_FILE = "network_log.csv"

# Initializing the CSV file with headers if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Source", "Destination", "Protocol", "Length"])

def get_protocol_name(proto_num):
    proto_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
    return proto_map.get(proto_num, f"Other({proto_num})")

def process_packet(packet):
    try:
        if packet.haslayer(IP):
            ip_layer = packet.getlayer(IP)

            # Extract data
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            src = ip_layer.src
            dst = ip_layer.dst
            proto = get_protocol_name(ip_layer.proto)
            length = len(packet)

            #Append to CSV
            with open(LOG_FILE, mode='a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, src, dst, proto, length])

                print(f"[*] Logged: {proto} | {src} -> {dst}")
    except Exception as e:
        print(f"[!] Error: {e}")

print(f"--- Sniffer Active & Logging to {LOG_FILE} ---")
sniff(filter="ip", prn=process_packet, store=0)