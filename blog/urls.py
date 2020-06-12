from django.urls import path
from . import views

urlpatterns = [
        path('',views.post_list, name='post_list'),
        path('post/<int:pk>/', views.post_detail, name='post_detail'),
        path('post/new', views.post_new, name='post_new'),
        path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
        path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
        path('post/<int:pk>/<int:pk1>', views.post_show, name='post_show'),
        path('post/<int:pk>/save/',views.post_save,name='post_save'),
        path('post/<int:pk>/scale/', views.post_scale, name='post_scale'),
        path('post/<int:pk>/thresholding/', views.post_thresholding, name='post_thresholding'),
        path('post/<int:pk>/contrast/', views.post_contrast, name='post_contrast'),
        path('post/<int:pk>/equalizer/', views.post_equalizer, name='post_equalizer'),
        path('post/<int:pk>/logaritmo/', views.post_logaritmo, name='post_logaritmo'),
        path('post/<int:pk>/raiz/', views.post_raiz, name='post_raiz'),
        path('post/<int:pk>/exponencial/', views.post_exponencial, name='post_exponencial'),
        path('post/<int:pk>/raizpower/', views.post_raizpower, name='post_raizpower'),
        path('post/<int:pk>/adicion/', views.post_adicion, name='post_adicion'),
        path('post/<int:pk>/sustraccion/', views.post_sustraccion, name='post_sustraccion'),
        path('post/<int:pk>/multiplicacion/', views.post_multiplicacion, name='post_multiplicacion'),
        path('post/<int:pk>/division/', views.post_division, name='post_division'),
        path('post/<int:pk>/blending/', views.post_blending, name='post_blending'),
        path('post/<int:pk>/not/', views.post_not, name='post_not'),
        path('post/<int:pk>/and/', views.post_and, name='post_and'),
        path('post/<int:pk>/or/', views.post_or, name='post_or'),
        path('post/<int:pk>/xor/', views.post_xor, name='post_xor'),
]
