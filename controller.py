#!/usr/bin/env python3
import models


def treatTemperature(msg):
    models.modelTemperature(msg)


def treatWeight(msg):
    models.modelWeight(msg)
