from django.db import models

from uuid import uuid4
from utils.images import resize_image

class Base(models.Model):
    created_at = models.DateField('Created at', auto_now_add=True)
    updated_at = models.DateField('Updated at', auto_now=True)

    class Meta:
        abstract = True


class Author(Base):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        db_table = 'authors'

    id_author = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    picture = models.ImageField(upload_to='pictures/authors/', blank=True, default='')
    name = models.CharField('Name', max_length=100)
    country = models.CharField('Country', max_length=100)
    bio = models.TextField('Bio', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        current_picture_name = str(self.picture.name)
        super_save = super().save(*args, **kwargs)
        picture_changed = False

        if self.picture:
            picture_changed = current_picture_name != self.picture.name

        if picture_changed:
            resize_image(self.picture, 900, True, 70)

        return super_save


class Book(Base):

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'books'

    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cover = models.ImageField(upload_to='pictures/cover', blank=True, default='')
    title = models.CharField('Title', max_length=100)
    publisher = models.CharField('Publisher', max_length=100)
    isbn = models.CharField('ISBN', unique=True, max_length=100)
    nr_pages = models.IntegerField('Pages',  null=True, blank=True)
    synopsis = models.TextField('Synopsis', null=True, blank=True)
    author = models.ManyToManyField(Author, verbose_name='Author(s)', related_name='book')

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        current_cover_name = str(self.cover.name)
        super_save = super().save(*args, **kwargs)
        cover_changed = False

        if self.cover:
            cover_changed = current_cover_name != self.cover.name

        if cover_changed:
            resize_image(self.cover, 900, True, 70)

        return super_save




