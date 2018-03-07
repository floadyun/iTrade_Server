from rest_framework import serializers
from strategy.models import Strategy

class StrategySerializers(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('id', 'strategy_title', 'strategy_content', 'publish_date', 'browse_count', 'pay_count', 'user_id', 'is_pay_money')