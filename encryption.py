from cryptography.fernet import Fernet
from app.config import settings

fernet = Fernet(settings.FERNET_KEY)

def encrypt_data(data: str) -> str:
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    return fernet.decrypt(token.encode()).decode() 