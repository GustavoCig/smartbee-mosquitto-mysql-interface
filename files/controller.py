#!/usr/bin/env python3
import models


def treatPayload(msg, fieldValueSeparator, separator):
    [fields, values] = msg.payload.split(fieldValueSeparator)
    fields = fields.split(separator)
    values = values.split(separator)
    models.DB('sensors/temperatura', fields, values)
