from .logic import measurements_logic as lo
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        measurement_dto = lo.get_measurements()
        measurement = serializers.serialize('json', measurement_dto)
        return HttpResponse(measurement, 'application/json')

    if request.method == 'POST':
        measurement_dto = lo.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = lo.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'PUT':
        measurement_dto = lo.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    if request.method == 'DELETE':
        measurement_dto = lo.delete_measurement(pk)