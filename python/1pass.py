#!/usr/bin/env python3

"""
THIS SCRIPT DOES NOT CURRENTLY WORK
"""

from onepassword import OnePassword
import json

op = OnePassword()

from op.client import (
    Client,
    new_client_from_environment,
    new_client
)

client_from_env: Client = new_client_from_environment()

vaults = client.get_vaults()
print(vaults)
