from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from articles.views import tech_index, tech_category_01, tech_category_02, tech_category_03, tech_single, tech_contact, tech_author

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tech_index),
    path('tech-index/', tech_index, name='tech_index'),
    path('tech_category_01/', tech_category_01, name='tech_category_01'),
    path('tech_category_02/', tech_category_02, name='tech_category_02'),
    path('tech_category_03/', tech_category_03, name='tech_category_03'),
    path('tech_single/', tech_single, name='tech_single'),
    path('tech_contact/', tech_contact, name='tech_contact'),
    path('tech_author', tech_author, name='tech_author'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
