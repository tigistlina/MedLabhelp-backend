import csv
import os
from app.models.test import Test
from app.models.panel import Panel
from app.models.organ import Organ

def run():
    file = open('scripts/lab_tests.csv')
    read_file=csv.reader(file)

    Test.objects.all().delete()
    # Panel.objects.all().delete()
    # Organ.objects.all().delete()

    count = 1

    for record in read_file:
        if count == 1:
            pass
        else:
            Panel.id = int(record[0])
            panel_instance = Panel.objects.get(panel_id=Panel.id)
            Test.objects.create(panel_id=panel_instance,name=record[1],description=record[2],info_url=record[3], normal_reference=record[4], unit_of_measure=record[5])
        count += 1