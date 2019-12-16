import json

from json import JSONDecodeError

from django.http import JsonResponse
from django.urls import reverse
from django.utils.translation import gettext as _

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from client.models import Client
from client.processors import client_create, client_delete, client_get, client_update, favorite_create, favorite_remove
from product.models import Product
from product.processors import product_create, product_delete, product_get, product_update


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def client_add(request):
    context = {}

    # Get Json from request body
    try:
        request_body = json.loads(request.body)

    # If Json is not valid
    except JSONDecodeError:
        context = {'success': False, 'message': _('Invalid body format. Must be a valid Json')}

    # With a valid json
    else:
        request_body['email'] = request_body.get('email').lower()

        # Get or create User, using Django Forms
        context = client_create(request_body)

        # # Is the function returns an User instance
        # if isinstance(client, User):
        #     context = client
        #
        # # If the client is not valid, returns forms errors
        # else:
        #     context = client

    # Return json request
    finally:
        return JsonResponse(context, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def client_management(request, client_id):
    context = {}

    # Delete client
    if request.method == 'DELETE':
        context = client_delete(client_id)

    # Load client
    elif request.method == 'GET':
        context = client_get(client_id)

    # Update client
    elif request.method == 'PUT':
        # Get Json from request body
        try:
            request_body = json.loads(request.body)

        # If Json is not valid
        except json.JSONDecodeError:
            context = {'success': False, 'message': _('Invalid body format. Must be a valid Json')}

        # With a valid json
        else:
            context = client_update(client_id, request_body)

    return JsonResponse(context, safe=False)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def client_products_management(request):
    context = {}

    # Get Json from request body
    try:
        request_body = json.loads(request.body)

    # If Json is not valid
    except JSONDecodeError:
        context = {'success': False, 'message': _('Invalid body format. Must be a valid Json')}

    # With a valid json
    else:
        # Get or create Favorite
        client_id = request_body.get('client_id')
        product_id = request_body.get('product_id')

        if client_id and product_id:
            if request.method == 'POST':
                context = favorite_create(client_id, product_id)
            if request.method == 'DELETE':
                context = favorite_remove(client_id, product_id)
        else:
            context = {'success': False, 'message': _('Invalid body format. Must have a client_id and product_id')}

    # Return json request
    finally:
        return JsonResponse(context, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def client_product_load(request, client_id):
    # Load client
    client = Client.objects.values('id').filter(id=client_id)

    if not client:
        context = {'success': False, 'message': _('Client not found')}
    else:
        page = int(request.GET.get('page', 1))
        page = 1 if page is 0 else page
        per_page = 3
        prev_page = page - 1
        next_page = page + 1
        start = per_page * (page - 1)
        end = per_page + start

        total_products = Product.objects.values().filter(client__id__exact=client_id).count()
        values = ['title', 'brand', 'image', 'price', 'review_score']
        products = Product.objects.values(*values).filter(client__id__exact=client_id).order_by('title')[start: end]

        context = {'success': True, 'data': list(products)}

        url_prev = f"{reverse('client-products', args=(client_id,))}?page={prev_page}" if prev_page >= 1 else None
        url_next = f"{reverse('client-products', args=(client_id,))}?page={next_page}" if end < total_products else None

        context.update({'prev_page': url_prev})
        context.update({'next_page': url_next})

    return JsonResponse(context, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_add(request):
    context = {}

    # Get Json from request body
    try:
        request_body = json.loads(request.body)

    # If Json is not valid
    except JSONDecodeError:
        context = {'success': False, 'message': _('Invalid body format. Must be a valid Json')}

    # With a valid json
    else:
        # Get or create User, using Django Forms
        context = product_create(request_body)

    # Return json request
    finally:
        return JsonResponse(context, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def product_management(request, product_id):
    context = {}

    # Delete product
    if request.method == 'DELETE':
        context = product_delete(product_id)

    # Load product
    elif request.method == 'GET':
        context = product_get(product_id)

    # Update product
    elif request.method == 'PUT':
        # Get Json from request body
        try:
            request_body = json.loads(request.body)

        # If Json is not valid
        except json.JSONDecodeError:
            context = {'success': False, 'message': _('Invalid body format. Must be a valid Json')}

        # With a valid json
        else:
            context = product_update(product_id, request_body)

    return JsonResponse(context, safe=False)
