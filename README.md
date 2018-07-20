# Introduction
Small python script meant to interface between a Mosquitto broker and a MySQL Database.

Current scripts works by creating a connection to the MySQL DB and to the Mosquitto broker while subscribing to predefined topics.
After subscribing, the script forwards each message received to it's according method, following a predefined computation, which them, adds the messages payload to the database.


# Configuration
Before using the script, needs to be defined a `config.py` file to define your system's constants.
This file contains MySQL configuration and 
a `paths` dictionary that specifies all the MQTT topics used by your application.

Since the `paths` dictionary relies on methods defined in the `controller.py`, an import is required:
```python
import controller
```

Then, define the configuration of your MySQL database:
```python
mysql = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'db'
}
```

Finally, define your `paths` dictionary:
```python
paths = {
    "topics/temperature": controller.methodThatDealsWithTemperature,
    "topics/weight": controller.methodThatDealsWithWeight
}
```

# How to use
With your `config.py` created, all that's left is to execute the script by running the file `connection.py`. Then your interface should be fully operational.
