from django.shortcuts import (
    render,
    HttpResponse,
    redirect,
)
from django.views.generic import (
    View,
    ListView,
    DetailView,
    FormView,
)
from django.urls import reverse_lazy
from deposits.models import Deposit
from deposits import models


class AddDepositView(View):
    def get(self, request):
        return render(
            template_name='form.html',
            request=request
        )

    def post(self, request):
        deposit = Deposit(
            deposit=request.POST['deposit'],
            term=request.POST['term'],
            rate=request.POST['rate'],
            interest='0'
        )

        deposit.save()

        context = {
            'deposit': deposit,
        }

        return redirect(reverse_lazy('index'))


class DepositsListView(ListView):
    template_name = 'index.html'
    model = Deposit


class GetDepositView(DetailView):
    template_name = 'detail.html'
    pk_url_kwarg = "user_id"
    model = models.Deposit.objects.all()
