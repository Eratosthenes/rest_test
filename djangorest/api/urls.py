from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BuildingCreateView, BuildingDetailsView, UnitCreateView, UnitDetailsView

urlpatterns = {
    url(r'^buildings/$', BuildingCreateView.as_view(), name="building_create"),
    url(r'^buildings/(?P<pk>[0-9]+)/$',
        BuildingDetailsView.as_view(), name="building_details"),
    url(r'^units/$', UnitCreateView.as_view(), name="unit_create"),
    url(r'^units/(?P<pk>[0-9]+)/$',
        UnitDetailsView.as_view(), name="unit_details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
