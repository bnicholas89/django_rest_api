from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer
from .models import Post


class UserSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('password',)
        read_only_fields = ()

    def update(self, instance, validated_data):
        if 'password' not in validated_data:
            raise serializers.ValidationError(
                {'error': 'password is required'})
        elif instance.check_password(validated_data['password']):
            del validated_data['password']
            return super(UserSerializer, self).update(instance, validated_data)
        else:
            raise serializers.ValidationError(
                {'error': 'password is incorrect'})


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner'
        )
