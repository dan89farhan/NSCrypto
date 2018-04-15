from django.db import models

# Create your models here.


class EncryptDecrypt(models.Model):
    SYMMETRIC_ASYMMETRIC = [
        ('symmetric', 'Symmetric Algo'),
        ('asymmetric', 'Asymmetric Algo'),
    ]

    SYMMETRIC_TECH = [
        ('ceaser cipher', 'Ceaser Ciper'),
        ('play fair', 'Play Fair'),
        ('hill cipher', 'Hill Cipher'),
        ('vernam cipher','Vernam Cipher'),
        ('rail fence', 'Rail Fence'),
        ('columnar','Columnar'),
        ('aes', 'AES'),
        ('sdes', 'SDES'),
    ]

    ASYMMETRIC_TECH = [
        ('rsa', 'RSA'),
    ]
    symmetric_asymmetric = models.CharField(max_length = 100, choices = SYMMETRIC_ASYMMETRIC, default = 'symmetric')
    symmetric_tech = models.CharField(max_length = 100, choices = SYMMETRIC_TECH, default = '')
    asymmetric_tech = models.CharField(max_length = 100, choices = ASYMMETRIC_TECH, default = '')
    message = models.CharField(max_length=100, blank=False, null=False)
    key = models.CharField(max_length = 100, blank=False, null=False)

