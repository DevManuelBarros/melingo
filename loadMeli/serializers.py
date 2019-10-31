from rest_framework import serializers
from .models import LoginModel
 
class LoginModelSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.access_token   = validated_data.get('access_token', instance.access_token)
        instance.token_type     = validated_data.get('token_type', instance.token_type)
        instance.expires_in     = validated_data.get('expires_in', instance.expires_in)
        instance.scope          = validated_data.get('scope', instance.scope)
        instance.refresh_token  = validated_data.get('refresh_token', instance.refresh_token)
        instance.user_id        = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance