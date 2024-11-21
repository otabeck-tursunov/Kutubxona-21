from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('info/', info_view),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:student_id>/', talaba_view),
    path('talabalar/<int:student_id>/update/', talaba_update_view),
    path('talabalar/<int:student_id>/delete/', talaba_del_view),
    path('recordlar/', recordlar_view, name='recordlar'),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitoblar/<int:book_id>/update/', kitob_update_view),

]
