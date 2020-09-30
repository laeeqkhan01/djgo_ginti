from django.urls import path
from .           import views

urlpatterns = [
  path(''                 , views.sab_aadaad , name='sab_aadaad' ),
  path('num/<int:pk>/'    , views.full_detail, name='full_detail'),
  path('num/new_adad/'    , views.new_adad   , name='new_adad'   ),
  path('num/<int:pk>/edit', views.edit_entry , name='edit_entry' ),
]
