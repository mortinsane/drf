from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from .serializers import WomenSerializer
from .models import Women


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        # return Response(
        #     {'title': 'Нина Добрев'}
        # )
        # lst = Women.objects.all().values()
        w = Women.objects.all()
        return Response(
            # {'posts': list(lst)}
            {'posts': WomenSerializer(w, many=True).data}
        )
    
    def post(self, request):
        # return Response(
        #     {'title': 'Лусинэ Геворкян'}
        # )

        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )

        return Response(
            # {'post': model_to_dict(post_new)}
            {'post': WomenSerializer(post_new).data}
        )