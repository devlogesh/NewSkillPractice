from traceback import print_exc
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.permissions import  AllowAny
from .models import *
from .serializers import *
from .functions import *
from rest_framework.response import Response
from rest_framework import status,generics
from django.contrib.auth import authenticate,login
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator
from practices.decorator import *



def user_params(request):
    val = request.data
    parser_data = {
        'mobile':val.get('mobile_number'),
        'email':val.get('e_mail'),
        'password':val.get('password','Admin@123'),
        
    }

    return parser_data

class Singup(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        val = user_params(request)
        user_data = {'username' : val['mobile'],'email' : val['email'],'password' : val['password']}
        user_serializer = UserCreateSerializer(data=user_data)
        if user_serializer.is_valid():            
            serializer = UserProfileSerializer(data=val)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.create(**user_serializer.validated_data)
                user.set_password(user_data['password'])
                user.save()
                user_profile = Userprofile.objects.get(id=serializer.data['id'])
                user_profile.user_id = user
                user_profile.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        else:
            return Response(user_serializer.errors,status.HTTP_400_BAD_REQUEST)
        

class UserLoginAPIView(APIView):

    def post(self,request,**kwargs):
        user_params = request.data
        username = user_params.get('username')
        password = user_params.get('password')

        if username and password:
            user = authenticate(username=user_params['username'],password=user_params['password'])
            if user:
                login(request,user)
                profile = Userprofile.objects.get(user_id=user.id)

                # token_id = Token.objects.filter(user_id = user.id)
                # if len(token_id)>0:
                #     token_id.delete()
                # token,create = Token.objects.get_or_create(user=user)
                token = generate_jwt(user.id)
                print(token,'tokemn')
                token_obj = AccessToken.objects.create(user_id=user,key=token)
                return Response({'user_id':user.id,'token':token}, status=status.HTTP_200_OK)
            else:
                errors = {'message':'Invalid Credentials..'}
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            errors = {'message':'Username and Password should not be empty..'}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        

@method_decorator(verify_jwt, name='dispatch')

class ListUserProfile(generics.ListAPIView):
    queryset = Userprofile.objects.filter(active=True)
    serializer_class = UserProfileSerializer
    # pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super(ListUserProfile, self).get_queryset()
        return queryset
    

class ListUserProfile2(APIView):
    @method_decorator(verify_jwt)
    def post(self,request):
        queryset = Userprofile.objects.filter(active=True)
        serializer_class = UserProfileSerializer(queryset,many=True)

        return Response({'data':serializer_class.data}, status=status.HTTP_200_OK)