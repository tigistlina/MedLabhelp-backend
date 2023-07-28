import csv
import os
from app.models.test import Test
from app.models.panel import Panel
from app.models.organ import Organ
from app.models.alternatename import AlternateName
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

def run():
    ReadOrgan()
    ReadPanel()
    ReadTest()
    ReadAlternateName()
    
def ReadTest():
    file = open('scripts/test.csv')
    read_file=csv.reader(file)

    Test.objects.all().delete()

    count = 1

    for record in read_file:
        if count == 1:
            pass
        else:
            panel_id = int(record[0])
            try:
                panel_instance = Panel.objects.get(id=panel_id)
                Test.objects.create(panel_id=panel_instance,name=record[1],description=record[2],info_url=record[3], normal_reference=record[4], unit_of_measure=record[5])
            except ObjectDoesNotExist:
                return JsonResponse(f"Panel with id {panel_id} does not exist.",safe=False) 
        count += 1

def ReadPanel():
    file = open('scripts/panel.csv')
    read_file=csv.reader(file)
    Panel.objects.all().delete()

    count = 1

    for record in read_file:
        if count == 1:
            pass
        else:
            organ_id = int(record[1])
            try:
                organ_instance = Organ.objects.get(id=organ_id)
                Panel.objects.create(name=record[0],organ_id=organ_instance)
            except ObjectDoesNotExist:
                return JsonResponse(f"Organ with id {organ_id} does not exist.",safe=False)
        count += 1

def ReadOrgan():
    file = open('scripts/organ.csv')
    read_file=csv.reader(file)
    Organ.objects.all().delete()

    count = 1

    for record in read_file:
        if count == 1:
            pass
        else:
            Organ.objects.create(name=record[0])
        count += 1

def ReadAlternateName():
    file = open('scripts/alternate_name.csv')
    read_file=csv.reader(file)
    AlternateName.objects.all().delete()

    count = 1

    for record in read_file:
        if count == 1:
            pass
        else:
            AlternateName.objects.create(test_id=int(record[0]),name=record[1])
        count += 1
