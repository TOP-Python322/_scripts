class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = hash(password)
    
    @property
    def password(self):
        return raise NotImplementedError
    
    @password.setter
    def password(self, new_password: str):
        self.__password = hash(password)
    
    def authenticate(self, inp_username: str, inp_password: str):
        if self.username != inp_username or self.__password != hash(inp_password):
            raise ValueError

