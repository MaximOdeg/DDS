from django.urls import path

from . import views

app_name = "web_dds"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("transactions/", views.transaction_list, name="transaction_list"),
    path("transaction/create/", views.transaction_create, name="transaction_create"),
    path("transaction/<int:pk>/edit/", views.transaction_edit, name="transaction_edit"),
    path(
        "transaction/<int:pk>/delete/",
        views.transaction_delete,
        name="transaction_delete",
    ),
]
