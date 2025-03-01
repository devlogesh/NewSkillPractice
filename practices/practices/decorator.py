import logging
from functools import wraps
import jwt
from .settings import SECRET_KEY
from django.http import JsonResponse


def verify_jwt(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse({"error": "Authentication credentials were not provided."}, status=401)
        
        # Extract the token
        token = auth_header.split(" ")[1]
        try:
            decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            print(decoded_payload,"decoded_payload")
            # return decoded_payload
            return view_func(request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired."}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"error": "Invalid token"}, status=401)
        
    return wrapper
