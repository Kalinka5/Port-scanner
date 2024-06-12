import nmap

nm = nmap.PortScanner()

target = "127.0.0.1"
options = "-sV -sC scan_results"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")
    for protocol in nm[host].all_protocols():
        print(f"Protocol: {protocol}")
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print(f"Port: {port}\tState: {state}")
