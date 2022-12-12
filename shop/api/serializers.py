from rest_framework import serializers
from product.models import Product
from service.convert import convert_to_webp


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField(method_name="get_image")

    class Meta:
        model = Product
        fields = "__all__"

    # Переопределяем поле image
    def get_image(self, obj):
        path = "/" + obj.image.name[:-4]
        formats = [obj.image.name[-3::], "webp"]
        data = {"path": path, "formats": formats}
        return data

    # Проверяем валидность формата загруженной картинки
    def validate(self, data):
        valid_formats = ("png", "jpg")
        image = self.context["image"]
        if image and image.name.split(".")[-1] in valid_formats:
            data["image"] = image
            return data
        data = {"error": "Отсутствует изображение или имеет не верный формат."}
        raise serializers.ValidationError(data)

    """Если все поля успешно создаются и конвертация картинки в
       webp завершилась успехом, тогда сохраняем новую запись в БД"""
    def create(self, validated_data):
        obj = Product.objects.create(**validated_data)
        if convert_to_webp(validated_data["image"], obj.image.name):
            obj.save()
            return obj
        data = {"error": "Ошибка конвертации изображения, данные не были сохранены."}
        raise serializers.ValidationError(data)
