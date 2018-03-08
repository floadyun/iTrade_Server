from rest_framework import viewsets
from strategy.models import Strategy
from strategy.serialzers import StrategySerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class StrategyViewSet(viewsets.ModelViewSet):
    queryset = Strategy.objects.all()
    serializer_class = StrategySerializers

@api_view(['POST'])
def addStrategy(request):
    title = request.query_params['strategy_title']
    content = request.query_params['strategy_content']
    strategy = Strategy()
    strategy.strategy_title = title
    strategy.strategy_content = content
    strategy.save()
    return Response('发布成功')

@api_view(['GET'])
def getStrategyList(request):
    strategys = Strategy.objects.all()
    serializer = StrategySerializers(strategys, many=True)
    return Response({'data': serializer.data})