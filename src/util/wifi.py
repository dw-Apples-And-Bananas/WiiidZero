import os

def connect():
    with open("/boot/Wiiid/wifi", "r") as f:
        wifi = f.read()
    lines = wifi.splitlines()
    while "" in lines:
        lines.remove("")
    connections = []
    s,p = 0,1
    for i in range(len(lines)-2):
        connections.append([
            lines[s].replace("ssid=",""),
            lines[p].replace("pass=","")
        ])
        s+=2
        p+=2
    print(connections)


    for connection in connections:
        os.system(f"sudo raspi-config nonint do_wifi_ssid_passphrase {connection[0]} {connection[1]}")

