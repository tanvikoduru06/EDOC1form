from django.db import models
import datetime
# Create your models here.
class Transaction(models.Model):
    Total_Amount=models.FloatField()
    Amount_to_be_Paid=models.FloatField()
    Mode_Of_Transfer=models.CharField(max_length=50)
    Transferred_by=models.CharField(max_length=60)
    Transferred_to = models.CharField(max_length=60)
    Time_of_transfer=models.DateTimeField(auto_now_add=True)
    Transaction_id=models.IntegerField()
    Project_id=models.IntegerField()

class Payment(Transaction):
    Amount_Remaining=models.FloatField()
    User_id=models.IntegerField()
    totalamount=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name='+', default="")