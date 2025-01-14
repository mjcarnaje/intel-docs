from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health, name='health'),
    path('documents', views.get_docs, name='get_docs'),
    path('documents/upload', views.upload_doc, name='upload_doc'),
    path('documents/<int:doc_id>', views.get_doc, name='get_doc'),
    path('documents/<int:doc_id>/raw', views.get_doc_raw, name='get_doc_raw'),
    path('documents/<int:doc_id>/markdown', views.get_doc_markdown, name='get_doc_markdown'),
    path('documents/<int:doc_id>/chunks', views.get_doc_chunks, name='get_doc_chunks'),
    path('documents/<int:doc_id>/delete', views.delete_doc, name='delete_doc'),
    path('documents/<int:doc_id>/update', views.update_doc, name='update_doc'),
    path('documents/search', views.search_docs, name='search_docs'),
    path('documents/chat', views.chat_with_docs, name='chat_with_docs'),
    path('documents/delete_all', views.delete_all_docs, name='delete_all_docs'),
    path('documents/<str:doc_id>/retry/', views.retry_doc_processing, name='retry_doc_processing'),
    path('documents/<str:doc_id>/chat', views.chat_with_single_doc, name='chat_with_single_doc'),
]
