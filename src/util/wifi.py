import os

def get_var(text, var):
    start = text.find(f"{var}=")+len(f"{var}=")
    end = text[start::].find("\n")
    if end == -1:
        return text[start::]
    else:
        return text[start:end+start]


def connect():
    with open("/boot/Wiiid/wifi.txt", "r") as f:
        wifi = f.read()

    ssid = get_var(wifi, "ssid")
    password = get_var(wifi, "pass")
    country = get_var(wifi, "country")

    with open("/boot/wpa_supplicant.conf", "w") as f:
        f.write("""ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country="""+country+"""

network={
    ssid=\""""+ssid+"""\"
    psk=\""""+password+"""\"
    key_mgmt=WPA-PSK
}""")
