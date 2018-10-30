from django.urls import path

from test_assignment.apps.account.views import LoginView, LogoutView, SignUpView, FollowView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('follow/<user_id>/', FollowView.as_view(), name='follow'),
]
