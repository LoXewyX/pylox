from cryptography.fernet import Fernet
from data.secrets import pswd_token # static token bc I'm lazy ._.

fernet = Fernet(pswd_token.encode())

def encode(pswd):
    try:
        return fernet.encrypt(pswd.encode()).decode()
    except:
        print("Error on encoding")
def decode(pswd):
    try:
        return fernet.decrypt(pswd.encode()).decode()
    except:
        print("Error on decoding")
