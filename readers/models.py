from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from utils.images import resize_image
from accounts.models import Profile
from uuid import uuid4


class Base(models.Model):
    created_at = models.DateField('Created at', auto_now_add=True)
    updated_at = models.DateField('Updated at', auto_now=True)

    class Meta:
        abstract = True

class UserBook(Base):

    class Meta:
        verbose_name = 'My Book'
        verbose_name_plural = 'My Books'
        db_table = 'user_books'

    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cover = models.ImageField(upload_to='readers/cover', blank=True, default='')
    title = models.CharField('Title', max_length=100)
    publisher = models.CharField('Publisher', max_length=100)
    isbn = models.CharField('ISBN', unique=True, max_length=100)
    nr_pages = models.IntegerField('Pages',  null=True, blank=True)
    synopsis = models.TextField('Synopsis', null=True, blank=True)
    author = models.CharField('Author(s)', max_length=255, null=True, blank=True)
    owner = models.ForeignKey(Profile, related_name='books', on_delete=models.CASCADE,)

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


class Status(Base):

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        db_table = 'status'
    
    STATUS_CHOICES = (
        (1, 'Read'),
        (2, 'Want to read'),
        (3, 'Current reading'),
    )

    id_status = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.IntegerField(choices=STATUS_CHOICES)
    book = models.ForeignKey(UserBook, related_name='status', on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Status: {self.get_status_display()}"
    

class Rating(Base):

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Rating'
        db_table = 'rating' 

    id_rating = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    rating = models.PositiveIntegerField(blank=True, null=True, default=0,  validators=[MinValueValidator(0), MaxValueValidator(5),])
    book = models.ForeignKey(UserBook, related_name='rating', on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __int__(self):
        return self.rating
    

class Notes(Base):

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        db_table = 'notes'

    id_notes = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    note = models.TextField('Notes', blank=True, null=True,)
    book = models.ForeignKey(UserBook, related_name='notes', on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.note