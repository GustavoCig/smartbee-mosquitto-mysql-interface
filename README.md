# Introduction
Small python script meant to interface between a Mosquitto broker and a MySQL Database.

Current scripts works by creating a connection to the MySQL Database and to the Mosquitto Broker while subscribing to topics defined in `config.py`.
After subscribing, the script forwards each message received to `controller.py` where the packet will be treated and all the data extracted will be forwarded to `models.py` where, finally, the data will be added the Database.


# Configuration
Before using the script, a `config.py` file need to be defined to define your system's settings.
This file contains MySQL/Mosquitto configuration and 
a `paths` dictionary that specifies all the MQTT topics used by your application.

* MySQL database configuration:
    ```python
    mysql = {
        'user': 'root',
        'password': 'root',
        'host': 'localhost',
        'database': 'db'
    }
    ```

* Mosquitto connection configuration:
    ```python
    mosquitto = {
        'username': 'user@user',
        'pwd': 'password',
        'hostMQTT': 'localhost',
        'port': 1883,
        'log': True
    }
    ```

* `paths` dictionary:
    ```python
    paths = {
        'topic/subtopic': {
            'table': 'any_table',
            'fields': [
                'id',
                'name',
                'any_field',
            ],
            'fieldValueSeparator': '/',
            'separator': '-',
            'qos': 0
        },
    }
    ```
    The current script manages packets in the following format:
    `id` - `name` - `any_field` **/** `1` - `user` - `any_value`
    Where the fields are separated from the values using whatever symbol is          defined in  `fieldValueSeparator`(`/`) and `separator`(`-`).                `fieldValueSeparator` is used to separate the fields from their respective values, meanwhile `separator` is used to separate each member individually, regardless if it is a field or an actual value.
    
# How to use
With your `config.py` created, all that's left is to execute the script by running the file `main.py` either directly or as a service. Then your interface should be fully operational.
