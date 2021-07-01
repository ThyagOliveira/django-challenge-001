from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser

from .serializers import AuthorSerializer, ArticleSerializer, ArticleSearchSerializer, ArticleAdminSerializer, \
    ArticleAnonymousSerializer, CustomUser
from .models import Author, Article
from .filters import CustomSearchFilter


class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUser


class AuthorAdminViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]


class ArticleAdminViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleAdminSerializer
    permission_classes = [IsAdminUser]


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = ['category']

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSearchSerializer
        if self.request.user.is_anonymous:
            return ArticleAnonymousSerializer
        return super().get_serializer_class()

