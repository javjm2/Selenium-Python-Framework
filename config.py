import os
from os import environ
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

TENANT_ID = os.environ.get('TENANT_ID')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

KEYVAULT_NAME = os.environ.get('KEYVAULT_NAME')
KEYVAULT_URI = f"https://{KEYVAULT_NAME}.vault.azure.net/"

_credentials = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credentials)
username = _sc.get_secret("username").value
password = _sc.get_secret("password").value
