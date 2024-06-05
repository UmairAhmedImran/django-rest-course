from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Products
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    # body = request.body
    # print(request.GET)
    # print(request.POST)

    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content)type'] = request.content_type
    data = request.data
    # instance = Products.objects.all().order_by("?").first()

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # instead of all above we can write
        # data = ProductSerializer(instance).data
        message = serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"Error": "Some wierd shit happened"}, status=404)
