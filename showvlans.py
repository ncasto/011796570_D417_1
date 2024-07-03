from netmiko import ConnectHandler
from getpass import getpass

userswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.8",
    "username": "admin",
    "password": ''
}

acctswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.7",
    "username": "admin",
    "password": ''
}

MGMTswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.6",
    "username": "admin",
    "password": ''
}


ITswitch = { 
    "device_type": "extreme_exos",
    "host": "10.10.1.5",
    "username": "admin",
    "password": ''
}


showcommand = "show vlan"

with ConnectHandler(**userswitch) as net_connect:
    output = net_connect.send_command(showcommand)
print(output)

with ConnectHandler(**acctswitch) as net_connect:
    output = net_connect.send_command(showcommand)
print(output)

with ConnectHandler(**MGMTswitch) as net_connect:
   output = net_connect.send_command(showcommand)
print(output)

with ConnectHandler(**ITswitch) as net_connect:
    output = net_connect.send_command(showcommand)
print(output)
