from django.utils.translation import gettext as _

from client.forms import ClientForm
from client.models import Client
from product.models import Product


def client_create(request_body):
    client_form = ClientForm(request_body)

    # If the client fields are valid
    if client_form.is_valid():
        # Save client
        user = client_form.save()
        # return new user id
        return {'success': True, 'message': _('New client created'), 'data': {'client_id': user.id}}

    # If there is any form error, return it
    else:
        return {'success': False, 'data': client_form.errors.as_json()}


def client_delete(client_id):
    # Load client
    client = Client.objects.filter(id=client_id)

    if client.exists():
        # Delete client and products favored
        client.delete()

        return {'success': True, 'message': _(f'Client {client_id} deleted')}

    else:
        return {'success': False, 'message': _('Client not found')}


def client_get(client_id):
    # Load client
    client = Client.objects.values('id', 'name', 'email').filter(id=client_id).first()

    if client:
        return {'success': True, 'data': client}
    else:
        return {'success': False, 'message': _('Client not found')}


def client_update(client_id, request_body):
    # Load client
    client = Client.objects.filter(id=client_id).first()

    if client:
        client_form = ClientForm(request_body, instance=client)

        if client_form.is_valid():
            client_form.save()

            data = Client.objects.values('id', 'name', 'email').filter(id=client_id).first()

            return {'success': True, 'message': _(f'Client {client_id} updated'), 'data': data}

        # If there is and error, return it
        else:
            return {'success': False, 'data': client_form.errors.as_json()}

    else:
        return {'error': _('Client not found')}


def favorite_create(client_id, product_id):
    # Load client
    client = Client.objects.filter(id=client_id).first()
    # Load product
    product = Product.objects.filter(id=product_id).first()

    # If client and product are valid
    if client and product:
        # If product already favored
        if client.products.filter(id=product_id).exists():
            return {'success': False, 'message': _('Product already favored')}
        else:
            # Add product to client
            client.products.add(product)

            return {'success': True, 'message': _('Product favored'), 'data': {
                'client_id': client_id,
                'product_id': product_id}}

    elif not client:
        return {'success': False, 'message': 'Client not found'}

    elif not product:
        return {'success': False, 'message': 'Product not found'}


def favorite_remove(client_id, product_id):
    # Load client
    client = Client.objects.filter(id=client_id).first()
    # Load product
    product = Product.objects.filter(id=product_id).first()

    if client and product:
        # If don't find product favored
        if not client.products.filter(id=product_id).exists():
            return {'success': False, 'message': _('Product not favored')}
        else:
            # Remove product
            client.products.remove(product)

            return {'success': True, 'message': _('Product removed from favorites'), 'data': {
                'client_id': client_id,
                'product_id': product_id}}

    elif not client:
        return {'success': False, 'message': 'Client not found'}

    elif not product:
        return {'success': False, 'message': 'Product not found'}
