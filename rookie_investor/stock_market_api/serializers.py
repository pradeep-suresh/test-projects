from rest_framework import serializers
from stock_market_api.models import DividendHistory

class DividendHistorySerializer(serializers.ModelSerializer):
    class Meta:
        