#Example 1
# def positive_value(x):
#     if x<0:
#         raise ValueError('Negative input')
#     else:
#         return x**x
        
# print(positive_value(8))

#example 2

class InvalidEmailError(Exception):
    def __init__(self, message):
        super().__init__(f'Invalid email address: {message}')
        self.message = message
    
def validate_email(email):
    if '@' not in email or '.' not in email:
        raise InvalidEmailError(email)
        
try:
    mail = input('enter your email:   ')
    validate_email(mail)
    print('The mail is valid:', mail)   
except InvalidEmailError as e:
    print('Error:', e)
