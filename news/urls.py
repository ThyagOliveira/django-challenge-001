from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from .views import AuthorAdminViewSet, ArticleAdminViewSet, ArticleViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'admin/authors', AuthorAdminViewSet)
router.register(r'admin/articles', ArticleAdminViewSet)
router.register(r'articles', ArticleViewSet)


urlpatterns = [
    path("login/", views.obtain_auth_token),
    path("sign-up/", UserViewSet.as_view()),
    path("", include(router.get_urls()))
]

