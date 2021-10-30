"""Kasa Power Driver.

Support for managing Kasa SmartPlug via python-kasa.
https://python-kasa.readthedocs.io/en/latest/
"""

import asyncio
from kasa import SmartPlug
from provisioningserver.drivers import make_ip_extractor, make_setting_field
from provisioningserver.drivers.power import PowerActionError, PowerDriver
    

class KasaPowerDriver(PowerDriver):
#class KasaPowerDriver:
    name = "Kasa"
    description = "Kasa SmartPlug"
    
    queryable = True
    chassis = True
    can_probe = False
    can_set_boot_order = False
    
    settings = [
        make_setting_field("power_address", "IP of Kasa SmartPlug", required=True),
    ]
    ip_extractor = make_ip_extractor("power_address")
        
    def detect_missing_packages(self):
        return []
    
    def power_on(self, system_id, context):
        try:
            smartPlug = SmartPlug(context["power_address"])
            
            if self.power_query(system_id, context) == "off":
                asyncio.run(smartPlug.turn_on())
        except:
            raise PowerActionError("Kasa Power Driver unable to power on SmartPlug")
        
    def power_off(self, system_id, context):
        try:
            smartPlug = SmartPlug(context["power_address"])
            
            if self.power_query(system_id, context) == "on":
                asyncio.run(smartPlug.turn_off())
        except:
            raise PowerActionError("Kasa Power Driver unable to power off SmartPlug")
        
    def power_query(self, system_id, context):
        smartPlug = SmartPlug(context["power_address"])
        asyncio.run(smartPlug.update())
        
        if smartPlug.is_on == True:
            return "on"
        elif smartPlug.is_on == False:
            return "off"
        else:
            raise PowerActionError("Kasa Power Driver retrieved unknown power state")
