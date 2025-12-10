from scapy.all import sniff, PcapWriter

pcap_writer = None  # FIX: Python uses None, not none

def packet_callback(packet):
    global pcap_writer

    # print to screen
    if packet.haslayer('IP'):
        src = packet['IP'].src
        dst = packet['IP'].dst
        proto = packet['IP'].proto
        print(f"[IP] {src} --> {dst} (proto: {proto})")

    # save to pcap if enabled
    if pcap_writer:
        pcap_writer.write(packet)

def start_sniffer(save=False, filename="capture.pcap"):
    global pcap_writer

    if save:
        print(f"[+] Saving packets to {filename}")
        pcap_writer = PcapWriter(filename, append=True, sync=True)

    print("SNIFFING THE PACKETS 👃")
    sniff(prn=packet_callback, store=False)
