import jwt
import datetime
from django.conf import settings
def generate_jwt(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.now() + datetime.timedelta(minutes=1),  
        "iat": datetime.datetime.now(),  # Issued at
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


