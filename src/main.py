#!/usr/bin/env  python

import threading
import time

from alert_collector import zabbix,sentry,promoteous
from actions import action_and_check

print("Hello")

## Our Monitoring systems ##
zabbix_1 = zabbix("Zabbix_2","172.26.32.1","123456")
prom_1 = promoteous("prom_1","172.26.32.2","123456")
sentry_1 = sentry("sentry_1","172.26.32.3","123456",)
monitoring_systems_obj = [zabbix_1,prom_1,sentry_1]

### Infinit loop to check new triggers and do actions if needed. ###
while True:
    for obj in monitoring_systems_obj:
        print("*"*100)
        print(obj.name)
        user_triggers = obj.get_list_of_triggers()
        for trigger in obj.get_triggers(): 
            for user_trigger in user_triggers:
                if trigger.split(" ")[1] == user_trigger["trigger_name"]:
                    t = threading.Thread(target=action_and_check, args = (trigger,user_trigger))
                    t.daemon = True
                    t.start()     
        time.sleep(1)                   

### THE END ###