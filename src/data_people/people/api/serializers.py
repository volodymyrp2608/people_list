from rest_framework import serializers
from people.models import List_People

class ListPeopleSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = List_People
        fields = [
            'url',
            'id',
            'user',
            'surname',
            'name',
            'birthday',
            'mobile_phone'
        ]

        read_only_fields = ['id', 'user']

    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)