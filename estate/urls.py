from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('properties', views.properties, name="properties"),
    path('agent', views.agent, name="agent"),
    path('services', views.services, name="services"),
    path('blog', views.blog, name='blog'),
    path('message', views.send_message, name="message"),
    path('property/<int:prop_id>', views.property, name="property"),
    path('review/<int:p_id>', views.review, name="review"),
    path('blogs/<int:blog_id>', views.blog_post, name="blogs"),
    path('properties_category/<str:category>', views.cat_search, name="search_cat"),
    path('properties_agent/<int:agent>', views.agent_search, name="search_agent"),
    path('properties_location/<str:location>', views.property_search, name="search_prop"),
    path('comment/<int:blog_id>', views.comments, name='comment'),
]