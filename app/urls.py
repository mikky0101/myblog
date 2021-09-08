from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home, blog, search, details, BlogDetailView, post_create, post_delete, post_update, contact, author_profile, about, technology, sports, nature, education, entertainment

app_name = 'blog'

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('technology/', technology, name="technology"),
    path('entertainment/', entertainment, name="entertaiment"),
    path('education/', education, name="education"),
    path('sports/', sports, name="sports"),
    path('nature/', nature, name="nature"),
    path('blog/', blog, name="blog"),
    path('search/', search, name="search"),
    path('details/<int:pk>/', details, name="detail"),
    path('create/', post_create, name='create'),
    path('profile/<int:pk>/', author_profile, name='profile'),
    path('post/<id>/update/', post_update, name='update'),
    path('post/<id>/delete/', post_delete, name='delete'),
    path('details/<slug>/', BlogDetailView.as_view(), name="details"),
    path("contact/", contact, name="contact")
]