#!/usr/bin/env python3
import files.connection as con
import config as cfg


def makeTopicsTuple(paths):
    topics = []
    keys = paths.keys()
    for key in keys:
        topics.append((key, paths[key]['qos']))
    return topics


username = cfg.mosquitto['username']
password = cfg.mosquitto['pwd']
log = cfg.mosquitto['log']
topics = makeTopicsTuple(cfg.paths)
broker = cfg.mysql['host']
port = cfg.mosquitto['port']
con.connect(username, password, log, topics, broker, port)
