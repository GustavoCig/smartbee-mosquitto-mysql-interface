#!/usr/bin/env python3
import mysql.connector
import config as cfg


def modelTemperature(msg):
    cnx = mysql.connector.connect(user=cfg.mysql['user'],
                                  password=cfg.mysql['password'],
                                  host=cfg.mysql['host'],
                                  database=cfg.mysql['database'])
    cursor = cnx.cursor()

    add_coleta = '''
    INSERT INTO colmeia_coleta
    (colmeia_id, sensor_id, valor)
    VALUES (%(colmeia_id)s, %(sensor_id)s, %(valor)s)
    '''

    data_coleta = {
        'colmeia_id': 1,
        'sensor_id': 1,
        'valor': msg,
    }
    cursor.execute(add_coleta, data_coleta)
    cnx.commit()
    cursor.close()
    cnx.close()


def modelWeight(msg):
    cnx = mysql.connector.connect(user=cfg.mysql['user'],
                                  password=cfg.mysql['password'],
                                  host=cfg.mysql['host'],
                                  database=cfg.mysql['database'])
    cursor = cnx.cursor()

    add_coleta = '''
        INSERT INTO colmeia_coleta
        (colmeia_id, sensor_id, valor)
        VALUES (%(colmeia_id)s, %(sensor_id)s, %(valor)s)
    '''

    data_coleta = {
        'colmeia_id': 1,
        'sensor_id': 2,
        'valor': msg,
    }
    cursor.execute(add_coleta, data_coleta)
    cnx.commit()
    cursor.close()
    cnx.close()
