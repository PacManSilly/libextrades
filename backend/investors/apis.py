from .models import InvestorInvestment, InvestorWithdrawal, ExpertTraders, Transaction
from rest_framework import status, views, viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .utils import resend_email_verification
from django.conf import settings
from . import serializers
import jwt


User = get_user_model()


class UserApiViewset(viewsets.GenericViewSet):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self, *args, **kwargs):
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [perm() for perm in permission_classes]

    def get_object(self, *args, **kwargs):
        """
        Edited so as to return the object instance of the currently logged in user.
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, email=self.request.user.email)

        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        fname, lname, email = (user.first_name, user.last_name, user.email)
        user.delete()
        data = {'first_name': fname, 'last_name': lname, 'email': email, 'detail': 'Deleted successfully'}
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)


class ResendVerifyEmail(viewsets.GenericViewSet):
    serializer_class = serializers.ResendEmailSerializer

    def post(self, request, *args, **kwargs):
        """
        Resends a new verificaton email.
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            # check if email belongs to the currently logged in user.
            if request.user.email == serializer.data['email']:
                resend_email_verification.delay(email=serializer.data['email'])
                return Response(data={"detail": _(F"A verification link has been sent to {serializer.data['email']}")})

            return Response(
                data={"error": _(F"Email address {serializer.data['email']} is not associated to your account")},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmail(views.APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        """
        Verifies a users account email address, gets the token from the url address.
        Return Success or Failure data.
        """
        token = request.GET.get('token')

        try:
            check_token = jwt.decode(token, key=settings.SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return Response(
                data={"error": _('Activation link expired, please request a new one.')},
                status=status.HTTP_400_BAD_REQUEST
            )
        except jwt.DecodeError:
            return Response(
                data={"error": _('Invalid token, please request a new one.')},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            user = User.objects.get(email=check_token['user_email'])

            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response(data={"detail": _("Email address verified successfully")}, status=status.HTTP_200_OK)

            return Response(
                data={"error": _("Your email address has already been verified")},
                status=status.HTTP_400_BAD_REQUEST
            )


class InvestorInvestmentApiViewset(viewsets.GenericViewSet):
    lookup_field = 'id'
    queryset = InvestorInvestment.objects.all()
    serializer_class = serializers.InvestorInvestmentSerializer

    def get_queryset(self):
        investor = self.request.user
        return investor.investorinvestment_set.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(investor=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save(investor=request.user)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None, *args, **kwargs):
        investment = self.get_object()
        id, plan, amount = (investment.id, investment.plan, investment.amount)
        investment.delete()
        data = {'id': id , 'plan': plan, 'amount': amount, 'detail': 'Deleted successfully'}
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)


class InvestorWithdrawalApiViewset(viewsets.GenericViewSet):
    lookup_field = 'id'
    queryset = InvestorWithdrawal.objects.all()
    serializer_class = serializers.InvestorWithdrawalSerializer

    def get_queryset(self):
        investor = self.request.user
        return investor.investorwithdrawal_set.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(investor=request.user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save(investor=request.user)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None, *args, **kwargs):
        investment = self.get_object()
        id, plan, amount = (investment.id, investment.plan, investment.amount)
        investment.delete()
        data = {'id': id , 'plan': plan, 'amount': amount, 'detail': 'Deleted successfully'}
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)


class TransactionApiViewset(viewsets.GenericViewSet):
    lookup_field = 'id'
    queryset = Transaction.objects.all()
    serializer_class = serializers.TransactionSerializer

    def get_queryset(self):
        investor = self.request.user
        return investor.transaction_set.all()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ExpertTraderApiViewSet(viewsets.GenericViewSet):
    lookup_field = 'id'
    queryset = ExpertTraders.objects.all()
    serializer_class = serializers.ExpertTraderSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, id=None, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data, context={'request': request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def destroy(self, request, id=None, *args, **kwargs):
    #     expert = self.get_object()
    #     id, name, email = (expert.id, expert.name, expert.email)
    #     expert.delete()
    #     data = {'id': id , 'full_name': name, 'email': email, 'detail': 'Deleted successfully'}
    #     return Response(data=data, status=status.HTTP_204_NO_CONTENT)

