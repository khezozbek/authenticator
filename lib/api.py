from rest_framework.pagination import PageNumberPagination
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Password
from .serializers import PasswordSerializers


def redirect_to_login(request):
    return HttpResponseRedirect(reverse('login'))


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class Pagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'


class PasswordAPIView(generics.ListCreateAPIView):
    serializer_class = PasswordSerializers
    pagination_class = PageNumberPagination
    page_size = 5

    def get_queryset(self):
        queryset = Password.objects.all()
        search_term = self.request.query_params.get('search', None)

        if search_term:
            queryset = queryset.annotate(
                similarity=Greatest(
                    TrigramSimilarity('address', search_term),
                )
            ).filter(similarity__gte=0.2).order_by('-similarity')
        return queryset


class PasswordUpdateAPIVIew(generics.UpdateAPIView):
    queryset = Password.objects.all()
    serializer_class = PasswordSerializers
