import base64

import firebase_admin

from config import CREDENTIAL_FILE_NAME, CREDENTIAL_B64, FIREBASE_SETTINGS


def __create_credential_file() -> None:
    with open(CREDENTIAL_FILE_NAME, "wb") as f:
        f.write(base64.b64decode(CREDENTIAL_B64))


def __get_credential() -> firebase_admin.credentials.Certificate:
    credential = firebase_admin.credentials.Certificate(CREDENTIAL_FILE_NAME)

    return credential


def initialize() -> None:
    __create_credential_file()

    CREDENTIAL = __get_credential()

    firebase_admin.initialize_app(CREDENTIAL, FIREBASE_SETTINGS)
