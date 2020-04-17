from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from credits.models import Transaction
from credits.models import Payment
from credits.serializers import TransactionSerializer
from credits.serializers import PaymentSerializer
from django.http import HttpResponse
from credits.forms import NewTransaction

class TransactionCRUD(ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer

def index(request):
    return render(request,'credits/index.html')


def users(request):
    form=NewTransaction()

    if request.method=="POST":
        form=NewTransaction(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'credits/users.html',{'form':form})

class PaymentCRUD(ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

def __str__(self):
    return self.queryset

def amount_remaining_view(request):
    Amount_Remaining=(Total_Amount)-(Amount_to_be_paid)
    return HttpResponse(Amount_Remaining)