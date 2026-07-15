from django.db import models

class ApplicationStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    DOCUMENTS_VERIFIED = "DOCUMENTS_VERIFIED", "Documents Verified"
    VISA_PROCESSING = "VISA_PROCESSING", "Visa Processing"
    APPROVED = "APPROVED", "Approved"
    TRAVELED = "TRAVELED", "Traveled"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Canceled"
    
class PaymentMethod(models.TextChoices):
    CASH = "CASH", "Cash"
    BANK = "BANK", "Bank"