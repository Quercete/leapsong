from os import environ

DISCORD_TOKEN = environ["LEAPSONG_TOKEN"]
CREDENTIAL_B64 = environ["LEAPSONG_CRED_B64"]
CREDENTIAL_FILE_NAME = "credential.json"

FIREBASE_SETTINGS = {
        'databaseURL': environ["LEAPSONG_DB_URL"],
        'storageBucket': environ["LEAPSONG_STORAGE_BUCKET"],
        'databaseAuthVariableOverride': {
            'uid': environ["LEAPSONG_UID"]
        }
    }
