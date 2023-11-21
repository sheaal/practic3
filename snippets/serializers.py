from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
   class Meta:
       model = Snippet
       fields = ['id', 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.username')
   highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

   class Meta:
       model = Snippet
       fields = ['url', 'id', 'highlight', 'owner',
                 'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
   snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

   class Meta:
       model = User
       fields = ['url', 'id', 'username', 'snippets']
