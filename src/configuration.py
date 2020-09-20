

def user_defined_triggers(monitoring_app_id):
    ### SO many thing can be done here. For example they can be retrieved from a DB or Config file
    return [
        {"trigger_name":"cpu_usage_thereshold==80","monitoring_app":monitoring_app_id,"action":"/home/user/scripts/action1"},
        {"trigger_name":"ram_usage_thereshold==95","monitoring_app":monitoring_app_id,"action":"/home/user/scripts/action2"},
        ]