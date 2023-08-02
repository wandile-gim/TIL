import jwt, datetime
def create_access_token(email):
    return jwt.encode({
        'email' : email,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'orig_iat' : datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')

print(create_access_token('admin@naver.com'))