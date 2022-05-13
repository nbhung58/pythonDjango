
from django.contrib.auth.models import User
from requests import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer, GetAllCourseSerializer
from course.models import Course

# Create your views here.
class GetAllCourseAPIView(APIView):
    def get(self, request):
        list_course = Course.objects.all()
        mydata = GetAllCourseSerializer(list_course, many=True)
        return Response(data=mydata.data, status= status.HTTP_200_OK)

    def post(self, request):
        mydata = CourseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Sai du lieu roi', status=status.HTTP_400_BAD_REQUEST)
        title = mydata.data['title1']
        content = mydata.data['content1']
        price = mydata.data['price1']
        cs = Course.objects.create(title=title, price=price, content=content)
        return Response("Add successfully", status=status.HTTP_200_OK)