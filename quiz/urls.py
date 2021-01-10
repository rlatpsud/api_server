from django.urls import path, include
from .views import helloAPI, randomOX,randomMul, randomTest

urlpatterns = [
    path('hello/', helloAPI),
    path('Mul/<int:id>/', randomMul),
    path('OX/<int:id>/', randomOX),
    path('Test/<int:id>/', randomTest)
]