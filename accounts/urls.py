from django.urls import URLPattern, path
from .views import SignUpView
app_name = 'accounts'
urlpatterns= [
    path('signup/', SignUpView.as_view(), name='signup' ),
]
