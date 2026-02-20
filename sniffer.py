from scapy.all import sniff

def process_packet(packet):
    if packet.haslayer("IP"):
        ip_layer = packet["IP"]
        print(f"Source: {ip_layer.src} -> Destination: {ip_layer.dst}")

        if packet.haslayer("TCP"):
            print("Protocol: TCP")
        elif packet.haslayer("UDP"):
            print("Protocol: UDP")
        else:
            print("Protocol: Other")

        print("-" * 50)

print("Starting packet sniffer... Press Ctrl+C to stop.")
sniff(prn=process_packet, count=20)