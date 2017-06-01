# -*- coding: utf-8 -*-
"""
This is the only interface that you should ever need to get a **user** logged
in, get.

**his/her** info and credentials, deserialize the credentials
and access **his/her protected resources**.

.. autosummary::
    :nosignatures:

    authomatic.setup
    authomatic.login
    authomatic.provider_id
    authomatic.access
    authomatic.async_access
    authomatic.credentials
    authomatic.request_elements
    authomatic.backend

"""

from . import six
from .core import Authomatic
from .core import setup
from .core import login
from .core import provider_id
from .core import access
from .core import async_access
from .core import credentials
from .core import request_elements
from .core import backend
