from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import logging
from .models import Course_table

logger = logging.getLogger('django')

@api_view(['GET'])
def add_course(request):
    dept = request.GET.get('Department', None)
    title = request.GET.get('CourseTitle', None)
    teacher = request.GET.get('Instructor', None)
    location = request.GET.get('location', '')

    logger.debug("************** myhello_api: " + title)

    if dept and title and teacher:
        new_course = Course_table(
            Department=dept,
            CourseTitle=title,
            Instructor=teacher
        )
        new_course.save()
        return Response({"data": title + " 已加入課程清單！"},
        status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"res": "參數不足"}, 
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def list_course(request):
    courses = Course_table.objects.all().values()
    
    return render(request, 'myhello/courselist.html', {'courses': courses})
