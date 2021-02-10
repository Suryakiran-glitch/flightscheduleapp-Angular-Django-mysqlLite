from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from .models import Schedule
from .serializers import UserSerializer,ScheduleSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def testing(request):
    return Response('Hello Django')

class User(viewsets.ModelViewSet):
    queryset = User
    serializer_class = UserSerializer

@csrf_exempt
def flight_list(request):
    #get all schedules
    if request.method == 'GET':
        schedules = Schedule.objects.all()
        schedule_serializer = ScheduleSerializer(schedules, many=True)
        return JsonResponse(schedule_serializer.data, safe=False)

    #Delete all Schedules
    if request.method == 'DELETE':
        Schedule.objects.all().delete()
        return Response("Delete all schedules")

    if request.method == 'POST':
        data = JSONParser().parse(request)
        schedule = ScheduleSerializer(data=data)
        if schedule.is_valid():
            schedule.save()
        return JsonResponse(schedule.data , status=status.HTTP_201_CREATED)
    return JsonResponse("Its a bad request" , status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def flight_details(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
    except:
        Schedule.DoesNotExist
        Response("Table does not exist" , status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        schedule_class = ScheduleSerializer(schedule)
        return JsonResponse(schedule_class.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
       data = JSONParser().parse(request)
       scheduled_class = ScheduleSerializer(schedule , data=data)
       if scheduled_class.is_valid():
           schedule.save()
           return JsonResponse(data=data , status=status.HTTP_200_OK)

       return Response("Invalid data format" , status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
      schedule.delete()
      return JsonResponse("Deleted successfully", status=status.HTTP_200_OK)