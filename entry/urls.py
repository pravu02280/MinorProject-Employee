from django.urls import path
from . import views

app_name = 'entry'
urlpatterns = [
    path('purchase/',views.PurchaseCreateView.as_view(), name='purchase'),
    path('purchasedetail/<int:pk>', views.PurchaseDetailView.as_view(), name="purchase_detail"),
    # path('productcreate/',views.productCreateView, name ='productcreate')

]
