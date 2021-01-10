from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Multiple, OX, Test
from .serializers import QuizSerializer
import random

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response('hello world!')

@api_view(['GET'])
def randomMul(request, id):
    totalMuls = Multiple.objects.all()
    randomMuls = random.sample(list(totalMuls), id)
    serializer = QuizSerializer(randomMuls, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomOX(request, id):
    totalOXs = OX.objects.all()
    randomOXs = random.sample(list(totalOXs), id)
    serializer = QuizSerializer(randomOXs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def randomTest(request, id):
    totalTests = Test.objects.all()
    randomTests = random.sample(list(totalTests), id)
    serializer = QuizSerializer(randomTests, many=True)
    return Response(serializer.data)