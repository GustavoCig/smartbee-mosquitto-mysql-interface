#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import config as cfg


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code {}").format(rc)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("{} -> {}").format(msg.topic, msg.payload)
    cfg.paths[msg.topic](msg.payload)


def on_log(client, userdata, level, buf):
    print("log: {}").format(buf)


def connect(username, pwd, logging, topics=[("sensors/temperature", 0),
            ("test/test", 0)], broker='localhost', port=1883):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    if logging:
        client.on_log = on_log

    client.username_pw_set(username, pwd)
    client.connect(broker, port, 60)

    client.subscribe(topics)
    client.loop_forever()


if __name__ == "__main__":
    connect('teste@teste', '123456', True)
