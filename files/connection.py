#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import config as cfg
import controller as ctrl


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {} to broker ").format(rc)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("{} -> {}").format(msg.topic, msg.payload)
    ctrl.treatPayload(msg, cfg.paths[msg.topic]['fieldValueSeparator'],
                      cfg.paths[msg.topic]['separator'])


def on_log(client, userdata, level, buf):
    print("log: {}").format(buf)


def connect(username, pwd, logging, topics, broker, port):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    if logging:
        client.on_log = on_log

    client.username_pw_set(username, pwd)
    client.connect(broker, port, 60)
    client.subscribe(topics)
    client.loop_forever()
