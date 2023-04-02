from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self) -> None:
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        #print(self.key)
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values = None):
        self.password_file = path

        if initial_values is not None:
            for key, values in initial_values.items():


pm = PasswordManager()
pm.create_key("mykey.key")