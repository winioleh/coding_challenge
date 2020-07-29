"""wingtel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from wingtel.plans.views import PlanViewSet
from wingtel.purchases.views import PurchaseViewSet
from wingtel.core.views import TCViewSet, CustomUserViewSet
from wingtel.agg_metrics.views import usage_metrics
from wingtel.usage.views import UsageRecordViewSet
from wingtel.subscriptions.views import SubscriptionViewSet
from wingtel.usage.views import get_subscriptions_with_exceeded_price_limit
from wingtel.agg_metrics.views import AggUsageViewSet




router = routers.DefaultRouter()

# router.register(r'att_subscriptions', ATTSubscriptionViewSet)
router.register(r'plans', PlanViewSet, base_name="plans")
router.register(r'providers', TCViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'usages', UsageRecordViewSet)
router.register(r'agg_metrics', AggUsageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include((router.urls, 'api'), namespace='api')),
    url(r'^api/usage_metrics', usage_metrics,name='usage_metrics'),
    url(r'^api/subscription_exceeded_price_limit', get_subscriptions_with_exceeded_price_limit,
        name='subscription_exceeded_price_limit'),
]
