from django.contrib import admin
from django.urls import path, include
# CHECK THIS IMPORT LINE:
from accounts.views import home, about, team, events, management_sapiens, select, madteam, contact, auction, product_remix, thinksink, brandplay, madmoments, treasuretrack, auction_register, brandplay_register, madmoments_register, thinksink_register, treasuretrack_register, productremix_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('events/', events, name='events'),

    # CHECK THIS LINE CAREFULLY:
    path('management-sapiens/', management_sapiens, name='management_sapiens'),
    path('select/', select, name='select'),
    path('madteam/', madteam, name='madteam'),
    path('contact/', contact, name='contact'),
    path('auction/', auction, name='auction'),
    path('product-remix/', product_remix, name='product_remix'),
    path('thinksink/', thinksink, name='thinksink'),
    path('brandplay/', brandplay, name='brandplay'),
    path('madmoments/', madmoments, name='madmoments'),
    path('treasuretrack/', treasuretrack, name='treasuretrack'),
    path('auction/register/', auction_register, name='auction_register'),
    path('brandplay/register/', brandplay_register, name='brandplay_register'),
    path('madmoments/register/', madmoments_register, name='madmoments_register'),
    path('thinksink/register/', thinksink_register, name='thinksink_register'),
    path('treasuretrack/register/', treasuretrack_register, name='treasuretrack_register'),
    path('product-remix/register/', productremix_register, name='productremix_register'),
]