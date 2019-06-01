from django.shortcuts import render
from .models import product_certificate
from .models import product_factory
from .models import location
from itertools import chain
from .models import certificatez


def get_certificate_no(request):
    cert_no = certificatez.objects.all()
    return render(request, 'safety.html', {'all_cert':cert_no})



# Create your views here.
def get_certificate(request):
    # aaa = str(request.GET.get('x'))
    # aaa = "TU 110010001"
    # cert = certificatez.objects.get(cert_no="TU 110010001")
    # # print(aaa)
    # return render(request,'show_cert.html',{'cert':cert})
    a = request.GET.get('x')
    print(a)
    product_set = []
    certificate_map = {'TU 110010001':1}
    cert = product_certificate.objects.get(id_pro=certificate_map['TU 110010001'])
    cert_all = product_certificate.objects.filter(certific_no=cert.certific_no)
    for i in cert_all:
        j = str(i).split()
        y = j[2]+" "+j[3]
        product_set.append(y)
    temp = list(set(product_set))
    manu_loc = []

    for i in temp:
        manu_plant = product_factory.objects.filter(product=i)
        manu_temp = str(manu_plant)
        x = manu_temp.index('(')+1
        y = manu_temp.index(')')
        manu_loc.append(manu_temp[x:y])
    manu_location = list(set(manu_loc))
    result_list = []
    for i in manu_location:
        result_list += list(chain(location.objects.filter(name=i)))
    # for i in manu_location:
    # result_list = location.objects.filter(name=manu_location[0])
    return render(request, 'show_certificate.html',{'cert': cert, 'products': cert_all, 'manu_location':result_list })