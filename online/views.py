

from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from django.contrib.auth.models import User
from .models import Course, Price, Profile

from django.forms.models import model_to_dict

from .serializers import CoursesListSerializer, PriceListSerializer
from rest_framework.decorators import api_view
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


def make_error_dict(code, type, message):
    dico = {
        "errors": {
            "code": code,
            "type": type,
            "message": message
        }
    }
    return Response(dico, status=code)


class ProfileCreate(views.APIView):

    def post(self, request):
        email = self.request.data.get('email')
        password = self.request.data.get('password')
        fullname = self.request.data.get('fullname')
        phone = self.request.data.get('phone')
        address = self.request.data.get('address')
        prior_experience = self.request.data.get('prior_experience')

        params = ['email', 'password', 'fullname',
                  'phone', 'address', 'prior_experience']
        keys = self.request.data.keys()
        for param in params:
            if param not in keys:
                return make_error_dict(400, "ParamsNeeded", f"{param}")

        if not User.objects.filter(email=email).exists():
            if len(password) < 6:
                return make_error_dict(400, 'FormValidator', 'password too short')

            user = User.objects.create_user(username="default", email=email)
            user.set_password(password)
            user.is_active = True
            user.fullname = fullname
            user.phone = phone
            user.address = address

            user.save()

            profile = Profile.objects.create(
                id=user.id, user_id=user.id, prior_experience=prior_experience)
            Token.objects.create(user=user)

            # send_confirmation_email(request, user)
            return JsonResponse(model_to_dict(user))
        else:
            return make_error_dict(400, 'FormValidator', 'email already exists')


@api_view(['GET', 'POST', 'DELETE'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        course_serializer = CoursesListSerializer(courses, many=True)
        return JsonResponse(course_serializer.data, safe=False)

    # elif request.method == 'POST':
    #     song_data = JSONParser().parse(request)
    #     song_serializer = SongListSerializer(data=song_data)
    #     if song_serializer.is_valid():
    #         song_serializer.save()
    #         return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED)
    #     return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     count = Song.objects.all().delete()
    #     return JsonResponse({'message': '{} Songs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     try:
#         song = Song.objects.get(pk=pk)
#     except song.DoesNotExist:
#         return JsonResponse({'message': 'The song does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         song_data = JSONParser().parse(request)
#         song_serializer = SongListSerializer(song, data=song_data)
#         if song_serializer.is_valid():
#             song_serializer.save()
#             return JsonResponse(song_serializer.data)
#         return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         song.delete()
#         return JsonResponse({'message': 'Song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def price_list(request):
    if request.method == 'GET':
        prices = Price.objects.all()
        price_serializer = PriceListSerializer(prices, many=True)
        return JsonResponse(price_serializer.data, safe=False)

    # elif request.method == 'POST':
    #     song_data = JSONParser().parse(request)
    #     song_serializer = SongListSerializer(data=song_data)
    #     if song_serializer.is_valid():
    #         song_serializer.save()
    #         return JsonResponse(song_serializer.data, status=status.HTTP_201_CREATED)
    #     return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     count = Song.objects.all().delete()
    #     return JsonResponse({'message': '{} Songs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     try:
#         song = Song.objects.get(pk=pk)
#     except song.DoesNotExist:
#         return JsonResponse({'message': 'The song does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         song_data = JSONParser().parse(request)
#         song_serializer = SongListSerializer(song, data=song_data)
#         if song_serializer.is_valid():
#             song_serializer.save()
#             return JsonResponse(song_serializer.data)
#         return JsonResponse(song_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         song.delete()
#         return JsonResponse({'message': 'Song was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
