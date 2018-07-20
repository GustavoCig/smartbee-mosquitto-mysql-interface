#!/usr/bin/env python3
mysql = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'db'
}

mosquitto = {
    'username': 'usuario',
    'pwd': '123',
    'port': 1883,
    'log': True
}

paths = {
    'topics/topic': {
        'table': 'topic',
        'fields': [
            'topic_id',
            'value_id',
            'value',
        ],
        'fieldValueSeparator': ',',
        'separator': '/',
        'qos': 0
    },
}
