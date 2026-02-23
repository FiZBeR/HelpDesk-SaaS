from rest_framework import serializers
from .models import UsuarioModel

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = ['id', 'username', 'password', 'email', 'rol', 'telefono']
        extra_kwargs = {
            'password' : {'write_only': True},
            'rol' : {'required': True}
        }

    def create (self, validate_data):
        password = validate_data.pop('password')
        user = UsuarioModel(**validate_data)
        user.set_password(password)
        user.save()

        return user