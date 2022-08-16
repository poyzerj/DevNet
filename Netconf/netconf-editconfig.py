from ncclient import manager

router = {
    "host": "192.168.1.250",
    "port": "830",
    "username": "cisco",
    "password": "cisco"
}

config_template = open(
    '/home/jpoyzer/DevNet/ios_config.xml').read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", interface_desc="Joe was here")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False, allow_agent=False, look_for_keys=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)

