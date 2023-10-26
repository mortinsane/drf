from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Women
import io

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

        

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()



# def encode():
#     model = WomenModel('Нина Добрев', 'Content: Нина Добрев')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)

# def decode():
#     stream = io.BytesIO(b'{"title":"\xd0\x9d\xd0\xb8\xd0\xbd\xd0\xb0 \xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb5\xd0\xb2","content":"Content: \xd0\x9d\xd0\xb8\xd0\xbd\xd0\xb0 \xd0\x94\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb5\xd0\xb2"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)