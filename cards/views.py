from django.http import HttpResponse
from django.shortcuts import render

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

info = {
    "user_count": 2000,
    "cards_count": 1002000,
    "menu": ["Главная", "О проекте", "Каталог"],
}


def index(request):
    """
    Для отображения главной страницы
    Возвращает рендер шаблона cards/main.html
    :param request:
    :return:
    """
    return render(request, 'cards/main.html', context=info)


def about(request):
    """
    Возвращает информацию о проекте
    :param request:
    :return:
    """
    return render(request, 'cards/about.html', context=info)


def catalog(request):
    """
    Возвращает каталог карточек
    :param request:
    :return:
    """
    return render(request, 'cards/catalog.html')


def get_categories(request):
    """
    Возвращает карточку
    :param request:
    :return:
    """
    return HttpResponse("Категории")


def get_cards_by_category(request, slug):
    """
    Возвращает карточку
    :param request:
    :param slug:
    :return:
    """
    return HttpResponse(f"Карточки по категориям {slug}")


def get_card_by_tag(request, slug):
    """
    Возвращает карточку по тегу
    :param request:
    :param slug:
    :return:
    """
    return HttpResponse(f"Карточки по тегам {slug}")


def get_detail_card_by_id(request, card_id):
    """
    Возвращает детальную информацию о карточке
    :param request:
    :param card_id:
    :return:
    """
    return HttpResponse(f"Карточка {card_id}")
