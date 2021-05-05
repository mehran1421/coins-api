from rest_framework.viewsets import ModelViewSet
from coins.models import Coin
from .serializers import CoinSerializer


class CoinsViewSet(ModelViewSet):
	queryset = Coin.objects.all()
	serializer_class = CoinSerializer