import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','IFSC.settings')

import django
django.setup()

from Banks.models import Banks

import xlrd

sheet=xlrd.open_workbook("bb.xlsx").sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,sheet.nrows):
    Banks.objects.get_or_create(ifsc=sheet.cell_value(i,0),branch=sheet.cell_value(i,1),address=sheet.cell_value(i,2),city=sheet.cell_value(i,3),district=sheet.cell_value(i,4),state=sheet.cell_value(i,5),bank=sheet.cell_value(i,6))
    if i%1000==0:
        print("done")
print("done")
