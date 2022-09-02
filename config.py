from os import environ
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

TENANT_ID = "e3e02793-55b2-4bfd-a515-8488a1b0653b"
CLIENT_ID = "b3ca5fd7-40a6-48a8-afe0-c8ab335aed41"
CLIENT_SECRET = "wul8Q~V3jcC2gW_fHMYC~5NJHOUyLSxJ2V1JXcor"

KEYVAULT_NAME = "test-selenium-vault"
KEYVAULT_URI = f"https://test-selenium-vault.vault.azure.net/"

_credentials = ClientSecretCredential(
    tenant_id=TENANT_ID,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credentials)
username = _sc.get_secret("username").value
password = _sc.get_secret("password").value
