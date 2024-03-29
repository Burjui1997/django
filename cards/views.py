from django.http import HttpResponse
from django.shortcuts import render
from .models import Card
from django.shortcuts import get_object_or_404
from django.db.models import F

"""
Index- возвращает главную страницу шаблона cards/main.html
about - возвращает информацию о проекте
catalog- возвращает каталог карточек
get_all_cards- возвращает все карточки для представления в каталоге
get_categories- возвращает карточку
get_cards_by_category- возвращает карточку
get_card_by_tag- возвращает карточку по тегу
get_detail_card_by_id- возвращает детальную информацию о карточке

Информация в шаблоны будет браться из базы данных, но пока мы сделаем переменные

"""
cards_dataset = [
    {"question": "Что такое PEP 8?",
     "answer": "PEP 8 — стандарт написания кода на Python.",
     "category": "Стандарты кода",
     "tags": ["PEP 8", "стиль", "форматирование"],
     "id_author": 1,
     "id_card": 1,
     "upload_date": "2023-01-15",
     "views_count": 100,
     "favorites_count": 25
     },
    {"question": "Как объявить список в Python?",
     "answer": "С помощью квадратных скобок: lst = []",
     "category": "Основы",
     "tags": ["списки", "основы"],
     "id_author": 2,
     "id_card": 2,
     "upload_date": "2023-01-20",
     "views_count": 150,
     "favorites_count": 30
     },
    {"question": "Что делает метод .append()?",

     "answer": "Добавляет элемент в конец списка.",
     "category": "Списки",
     "tags": ["списки", "методы"],
     "id_author": 2,
     "id_card": 3,
     "upload_date": "2023-02-05",
     "views_count": 75,
     "favorites_count": 20
     },
    {"question": "Какие типы данных в Python иммутабельные?",
     "answer": "Строки, числа, кортежи.",
     "category": "Типы данных",
     "tags": ["типы данных", "иммутабельность"],
     "id_author": 1,
     "id_card": 4,
     "upload_date": "2023-02-10",
     "views_count": 90,
     "favorites_count": 22
     },
    {"question": "Как создать виртуальное окружение в Python?",
     "answer": "С помощью команды: python -m venv myenv",
     "category": "Виртуальные окружения",
     "tags": ["venv", "окружение"],
     "id_author": 2,
     "id_card": 5,
     "upload_date": "2023-03-01",
     "views_count": 120,
     "favorites_count": 40
     }
]
info = {
    "users_count": 100500,
    "cards_count": 200600,
    # "menu": ['Главная', 'О проекте', 'Каталог']
    "menu": [
        {"title": "Главная",
         "url": "/",
         "url_name": "index"},
        {"title": "О проекте",
         "url": "/about/",
         "url_name": "about"},
        {"title": "Каталог",
         "url": "/cards/catalog/",
         "url_name": "catalog"},
    ], "cards": cards_dataset
}


def index(request):
    """
    Для отображения главной страницы
    Возвращает рендер шаблона cards/main.html
    :param request:
    :return:
    """
    return render(request, 'main.html', context=info)


def about(request):
    """
    Возвращает информацию о проекте
    :param request:
    :return:
    """
    return render(request, 'about.html', context=info)


def catalog(request):
    # Считываем параметры из GET запроса
    sort = request.GET.get('sort', 'upload_date')  # по умолчанию сортируем по дате загрузки
    order = request.GET.get('order', 'desc')  # по умолчанию используем убывающий порядок

    # Сопоставляем параметр сортировки с полями модели
    valid_sort_fields = {'upload_date', 'views', 'adds'}
    if sort not in valid_sort_fields:
        sort = 'upload_date'  # Возвращаемся к сортировке по умолчанию, если передан неверный ключ сортировки

    # Обрабатываем порядок сортировки
    if order == 'asc':
        order_by = sort
    else:
        order_by = f'-{sort}'

    # Получаем отсортированные карточки
    cards = Card.objects.all().order_by(order_by)

    # Подготавливаем контекст и отображаем шаблон
    context = {
        'cards': cards,
        'cards_count': cards.count(),
        'menu': info['menu'],
    }
    return render(request, 'cards/catalog.html', context=context)


def get_categories(request):
    """
    Возвращает карточку
    :param request:
    :return:
    """
    return render(request, 'Base.html')


def get_cards_by_category(request, slug):
    """
    Возвращает карточку
    :param request:
    :param slug:
    :return:
    """
    return HttpResponse(f"Карточки по категориям {slug}")


def get_cards_by_tag(request, tag_id):
    """
    Возвращает карточку
    :param request:
    :param tag_id:
    :return:
    """
    cards = Card.objects.filter(tags=tag_id)
    context = {
        'cards': cards,
        'cards_count': cards.count(),
        'menu': info['menu'],
    }
    return render(request, 'cards/catalog.html', context)


def get_detail_card_by_id(request, card_id):
    """
    Возвращает шаблон cards/templates/cards/card_detail.html с детальной информацией по карточке
    """
    card = {
        "card": get_object_or_404(Card, id=card_id),
        "menu": info["menu"]
    }

    return render(request, 'cards/card_detail.html', status=200, context=card)

def get_detail_card_by_id(request, card_id):
    """
    /cards/<int:card_id>/detail/
    Возвращает шаблон cards/templates/cards/card_detail.html с детальной информацией по карточке
    """

    # Добываем карточку из БД через get_object_or_404
    # если карточки с таким id нет, то вернется 404
    # Используем F object для обновления счетчика просмотров (views)

    card_obj = get_object_or_404(Card, pk=card_id)
    card_obj.views = F('views') + 1
    card_obj.save()

    card_obj.refresh_from_db()  # Обновляем данные из БД

    card = {
        "card": card_obj,
        "menu": info["menu"],
    }

    return render(request, 'cards/card_detail.html', card, status=200)