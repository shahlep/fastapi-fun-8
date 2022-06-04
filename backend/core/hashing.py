from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Hash():
    @staticmethod
    def get_hash_password(plain_password):
        return pwd_context.hash(plain_password)
