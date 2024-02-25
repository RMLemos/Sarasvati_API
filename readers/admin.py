from django.contrib import admin

from readers.models import Notes, Rating, Status, UserBook

@admin.register(UserBook)
class UserBookAdmin(admin.ModelAdmin):
    list_display = 'id_book', 'title', 'publisher', 'nr_pages', 'isbn', 'synopsis',
    list_display_links = 'title',
    search_fields = 'title', 'isbn',
    list_per_page = 10
    ordering = 'title',
    readonly_fields = (
        'created_at', 'updated_at',
    )


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = 'id_status', 'status',
    search_fields = 'status',
    list_per_page = 10
    readonly_fields = (
        'created_at', 'updated_at',
    )
    autocomplete_fields = 'book',


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = 'id_rating', 'rating',
    list_per_page = 10
    readonly_fields = (
        'created_at', 'updated_at',
    )
    autocomplete_fields = 'book',

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = 'id_notes', 'note',
    list_display_links = 'note',
    list_per_page = 10
    readonly_fields = (
        'created_at', 'updated_at',
    )
    autocomplete_fields = 'book',