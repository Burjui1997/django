from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_column='CategoryID')
    name = models.CharField(max_length=255, unique=True, db_column='Name')

    class Meta:
        db_table = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True, db_column='TagID')
    name = models.CharField(max_length=255, unique=True, db_column='Name')

    class Meta:
        db_table = 'Tags'


class Card(models.Model):
    card_id = models.AutoField(primary_key=True, db_column='CardID')
    question = models.TextField(db_column='Question')
    answer = models.TextField(db_column='Answer')
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, db_column='CategoryID')
    upload_date = models.DateTimeField(auto_now_add=True, db_column='UploadDate')
    views = models.IntegerField(default=0, db_column='Views')
    favorites = models.IntegerField(default=0, db_column='Favorites')
    tags = models.ManyToManyField('Tag', related_name='cards', through='CardTags')

    class Meta:
        db_table = 'Cards'

    def __str__(self):
        return self.question


class CardTags(models.Model):
    card = models.ForeignKey('Card', on_delete=models.CASCADE, db_column='CardID')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, db_column='TagID')

    class Meta:
        db_table = 'CardTags'
        unique_together = (('card', 'tag'),)

    def __str__(self):
        return f'{self.card} - {self.tag}'
