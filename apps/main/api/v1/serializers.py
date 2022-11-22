from rest_framework import serializers


class MarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = '__all__'

    def set_model(self, model):
        self.Meta.model = model