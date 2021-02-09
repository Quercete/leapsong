import firebase_admin
from firebase_admin import credentials
from google.cloud import storage

from config import CREDENTIAL_FILE_NAME


storage_client: storage.Client = \
    storage.Client.from_service_account_json(CREDENTIAL_FILE_NAME)
