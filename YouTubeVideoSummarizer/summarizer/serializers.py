from rest_framework import serializers

from summarizer.models import Summary

class SummaryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = "__all__"
        read_only_fields = ["uuid", ]

class SummaryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ["title", "summary", "content_type"]

class SummaryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = "__all__"
        read_only_fields = ["uuid", ]
