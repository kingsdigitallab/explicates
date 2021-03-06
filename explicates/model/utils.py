# -*- coding: utf8 -*-
"""Model utilities module."""

import uuid
from datetime import datetime


def make_timestamp():
    """Return timestamp expressed in the UTC xsd:datetime format."""
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


def make_uuid():
    """Return a Unicode UUID."""
    return str(uuid.uuid4())
