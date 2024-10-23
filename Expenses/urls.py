from django.urls  import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'expenses',CreateExpenses)

urlspatterns=[
    path('',include(router.urls)),
    path('expennses/month/<str:date>',FilterByMonthExpense.as_view()),
    path('')
    
]