from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from order.models import Shop,Menu,Order,Order_food
from django.views.decorators.csrf import csrf_exempt
from order.serializers import ShopSerializer,MenuSerializer
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def order_list(request):
    if request.method == 'GET':
        # shop = Shop.objects.all()
        # serializer = ShopSerializer(shop,many=True)
        # return JsonResponse(serializer.data, safe=False)

        order_list = Order.objects.all()        
        return render(request,'delivery/order_list.html',{"order_list":order_list})
    elif request.method == 'POST':
        order_id = request.POST['order_id']
                
        order_item = Order.objects.get(pk=int(order_id))
        shop = order_item.shop        
        order_item.deliver_time = order_item.estimated_time;
        order_item.save();

        # order_item = Order.objects.get(pk = shop_item.order_set.latest('id').id)
        # for food in food_list :
        #     order_item.order_food_set.create(food_name=food)

        return render(request,'delivery/success.html', {'shop':shop})
    