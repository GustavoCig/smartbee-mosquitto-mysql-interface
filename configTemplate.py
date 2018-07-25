#!/usr/bin/env python3
mysql = {
    'user': 'root',
    'password': 'root',
    'hostDB': '127.0.0.1',
    'database': 'db'
}

mosquitto = {
    'username': 'user',
    'pwd': '123',
    'hostMQTT': '127.0.0.1',
    'port': 1883,
    'log': True
}

paths = {
    'sensors/temperature': {
        'table': 'colmeia_coleta',
        'fields': [
            'colmeia_id',
            'sensor_id',
            'value',
        ],
        'fieldValueSeparator': '/',
        'separator': '-',
        'qos': 0
    },
}
