from posts.models import Post, Group, Comment, User, Follow

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'author', 'posts')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user','following'),
            message=('Подписка невозможна')
    )]

    def validate(self,data):
       if data['following'] == self.context['request'].user:
           raise serializers.ValidationError('Подписка на самого себя невозможна')
       return data
