from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),  # Общий каталог карточек
    path('categories/', views.get_categories, name='categories'),  # Список всех категорий
    path('categories/<slug:slug>/', views.get_cards_by_category, name='category'),  # Карточки по категориям
    path('tags/<slug:slug>/', views.get_card_by_tag, name='tag'),  # Карточки по тегам
    path('<int:card_id>/detail/', views.get_detail_card_by_id, name='detail'),  # Детальная информация

]
