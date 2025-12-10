from django.db import models
import uuid

class UnitType(models.TextChoices):
    ADET = 'ADET', 'Adet'
    KG = 'KG', 'Kilogram'
    GRAM = 'GRAM', 'Gram'
    PAKET = 'PAKET', 'Paket'

class Category(models.TextChoices):
    FIDAN = 'FIDAN', 'Fidan'
    TOHUM = 'TOHUM', 'Tohum'

class RequestStatus(models.TextChoices):
    PENDING = 'PENDING', 'Beklemede'
    APPROVED = 'APPROVED', 'Onaylandı'
    REJECTED = 'REJECTED', 'Reddedildi'
    COMPLETED = 'COMPLETED', 'Teslim Alındı'

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='inventory')
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10, choices=UnitType.choices, default=UnitType.ADET)
    category = models.CharField(max_length=10, choices=Category.choices, default=Category.FIDAN)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.school.name}"

class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requester = models.ForeignKey(School, on_delete=models.CASCADE, related_name='sent_requests')
    owner = models.ForeignKey(School, on_delete=models.CASCADE, related_name='received_requests')
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.FloatField()
    status = models.CharField(max_length=20, choices=RequestStatus.choices, default=RequestStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)