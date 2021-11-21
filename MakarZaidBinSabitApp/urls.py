from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Home,Registration,Record
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('registration',Registration.as_view(),name='registration'),
    path('record',Record.as_view(),name='record'),
    # path('progress',Progress.as_view(),name='progress'),
    # path('progress',Progress.as_view(),name='progress'),
    # path('fee',Fee.as_view(),name="fee")
    # path('', views.home,name='home'),
    # path('registration', views.registration,name="registration"),
    # path('progress', views.progress,name="progress"),
    # path('fee', views.fee_record, name="fee"),
    # path('student_record', views.student_record, name="student_record"),
    # path('account_record', views.account_record, name="account_record"),
    # path('expense', views.expense, name="expense"),
]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)