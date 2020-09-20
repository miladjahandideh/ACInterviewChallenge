from abc import ABC , abstractmethod
from configuration import user_defined_triggers

class MonitoringApp(ABC):
    @abstractmethod
    def __init__(self, name, api_url, api_token):
        self.name = name
        self.api_url = api_url
        self.api_token = api_token
        
    @abstractmethod
    def check_connection(self):
        pass
    @abstractmethod     
    def get_list_of_triggers(self):
        pass
    @abstractmethod
    def get_triggers(self):
        pass

class zabbix(MonitoringApp):
    def __init__(self, name, api_url, api_token):
        self.name = name
        self.api_url = api_url
        self.api_token = api_token

    def check_connection(self):
        return True
    
    def get_list_of_triggers(self):
        return user_defined_triggers(self.api_url)

    def get_triggers(self):
        return ["192.168.1.2 cpu_usage_thereshold==80","192.168.1.4 ram_usage_thereshold==95"]

    
class promoteous(MonitoringApp):
    def __init__(self, name, api_url, api_token):
        self.name = name
        self.api_url = api_url
        self.api_token = api_token

    def check_connection(self):
        return True
    
    def get_list_of_triggers(self):
        return user_defined_triggers(self.api_url)

    def get_triggers(self):
        return ["192.168.1.2 cpu_usage_thereshold==80","192.168.1.4 ram_usage_thereshold==95"]

    

class sentry(MonitoringApp):
    def __init__(self, name, api_url, api_token):
        self.name = name
        self.api_url = api_url
        self.api_token = api_token

    def check_connection(self):
        return True
    
    def get_list_of_triggers(self):
        return user_defined_triggers(self.api_url)

    def get_triggers(self):
        return ["192.168.1.2 cpu_usage_thereshold==80","192.168.1.4 ram_usage_thereshold==95"]

## THE END ##