from django.contrib import admin
from django.urls import path,include
from First.views import my_test
from First.views import entry


urlpatterns=[
	path('', my_test),
	path('Entry',entry)

]