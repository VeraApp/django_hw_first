# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'Input Error'})

class SensorView(APIView):
    # def get_object(self, id):
    #     queryset = Sensor.objects.get(id=id)
    #     serializer_class = SensorSerializer(queryset)
    #     return Response(serializer_class.data)
    def get(self, request, id):
        try:
            sensors = Sensor.objects.get(id=id)
            serializer = SensorDetailSerializer(sensors)

            print(serializer.data)
            return Response(serializer.data)
        except Sensor.DoesNotExist:
            return Response({"message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)
    def patch(self, request, id):
        try:
            sensor = Sensor.objects.get(id=id)
            data = request.data
            serializer = SensorSerializer(sensor, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Sensor.DoesNotExist:
            return Response({"message": "Запись не найдена"}, status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def create_measurement(request):
    data = request.data
    serializer = MeasurementSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)




