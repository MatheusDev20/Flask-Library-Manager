import bcrypt

class Bcrypt:

    @classmethod
    def password_hash(self, password: str):
        """ Hasheds a password using a random salt generator and bcrypt algorith """
        byte_encoded_password = password.encode('utf-8')

        pass_salt = bcrypt.gensalt()

        encode_pass = bcrypt.hashpw(byte_encoded_password, salt=pass_salt)

        return encode_pass.decode('utf-8')

    
    @classmethod
    def check_password_hash(self, password: str, hashed: str):
        """ Check if a password mathces a hash """
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
