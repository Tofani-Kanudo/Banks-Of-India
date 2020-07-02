from django.shortcuts import render
from Banks.models import Banks
# Create your views here.

def Index(request):
    banks=Banks.objects.distinct()
    return render(request,'Index.html',{'banks':banks})
def Search(request):
    if request.GET.get('IFSC'):
        sc=request.GET['IFSC']
        branch=Banks.objects.get(ifsc=sc)
        return render(request,'Index.html',{'branch':branch,'res':"Branch Details"})
    elif request.GET.get('bank'):
        bank=Banks.objects.filter(bank__icontains=request.GET.get('bank'))
        if bank:
            city=bank.filter(city__icontains=request.GET.get('city'))
            return render(request,'Index.html',{'city':city,'res':"Banks in "+request.GET.get('city')})
    return Index(request)