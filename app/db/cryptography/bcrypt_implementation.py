import bcrypt

class Bcrypt:

    @classmethod
    def password_hash(self, password: str):
        """ Hasheds a password using a random salt generator and bcrypt algorith """
        byte_encoded_password = password.encode('utf-8')

        pass_salt = bcrypt.gensalt()

        return bcrypt.hashpw(byte_encoded_password, salt=pass_salt)