from django.contrib import admin
from credits.models import Transaction,Payment
# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display=['Total_Amount','Amount_to_be_Paid','Mode_Of_Transfer','Transferred_by','Transferred_to','Time_of_transfer','Transaction_id','Project_id']
class PaymentAdmin(admin.ModelAdmin):
    list_display=['Amount_Remaining','User_id']


admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Payment,PaymentAdmin)
