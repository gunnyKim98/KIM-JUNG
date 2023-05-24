from django.db import models


class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()


class DepositOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='deposit_options')
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()


class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    join_way = models.TextField(null=True)
    mtrt_int = models.TextField(null=True)
    spcl_cnd = models.TextField(null=True)
    join_member = models.TextField(null=True)
    etc_note = models.TextField(null=True)


class SavingOptions(models.Model):
    fin_prdt_cd = models.ForeignKey(SavingProducts, on_delete=models.CASCADE, related_name='saving_options')
    intr_rate_type_nm = models.CharField(max_length=100, blank=True)
    rsrv_type_nm = models.CharField(max_length=100, blank=True)
    intr_rate = models.FloatField(blank=True)
    intr_rate2 = models.FloatField(blank=True)
    save_trm = models.IntegerField(blank=True)