import unittest
from src.actions import action_and_check

 
class TestActions(unittest.TestCase):
    def test_action_and_check(self):
        self.assertTrue(action_and_check("192.168.1.2 cpu_usage_thereshold==80",{'trigger_name': 'cpu_usage_thereshold==80', 'monitoring_app': '172.26.32.1', 'action': '/home/user/scripts/action1'}),True)
        
