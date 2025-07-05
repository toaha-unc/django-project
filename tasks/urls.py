
from django.urls import path

from tasks.views import show_specific_task, show_task


urlpatterns = [
    path('show-task/', show_task),
    path('show-task/<id>', show_specific_task)
]