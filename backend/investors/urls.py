from rest_framework_simplejwt.views import TokenVerifyView
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth import views as dj_rest
from django.urls import path
from . import apis


urlpatterns = [

    # Authenication endpoint
    path("auth/token/login/", dj_rest.LoginView.as_view(), name="login_via_token"),
    path("auth/token/logout/", dj_rest.LogoutView.as_view(), name="logout_via_token"),
    path("auth/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("auth/token/refresh/", get_refresh_view().as_view(), name="token_refresh"),

    # users endpoint
    path('users/', apis.UserApiViewset.as_view({'get': 'list'}), name='users_list'),
    path('users/new/', apis.UserApiViewset.as_view({'post': 'create'}), name='users_create'),
    path('users/me/', apis.UserApiViewset.as_view({'get': 'retrieve'}), name='users_detail'),
    path('users/me/update/', apis.UserApiViewset.as_view({'put': 'update', 'patch': 'update'}), name='users_update'),
    path('users/me/delete/', apis.UserApiViewset.as_view({'delete': 'destroy'}), name='users_delete'),
    path("users/me/change/password/", dj_rest.PasswordChangeView.as_view(), name="users_change_password"),

    # Investors investments endpoints
    path('investments/', apis.InvestorInvestmentApiViewset.as_view({'get': 'list'}), name='investments_list'),
    path('investments/new/', apis.InvestorInvestmentApiViewset.as_view({'post': 'create'}), name='investments_create'),
    path('investments/<int:id>/', apis.InvestorInvestmentApiViewset.as_view({'get': 'retrieve'}), name='investments_detail'),
    path('investments/<int:id>/update/', apis.InvestorInvestmentApiViewset.as_view({'put': 'update', 'patch': 'update'}), name='investments_update'),
    path('investments/<int:id>/delete/', apis.InvestorInvestmentApiViewset.as_view({'delete': 'destroy'}), name='investments_delete'),

    # Investors withdrawal endpoints
    path('withdrawals/', apis.InvestorWithdrawalApiViewset.as_view({'get': 'list'}), name='withdrawals_list'),
    path('withdrawals/new/', apis.InvestorWithdrawalApiViewset.as_view({'post': 'create'}), name='withdrawals_create'),
    path('withdrawals/<int:id>/', apis.InvestorWithdrawalApiViewset.as_view({'get': 'retrieve'}), name='withdrawals_detail'),
    path('withdrawals/<int:id>/update/', apis.InvestorWithdrawalApiViewset.as_view({'put': 'update', 'patch': 'update'}), name='withdrawals_update'),
    path('withdrawals/<int:id>/delete/', apis.InvestorWithdrawalApiViewset.as_view({'delete': 'destroy'}), name='withdrawals_delete'),

    # expert traders endpoint
    path('experts/', apis.ExpertTraderApiViewSet.as_view({'get': 'list'}), name="experts_list"),
    path('experts/new/', apis.ExpertTraderApiViewSet.as_view({'post': 'create'}), name="experts_create"),
    path('experts/<uuid:id>/', apis.ExpertTraderApiViewSet.as_view({'get': 'retrieve'}), name="experts_detail"),
    path('experts/<uuid:id>/update/', apis.ExpertTraderApiViewSet.as_view({'put': 'update', 'patch': 'update'}), name="experts_update"),

    # Email verification endpoint
    path('verify-email/', apis.VerifyEmail.as_view(), name='verify_email'),
    path("resend-email/", apis.ResendVerifyEmail.as_view({'post': 'post'}), name="resend_verification_email"),

    # reset passeword endpoint
    # this url endpoint is used to actually change the password
    path("auth/help/password/reset/confirm/<str:uidb64>/<str:token>/", dj_rest.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

]
