from django.db import models


class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=5000)
    upload_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    adds = models.IntegerField(default=0)
    tags = models.JSONField()

    class Meta:
        db_table = 'Cards'
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return f'Карточка {self.question} - {self.answer[:50]}'


# from cards.models import Card
# from django.utils import timezone
# import json
#
# # Пример карточек
# cards_data = [
#     {
#         "question": "Что такое PEP 8?",
#         "answer": "PEP 8 — это документ, описывающий соглашение о том, как писать код для языка Python, включая стандарты оформления кода.",
#         "tags": json.dumps(["Python", "PEP 8", "стиль кода"])
#     },
#     {
#         "question": "Как в Python создать виртуальное окружение?",
#         "answer": "Используйте команду `python -m venv your_env_name` для создания виртуального окружения.",
#         "tags": json.dumps(["Python", "виртуальное окружение", "venv"])
#     },
#     {
#         "question": "Что делает оператор `yield`?",
#         "answer": "Оператор `yield` используется в функциях-генераторах и позволяетфункции возвращать промежуточные результаты работы, останавливаясь на каждом `yield`и возобновляя выполнение с этого места.",
#         "tags": json.dumps(["Python", "yield", "генераторы"])
#     },
#     {
#         "question": "Какие типы данных в Python являются неизменяемыми?",
#         "answer": "Неизменяемыми типами данных в Python являются числа (int, float),строки (str) и кортежи (tuple).",
#         "tags": json.dumps(["Python", "типы данных", "неизменяемые типы"])
#     },
#     {
#         "question": "Что такое list comprehension и как его использовать?",
#         "answer": "List comprehension — это синтаксическая конструкция,предназначенная для создания списков из других списков, применяя к каждому элементунекоторое выражение или фильтр.",
#         "tags": json.dumps(["Python", "list comprehension", "списки"])
#     }
# ]
