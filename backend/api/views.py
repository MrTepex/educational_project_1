import webcolors
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ColorSerializer, CalculatorSerializer


@api_view(['POST'])
def color_view(request):
    """API endpoint для работы с цветами"""
    serializer = ColorSerializer(data=request.data)
    
    if serializer.is_valid():
        color_input = serializer.validated_data['color']
        
        try:
            # Пытаемся преобразовать название цвета в HEX
            if color_input.startswith('#'):
                # Если уже HEX формат
                hex_color = color_input
                color_name = color_input
            else:
                # Пытаемся найти название цвета
                hex_color = webcolors.name_to_hex(color_input)
                color_name = color_input
                
            return Response({
                'color': color_name,
                'hex': hex_color
            })
            
        except ValueError:
            # Если цвет не найден, возвращаем ошибку
            return Response({
                'error': f'Цвет "{color_input}" не найден. Попробуйте использовать HEX формат (#FF0000) или стандартные названия цветов.'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def calculator_view(request):
    """API endpoint для калькулятора"""
    serializer = CalculatorSerializer(data=request.data)
    
    if serializer.is_valid():
        a = serializer.validated_data['a']
        b = serializer.validated_data['b']
        operation = serializer.validated_data['operation']
        
        try:
            if operation == '+':
                result = a + b
            elif operation == '-':
                result = a - b
            elif operation == '*':
                result = a * b
            elif operation == '/':
                if b == 0:
                    return Response({
                        'error': 'Деление на ноль невозможно'
                    }, status=status.HTTP_400_BAD_REQUEST)
                result = a / b
            else:
                return Response({
                    'error': 'Неподдерживаемая операция'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({
                'result': result,
                'operation': operation,
                'a': a,
                'b': b
            })
            
        except Exception as e:
            return Response({
                'error': f'Ошибка вычисления: {str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 