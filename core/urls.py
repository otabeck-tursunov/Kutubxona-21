from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('info/', info_view),
    path('talabalar/', talabalar_view),
    path('talabalar/<int:student_id>/', talaba_view),
]
