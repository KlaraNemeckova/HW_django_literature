from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('writers/', views.writers, name='writers'),
    path('books/', views.best_books, name='best books'),  # name se pak píše do navigation, v tomto případě 'best books'
    path('books/<int:id>', views.details, name='details'),
    path('writers/Hemingway', views.hemingway, name='Hemingway'),
    path('writers/Shakespeare', views.shakespeare, name='Shakespeare'),
    path('writers/Hemingway/The_Old_Man_and_the_Sea', views.the_old_man, name='The old man'),
    path('writers/Hemingway/The_Sun_Also_Rises', views.the_sun, name='The sun'),
    path('writers/Hemingway/1926', views.published_1926, name='Books published 1926'),
    path('writers/Hemingway/1940', views.published_1940, name='Books published 1940'),

]

