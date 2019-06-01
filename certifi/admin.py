from django.contrib import admin

# Register your models here.

from .models import client
from .models import user
from .models import location
from .models import test_standard
from .models import service
from .models import product
from .models import sequence
from .models import performance
from .models import product_factory
from .models import factory_inspection_jj
from .models import certificatez
from .models import expertise
from .models import tempp
from .models import temp2
from .models import certificategenerator_y
from .models import report_no2
from .models import file_generator_number
from .models import product_certificate
from .models import cert_type_code_zz
# from .models import file_number_generator


# Register your models here.
class tempadmin(admin.ModelAdmin):
    list_display = ('x',)
    exclude = ('m',)

class cert_no_generator_admin(admin.ModelAdmin):
    display = ('yy',)
    exclude=('seq',)

class factory_admin(admin.ModelAdmin):
    display = ('a',)
    exclude = ('id_xx',)

class file_admin(admin.ModelAdmin):
    display = ('b',)
    exclude = ('seq2',)

class report_no_admin(admin.ModelAdmin):
    exclude = ('page_numberr',)

class produc_admin(admin.ModelAdmin):
    exclude = ('prod_id',)



# class file_number_generator_admin(admin.ModelAdmin):
#     display = ('z',)
#     exclude=('seq1',)


admin.site.register(client)
admin.site.register(user)
admin.site.register(location)
admin.site.register(test_standard)
admin.site.register(service)
admin.site.register(product, produc_admin)
admin.site.register(sequence)
admin.site.register(performance)
admin.site.register(product_factory)
admin.site.register(factory_inspection_jj, factory_admin)
admin.site.register(certificatez)
admin.site.register(expertise)
admin.site.register(temp2)
admin.site.register(tempp, tempadmin)
admin.site.register(certificategenerator_y,cert_no_generator_admin)
admin.site.register(report_no2,report_no_admin)
admin.site.register(file_generator_number, file_admin)
admin.site.register(cert_type_code_zz)
admin.site.register(product_certificate)
# admin.site.register(file_number_generator,file_number_generator_admin)
