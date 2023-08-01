"""
URL configuration for medlab_help project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import test_views, panel_views, organ_views, alternate_name_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tests/', test_views.TestList),
    path('tests/<str:id>', test_views.TestDetail),

    path('panels/', panel_views.PanelList),
    path('panels/<str:id>', panel_views.PanelDetail),

    path('organs/', organ_views.OrganList),
    path('organs/<str:id>', organ_views.OrganDetail),

    path('organs/<str:id>/tests', organ_views.TestDetailByOrganId),

    path('alternatenames/', alternate_name_views.AlternateNameList),
    path('alternatenames/<str:id>', alternate_name_views.AlternateNameDetail),

]

urlpatterns = format_suffix_patterns(urlpatterns)