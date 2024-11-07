from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView
)

from rest_framework.parsers import FormParser

from summarizer.models import Summary
from summarizer.serializers import (
    SummaryCreateSerializer,
    SummaryListSerializer,
    SummaryDetailSerializer
)


class SummaryCreateView(CreateAPIView):
    parser_classes = (FormParser,)
    queryset = Summary.objects.all()
    serializer_class = SummaryCreateSerializer


class SummaryListView(ListAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummaryListSerializer


class SummaryDetailView(RetrieveAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummaryDetailSerializer
    lookup_field = "uuid"


class SumarryDeleteView(DestroyAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummaryDetailSerializer
    lookup_field = "uuid"


class SumarryDeleteView(UpdateAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummaryDetailSerializer
    lookup_field = "uuid"