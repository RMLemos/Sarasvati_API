from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers

from accounts.views import ProfileViewSet, UserViewSet
from library.views import AuthorViewSet, BookViewSet
from readers.views import NotesViewSet, RatingViewSet, StatusViewSet, UserBookViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)
router.register(r'mybooks', UserBookViewSet)
router.register(r'status', StatusViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'notes', NotesViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
