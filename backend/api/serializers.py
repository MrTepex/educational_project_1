from rest_framework import serializers


class ColorSerializer(serializers.Serializer):
    """Сериализатор для работы с цветами"""
    color = serializers.CharField(max_length=50)
    hex = serializers.CharField(max_length=7, read_only=True)


class CalculatorSerializer(serializers.Serializer):
    """Сериализатор для калькулятора"""
    a = serializers.FloatField()
    b = serializers.FloatField()
    operation = serializers.ChoiceField(choices=['+', '-', '*', '/'])
    result = serializers.FloatField(read_only=True) 