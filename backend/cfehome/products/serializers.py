from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from . import validators


class ProductSerializer(serializers.ModelSerializer):
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[
            validators.unique_validate_title,
            validators.validate_title_no_hello,
        ]
    )
    name = serializers.CharField(source="title", read_only=True)

    class Meta:
        model = Product
        fields = [
            "user",
            "url",
            "edit_url",
            "id",
            "title",
            "content",
            "name",
            "price",
            "sale_price",
            "my_discount",
            "username",
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")

    #     return value

    """
    example
    ====================
    def create(self, validated_data):
        # email = validated_data.pop("email")
        # print(email)
        # email = Product.objects.create(**validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title")
        return instance
    """

    def get_my_user_data(self, obj):
        return {"username": obj.user.username}

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
