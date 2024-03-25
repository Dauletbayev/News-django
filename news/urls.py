from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from articles import views
from articles.views import HomePage, search_results, article_page, category_page,MyLoginView, logout_view, contact_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePage.as_view(), name='home'),
    path('search_results', search_results),
    path('articles/<int:pk>', article_page),
    path('category/<int:pk>', category_page),
    path("article/<int:pk>", views.NewsDetailView.as_view(), name='article'),
    path("create/", views.NewsCreateView.as_view(), name='create'),
    path("edit/<int:pk>", views.NewsUpdateView.as_view(), name='edit'),
    path("delete/<int:pk>", views.NewsDeleteView.as_view(), name='delete'),
    path('login/', MyLoginView.as_view()),
    path('logout/', logout_view),
    path("contact/", contact_us, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
