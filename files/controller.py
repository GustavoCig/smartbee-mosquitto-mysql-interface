#!/usr/bin/env python3
import models


def treatPayload(msg, fieldValueSeparator, separator):
    [fields, values] = msg.split(fieldValueSeparator)
    fields = fields.split(separator)
    values = values.split(separator)
    models.DB(fields, values)
