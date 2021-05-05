from rest_framework.serializers import ModelSerializer
from coins.models import Coin


class CoinSerializer(ModelSerializer):
    class Meta:
        model = Coin
        fields = [
            'name',
            'symbol',
            'price',
            'rank',
            'image'
        ]
