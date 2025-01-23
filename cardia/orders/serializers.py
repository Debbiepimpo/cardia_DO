from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product = Product.objects.get(id=item_data['product'].id)
            if product.stock < item_data['quantity']:
                raise serializers.ValidationError(f"Producto {product.name} fuera de stock.")
            product.stock -= item_data['quantity']
            product.save()
            OrderItem.objects.create(order=order, product=product, **item_data)
        return order
