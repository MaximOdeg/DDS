from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TransactionForm
from .models import Category, Status, Subcategory, Transaction, Type


def home_view(request):
    return render(request, "home.html")


def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, "transaction_list.html", {"transactions": transactions})


def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("web_dds:transaction_list")
    else:
        form = TransactionForm()
    return render(request, "transaction_form.html", {"form": form})


def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("web_dds:transaction_list")
    else:
        form = TransactionForm(instance=transaction)
    return render(request, "transaction_form.html", {"form": form})


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == "POST":
        transaction.delete()
        return redirect("web_dds:transaction_list")
    return render(
        request, "transaction_confirm_delete.html", {"transaction": transaction}
    )


def get_subcategories(request, category_id):
    subcategories = Subcategory.objects.filter(category_id=category_id).values(
        "id", "name"
    )
    return JsonResponse(list(subcategories), safe=False)
