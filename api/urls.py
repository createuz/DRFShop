# from .views import ProductAPIView, AddToShoppingCardAPIView, UserShoppingCardAPIView, \
#     DeleteFromCardAPIView, ProductListCreateView, ProductUpdateDeleteView, ProductDetailView, CommentCreateView, \
#     SendMail
#
# urlpatterns = [
#     path('api/', ProductAPIView.as_view(), name='api'),
#     path('add_product/', ProductListCreateView.as_view(), name='product-list-create'),
#     path('product-update-delete/<int:pk>', ProductUpdateDeleteView.as_view(), name='products_update_delete'),
#     path('product-detail/<int:pk>', ProductDetailView.as_view(), name='products_detail'),
#     path('product/comment/<int:pk>', CommentCreateView.as_view(), name='comment-create'),
#     path('product/on_sale/', ProductListCreateView.as_view(), name='on-sale-product-list'),
#     path('add-to-card', AddToShoppingCardAPIView.as_view(), name='shopping_card'),
#     path('send-email', SendMail.as_view(), name='send_email'),
#     path('user-card', UserShoppingCardAPIView.as_view(), name='user_card'),
#     path('user-card-delete/<int:pk>', DeleteFromCardAPIView.as_view(), name='user_card_delete'),
#
# ]
# from api.views import ProductViewSet, CategoryViewSet, CommentViewSet
#
# product_list = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
#
# product_detail = ProductViewSet.as_view(
#     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
#
# comment_list = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
#
# comment_detail = CommentViewSet.as_view(
#     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
#
# category_list = CategoryViewSet.as_view({'get': 'list', 'post': 'create'})
#
# category_detail = CategoryViewSet.as_view(
#     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
# from django.urls import path, include
# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
# router.register(r'comments', CommentViewSet, basename='comment')
# router.register(r'categories', CategoryViewSet, basename='category')
#
#
#
# urlpatterns = [
#     path('products/', product_list, name='product-list'),
#     path('products/<int:pk>/', product_detail, name='product-detail'),
#     path('categories/', category_list, name='category-list'),
#     path('categories/<int:pk>/', category_detail, name='category-detail'),
#     path('products/comment/<int:pk>', product_detail, name='product-comment'),
#     path('comments/', comment_list, name='comment-list'),
#     path('comments/<int:pk>/', comment_detail, name='comment-detail'),
#     path('', include(router.urls)),
#
# ]

#
# from api.views import ProductViewSet, CategoryViewSet, CommentViewSet
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'products', ProductViewSet, basename='product')
# router.register(r'comments', CommentViewSet, basename='comment')
# router.register(r'categories', CategoryViewSet, basename='category')
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProductViewSet, SendMail, AddToShoppingCardAPIView,
    UserShoppingCardAPIView, DeleteFromCardAPIView, UserShoppingLikeAPIView, DeleteFromLikeAPIView,
    AddToShoppingLikeAPIView, SearchAPIView
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [

    # Products
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product-detail'),

    # Categories
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category-detail'),

    # Send Email
    path('send-email', SendMail.as_view(), name='send_email'),
    path('send-email/', SendMail.as_view(), name='send_email'),
    path('add-to-card', AddToShoppingCardAPIView.as_view(), name='shopping_card'),
    path('user-card', UserShoppingCardAPIView.as_view(), name='user_card'),
    path('user-card-delete/<int:pk>', DeleteFromCardAPIView.as_view(), name='user_card_delete'),
    path('add-to-like', AddToShoppingLikeAPIView.as_view(), name='shopping_like'),
    path('user-like', UserShoppingLikeAPIView.as_view(), name='user_like'),
    path('user-like-delete/<int:pk>', DeleteFromLikeAPIView.as_view(), name='user_like_delete'),
    path('', include(router.urls)),

    # Search
    path('search/', SearchAPIView.as_view(), name='your-model-list'),
]
'''
    GET /products/: Get a list of products.
    POST /products/: Add new product.
    PUT /products/<pk>/: Update a specific product.
    DELETE /products/<pk>/: Delete a specific product.
    GET /products/<pk>/: Get details of a particular product.
    GET /categories/: Get a list of categories.
    POST /categories/: Add new category.
    PUT /categories/<pk>/: Update a specific category.
    DELETE /categories/<pk>/: Delete a specific category.
'''