from django.urls import path

from summarizer.views import (
    SummaryListView,
    SummaryCreateView,
    SumarryDeleteView,
    SummaryDetailView,
)

urlpatterns = [
    path("create/", SummaryCreateView.as_view(), name="summary-create"),
    path("list/", SummaryListView.as_view(), name="summary-create"),
    path("<str:uuid>/detail/", SummaryDetailView.as_view(), name="summary-create"),
    path("<str:uuid>/delete/", SumarryDeleteView.as_view(), name="summary-create")
]