from scapy.all import sniff, IP
import signal
import sys

PROTO_MAP = {
    1: "ICMP",
    6: "TCP",
    17: "UDP"
}

def process_packet(packet):
    # Check if the packet has an IP layer
    try:
        if packet.haslayer(IP):
            ip_layer = packet.getlayer(IP)
            # Identify the protocol
            proto_num = ip_layer.proto

            proto_name = PROTO_MAP.get(proto_num, f"Other({proto_num})")

            src = ip_layer.src
            dst = ip_layer.dst
            size = len(packet)

            print(f"[{proto_name}] {src} -> {dst} | Size: {size} bytes")

    except Exception as e:
        print(f"[!] Error parsing packet: {e}")

def stop_sniffing(sig, frame):
    print("\n[!] Stopping sniffer... Saving data...")
    sys.exit(0)

signal.signal(signal.SIGINT, stop_sniffing)

print ("--- Starting Sniffer (Ctrl+C to stop) ---")

sniff(filter="ip", prn=process_packet, store=0)

print("\n--- Test Complete ---")