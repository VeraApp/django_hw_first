from django.urls import path
from measurement.views import SensorsView, SensorView, create_measurement


urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<id>/', SensorView.as_view()),
    path('measurements/', create_measurement)
]
