from django.db import models

# Create your models here.


class EncryptDecrypt(models.Model):
    SYMMETRIC_ASYMMETRIC = [
        ('symmetric', 'Symmetric Algo'),
        ('asymmetric', 'ASymmetric Algo'),
    ]

    SYMMETRIC_TECH = [
        ('ceaser cipher', 'Ceaser Ciper'),
        ('play fair', 'Play Fair'),
        ('hill cipher', 'Hill Cipher'),
        
    ]

    ASYMMETRIC_TECH = [
        ('des', 'des 8 bit  ')
    ]
    symmetric_asymmetric = models.CharField(max_length = 100, choices = SYMMETRIC_ASYMMETRIC, default = 'symmetric')
    symmetric_tech = models.CharField(max_length = 100, choices = SYMMETRIC_TECH, default = '')
    asymmetric_tech = models.CharField(max_length = 100, choices = ASYMMETRIC_TECH, default = '')
    message = models.CharField(max_length=100, blank=False, null=False)
    key = models.CharField(max_length = 100, blank=False, null=False)

