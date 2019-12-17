from django.utils.translation import gettext as _

from product.forms import ProductForm
from product.models import Product


def product_create(request_body):
    product_form = ProductForm(request_body)

    # If the product fields are valid
    if product_form.is_valid():
        # Save product
        product = product_form.save()
        # return new product id
        return {'success': True, 'message': _('New product created'), 'data': {'product_id': product.id}}

    # If there is any form error, return it
    else:
        return {'success': False, 'data': product_form.errors.as_json()}


def product_delete(product_id):
    # Load product
    product = Product.objects.filter(id=product_id)

    if product.exists():
        # Delete product
        product.delete()

        return {'success': True, 'message': _(f'Product {product_id} deleted')}

    else:
        return {'success': False, 'message': _('Product not found')}


def product_get(product_id):
    # Load product
    product = Product.objects.values('title', 'brand', 'image', 'price', 'review_score').filter(id=product_id).first()

    if product:
        return {'success': True, 'data': product}
    else:
        return {'success': False, 'message': _('Product not found')}


def product_update(product_id, request_body):
    # Load product
    product = Product.objects.filter(id=product_id).first()

    if product:
        product_form = ProductForm(request_body, instance=product)

        if product_form.is_valid():
            product_form.save()

            data = Product.objects.values('title', 'brand', 'image', 'price').filter(id=product_id).first()

            return {'success': True, 'message': _(f'Product {product_id} updated'), 'data': data}

        # If there is and error, return it
        else:
            return {'success': False, 'data': product_form.errors.as_json()}

    else:
        return {'error': _('Product not found')}
