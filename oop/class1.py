class User:
    username: str
    password: str
    email: str
    
    def auth(self, input_password: str):
        ...


ivan = User()
ivan.username = 'ivannnnn9000'
ivan.password = '12345'

anna = User()
anna.username = 'anutka2002'
anna.password = 'qwerty'


