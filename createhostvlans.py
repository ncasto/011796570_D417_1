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
createacctvlan = "create vlan ACCT_Network tag 20"

createuservlan = "create vlan User_Network tag 30" 
createmgmtvlan = "create vlan MGMT_Network tag 10" 

createitvlan = "create vlan IT_Network tag 40"

with ConnectHandler(**userswitch) as net_connect:
    output = net_connect.send_command(createuservlan)
    output += net_connect.save_config()

print(output)

with ConnectHandler(**acctswitch) as net_connect:
    output = net_connect.send_command(createacctvlan)
    output += net_connect.save_config()
print(output)

with ConnectHandler(**MGMTswitch) as net_connect:
    output = net_connect.send_command(createmgmtvlan)
    output += net_connect.save_config()
print(output)

with ConnectHandler(**ITswitch) as net_connect:
    output = net_connect.send_command(createitvlan)
    output += net_connect.save_config()
print(output)
