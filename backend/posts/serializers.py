from rest_framework.serializers import ModelSerializer, SerializerMethodField
from posts.models import Post


class PostListSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content',
                  'image', 'slug', 'timestamp']

    def get_user(self, obj):
        return str(obj.user)


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'image')


class PostDetailSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'content',
            'image',
            'slug'
        ]


class PostCreateSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'image'
        ]
