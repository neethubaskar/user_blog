from rest_framework.pagination import PageNumberPagination


class BlogPostListPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
