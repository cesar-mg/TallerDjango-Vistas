from variables.models import Variable
from ..models import Measurement

def get_measurements():
    measurement = Measurement.objects.all()
    return measurement

def get_measurement(mer_pk):
    measurement = Measurement.objects.get(pk=mer_pk)
    return measurement

def update_measurement(mer_pk, new_mer):
    measurement = get_measurement(mer_pk)
    measurement.variable = new_mer["variable"]
    measurement.value = new_mer["value"]
    measurement.unit = new_mer["unit"]
    measurement.place = new_mer["place"]
    measurement.dateTime = new_mer["dateTime"]
    measurement.save()
    return measurement

def create_measurement(mer):
    measurement = Measurement(variable=mer["variable"],value = mer["value"], unit=mer["unit"],place=mer["place"],dateTime=mer["dateTime"])
    measurement.save()
    return measurement
def delete_measurement(mer_pk):
    measurement = Measurement.objects.get(pk=mer_pk)
    measurement.delete()
    