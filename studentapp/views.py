from django.http.response import JsonResponse
from .models import Student
from .serializers import StudentSerializer


def StudentView(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data,safe=False)