from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """رمزگذاری (Hash) رمز عبور"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """بررسی اعتبار رمز عبور"""
    return pwd_context.verify(plain_password, hashed_password)
