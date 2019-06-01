from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class donations(models.Model):
    firstname = models.CharField(max_length=42)
    lastname = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    # phone = models.IntegerField()
    phone = models.CharField(max_length=42)
    contribution_type = models.CharField(max_length=255)
    amount  = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)

    # slug = models.SlugField(unique=True, max_length=255)
    # content = models.TextField()
    # created_on = models.DateTimeField(auto_now_add=True)
    # author = models.TextField()


class client(models.Model):
    idd_client = models.IntegerField(default=1)
    client_code = models.CharField(max_length=5, blank = True)
    client_nam = models.CharField(max_length=42, primary_key=True)
    client_type = models.CharField(max_length=42, blank = True)
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            idd_client = client.objects.all().aggregate(largest=models.Max('idd_client'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if idd_client is not None:
                self.idd_client = idd_client + 1

        super(client, self).save(*args, **kwargs)
    def __str__(self):
        return self.client_nam+"("+str(self.idd_client)+")"


class user(models.Model):
    client_id = models.ForeignKey(client, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=42)
    middle_name = models.CharField(max_length=42, blank = True)
    last_name = models.CharField(max_length=42)
    job_title = models.CharField(max_length=42, blank = True)
    email = models.CharField(max_length=42, primary_key=True)
    office_phone = models.CharField(max_length=42,blank=True)
    cell_phone = models.CharField(max_length=42,blank=True)
    password = models.CharField(max_length=42, blank = True)
    prefix = models.CharField(max_length=42, blank = True)
    def __str__(self):
        return self.first_name+" "+self.last_name


class location(models.Model):
    id = models.IntegerField(default=100000, validators=[MaxValueValidator(999999), MinValueValidator(100000)], primary_key=True)
    client_id = models.ForeignKey(client, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=42, blank = True)
    address1 = models.CharField(max_length=42, blank = True)
    address2 = models.CharField(max_length=42, blank = True)
    city = models.CharField(max_length=42, blank = True)
    state = models.CharField(max_length=42, blank = True)
    country = models.CharField(max_length=42, blank = True)
    zip = models.CharField(max_length=42, blank = True)
    country = models.CharField(max_length=42, blank = True)
    phone = models.CharField(max_length=42, blank = True)
    fax =  models.CharField(max_length=42, blank = True)
    def __str__(self):
        return str(self.id)+" ("+self.name+")"


class test_standard(models.Model):
    test_name = models.CharField(max_length=42, primary_key=True)
    test_description = models.CharField(max_length=42, blank = True)
    publish_date = models.CharField(max_length=42, blank=True)
    def __str__(self):
        return self.test_name

class service(models.Model):
    service_name = models.CharField(max_length=42, primary_key=True)
    service_description = models.CharField(max_length=42, blank = True)
    fi_required = models.CharField(max_length=42, blank=True)
    fi_frequency = models.CharField(max_length=42, blank=True)
    test_standard = models.ForeignKey(test_standard, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.service_name


class product(models.Model):
    prod_id = models.IntegerField(default=1)
    model_no = models.CharField(max_length=42, primary_key=True)
    name = models.CharField(max_length=42, blank=True)

    type = models.CharField(max_length=42, blank=True)
    fireclass = models.CharField(max_length=42, blank=True)
    length = models.CharField(max_length=42, blank=True)
    weight = models.CharField(max_length=42, blank=True)
    max_system_voltage = models.CharField(max_length=42, blank=True)
    individual_cell_area = models.CharField(max_length=42, blank=True)
    cell_technology = models.CharField(max_length=42, blank=True)
    cell_manufacturer = models.CharField(max_length=42, blank=True)
    cell_part_no = models.CharField(max_length=42, blank=True)
    cell_manufacturer_location = models.CharField(max_length=42, blank=True)
    total_number_of_cells = models.CharField(max_length=42, blank=True)
    no_of_cells_in_series = models.CharField(max_length=42, blank=True)
    number_of_series_strings = models.CharField(max_length=42, blank=True)

    number_of_bypass_diodes = models.CharField(max_length=42, blank=True)
    bypass_diode_rating = models.CharField(max_length=42, blank=True)
    bypass_diode_max_temp = models.CharField(max_length=42, blank=True)
    series_fuse_rating = models.CharField(max_length=42, blank=True)
    interconnect_material_and_material_contact_number = models.CharField(max_length=42, blank=True)
    interconnect_dimensions = models.CharField(max_length=42, blank=True)
    superstrate_type = models.CharField(max_length=42, blank=True)
    supersrtate_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)
    substrate_type = models.CharField(max_length=42, blank=True)
    subsrtate_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)

    frame_type_or_material = models.CharField(max_length=42, blank=True)
    frame_adhesive = models.CharField(max_length=42, blank=True)
    encapsulant_type = models.CharField(max_length=42, blank=True)
    encapsulant_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)
    junction_box_type = models.CharField(max_length=42, blank=True)
    junction_box_manufacturer_and_part_no = models.CharField(max_length=42, blank=True)
    junction_box_potting_material = models.CharField(max_length=42, blank=True)
    junction_box_adhesive = models.CharField(max_length=42, blank=True)
    junction_box_use_with_contuit = models.CharField(max_length=42, blank=True)
    cable_connector_type = models.CharField(max_length=42, blank=True)
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            prod_id = product.objects.all().aggregate(largest=models.Max('prod_id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if prod_id is not None:
                self.prod_id = prod_id + 1

        super(product, self).save(*args, **kwargs)
    def __str__(self):
        return self.model_no




class sequence(models.Model):
    sequence_id = models.CharField(max_length=42, primary_key=True)
    sequence_name = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.sequence_name




class performance(models.Model):
    performance_id = models.CharField(max_length=42, primary_key=True)
    model_num = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    sequenc_id = models.ForeignKey(sequence, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=42, blank=True)
    open_circuit_voltage = models.CharField(max_length=42, blank=True)
    short_circuit_current = models.CharField(max_length=42, blank=True)
    voltage_at_max_power = models.CharField(max_length=42, blank=True)
    current_at_max_power = models.CharField(max_length=42, blank=True)
    max_power_output = models.CharField(max_length=42, blank=True)
    fill_factor = models.CharField(max_length=42, blank=True)
    def __str__(self):
        return self.model_num


class product_factory(models.Model):
    id_u = models.IntegerField(default=1)
    loc = models.ForeignKey(location, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    contact = models.CharField(max_length=42, blank=True)
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            id = factory_inspection_jj.objects.all().aggregate(largest=models.Max('id'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if id is not None:
                self.id = id + 1

        super(product_factory, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.id_u)+str(self.product)+str(self.loc)


class cert_type_code_zz(models.Model):
    cert_type_code_xx = models.CharField(max_length=42, primary_key=True)
    code_description = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.cert_type_code_xx


class certificategenerator_y(models.Model):
    class Meta:
        unique_together = (('subsidiary_code','year_code','pv_type_code',"seq"),)

    seq = models.IntegerField(default=1)
    cert_type_code =  models.ForeignKey(cert_type_code_zz, on_delete=models.SET_NULL, null=True)
    subsidiary_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
    year_code = models.IntegerField(default=100, validators=[MaxValueValidator(999), MinValueValidator(100)])
    pv_type_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            seq1 = certificategenerator_y.objects.filter(pv_type_code=self.pv_type_code)
            seq = seq1.aggregate(largest=models.Max('seq'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if seq is not None:
                self.seq = seq + 1

        super(certificategenerator_y, self).save(*args, **kwargs)

    def __str__(self):
        if self.seq < 9:
            return str(self.cert_type_code)+" "+str(self.subsidiary_code)+str(self.year_code)+str(self.pv_type_code)+"000"+str(self.seq)
        elif self.seq >9 and self.seq<99:
            return str(self.cert_type_code) + " " + str(self.subsidiary_code) + str(self.year_code) + str(self.pv_type_code) + "00" + str(self.seq)
        elif self.seq >99 and self.seq<999:
            return str(self.cert_type_code) + " " + str(self.subsidiary_code) + str(self.year_code) + str(self.pv_type_code) + "0" + str(self.seq)
        else:
            return str(self.cert_type_code) + " " + str(self.subsidiary_code) + str(self.year_code) + str(self.pv_type_code) +str(self.seq)






class file_generator_number(models.Model):
    class Meta:
        unique_together = (('reggion_code', 'yearr_codde','typpe_numbb','pv_type_code',"seq2"),)

    seq2 = models.IntegerField(default=1000)
    reggion_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
    yearr_codde = models.IntegerField(default=10, validators=[MaxValueValidator(99), MinValueValidator(10)])
    pv_type_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
    typpe_numbb = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            seq2 = file_generator_number.objects.all().aggregate(largest=models.Max('seq2'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if seq2 is not None:
                self.seq2 = seq2 + 1

        super(file_generator_number, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.reggion_code)+str(self.yearr_codde)+str(self.typpe_numbb)+str(self.pv_type_code)+str(self.seq2)










class certificatez(models.Model):
    sequence_cer = models.IntegerField(default=1)
    certificate_id = models.AutoField(primary_key=True)
    cert_no = models.ForeignKey(certificategenerator_y, on_delete=models.SET_NULL, null=True)
    client_id = models.ForeignKey(client, on_delete=models.SET_NULL, null=True)
    contact_name = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
    test_std = models.ForeignKey(test_standard, on_delete=models.SET_NULL, null=True)
    issue_date = models.DateField()
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            sequence_cer = certificatez.objects.all().aggregate(largest=models.Max('sequence_cer'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if sequence_cer is not None:
                self.sequence_cer = sequence_cer + 1

        super(certificatez, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.cert_no)

class expertise(models.Model):
    id = models.CharField(max_length=42, primary_key=True)
    test_sttd = models.ForeignKey(test_standard, on_delete=models.SET_NULL, null=True)
    certification = models.CharField(max_length=42, blank=True)
    def __str__(self):
        return self.test_sttd


class factory_inspection_jj(models.Model):
    class Meta:
        unique_together = (('type_of_inspection','pvv_type', 'locatio_id'),)
    id_xx = models.IntegerField(default=1)
    locatio_id = models.CharField(max_length=42)
    type_of_inspection = models.CharField(max_length=2, blank=True)
    pvv_type = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)], blank=True)
    date = models.CharField(max_length=42, blank=True)
    inspector = models.CharField(max_length=42, blank=True)
    inspection_sequence = models.CharField(max_length=42, blank=True)
    cert_no_ab = models.ForeignKey(certificatez, on_delete=models.SET_NULL, null=True)
    findings = models.CharField(max_length=42, blank=True)
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            id_xx = factory_inspection_jj.objects.all().aggregate(largest=models.Max('id_xx'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if id_xx is not None:
                self.id_xx = id_xx + 1

        super(file_generator_number, self).save(*args, **kwargs)
    def __str__(self):
        return self.type_of_inspection+" "+str(self.pvv_type)+str(self.locatio_id)


class tempp(models.Model):
    class Meta:
        unique_together = (('x', 'y', 'z','m'),)
    x = models.CharField(max_length=42)
    y = models.CharField(max_length=42)
    z = models.CharField(max_length=42)
    m = models.IntegerField(default=170)

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            m = tempp.objects.all().aggregate(largest=models.Max('m'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if m is not None:
                self.m = m + 1

        super(tempp, self).save(*args, **kwargs)
    def __str__(self):
        return self.x+self.y+self.z+str(self.m)


class temp2(models.Model):
    idd = models.CharField(max_length=42, primary_key=True)
    gg = models.ForeignKey(tempp, on_delete=models.SET_NULL, null=True)

class report_no2(models.Model):
    class Meta:
        unique_together = (('report_nummber','page_numberr'),)
    report_nummber = models.CharField(max_length=42, blank=True)
    page_numberr = models.IntegerField(default=1)
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            s = report_no2.objects.filter(report_nummber=self.report_nummber)
            seq = s.aggregate(largest=models.Max('page_numberr'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if seq is not None:
                self.page_numberr = seq + 1
            else:
                self.page_numberr = 1


        super(report_no2, self).save(*args, **kwargs)
    def __str__(self):
        return self.report_nummber+" "+str(self.page_numberr)


class product_certificate(models.Model):
    class Meta:
        unique_together = (('certific_no','prod','location_idd','page_numb'),)
    id_pro = models.IntegerField(default=1)
    certific_no = models.ForeignKey(certificatez, on_delete=models.SET_NULL, null=True)
    prod = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    location_idd = models.ForeignKey(location, on_delete=models.SET_NULL, null=True)
    page_numb = models.IntegerField(default=1, validators=[MaxValueValidator(9999), MinValueValidator(1)])
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            id_pro = product_certificate.objects.all().aggregate(largest=models.Max('id_pro'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if id_pro is not None:
                self.id_pro = id_pro + 1

        super(product_certificate, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.certific_no)+" "+str(self.prod)+" "+str(self.location_idd)



# class file_number_generator(models.Model):
#     class Meta:
#         unique_together = (('type_num', 'seq1'),)
#
#     seq1 = models.IntegerField(default=1000)
#     region_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
#     yea_code = models.IntegerField(default=10, validators=[MaxValueValidator(99), MinValueValidator(10)])
#     type_num = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
#     pv_code = models.IntegerField(default=1, validators=[MaxValueValidator(9), MinValueValidator(1)])
#     def save(self, *args, **kwargs):
#         # This means that the model isn't saved to the database yet
#         if self._state.adding:
#             # Get the maximum display_id value from the database
#             seq1 = certificategenerator.objects.all().aggregate(largest=models.Max('seq'))['largest']
#
#             # aggregate can return None! Check it first.
#             # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
#             if seq1 is not None:
#                 self.seq1 = seq1 + 1
#
#         super(file_number_generator, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.type_num)+ " "+str(self.seq1)







