from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.db.models import Q

from blog.v1.serializers import BlogPostListSerializer
from blog.models import BlogPost
from blog.v1.pagination import BlogPostListPagination


class BlogPostListView(generics.ListAPIView):
    """
    Listing view for published blogs.
    """
    model = BlogPost
    serializer_class = BlogPostListSerializer
    pagination_class = BlogPostListPagination
    response_data = dict()

    def get_queryset(self):
        """
        filters the queryset based on active 
        status and user if the user is logged in.
        :return: queryset
        """
        filter_condition = Q(is_active=True)
        if self.request.user:
            filter_condition &= Q(author=self.request.user)
        queryset = self.model.objects.filter(filter_condition)
        return queryset
    
    def list(self, request, *args, **kwargs):
        try:
            resonse = super().list(request, *args, **kwargs)
            data = resonse.data
            self.response_data['status'] = 'success'
            self.response_data['data'] = data
            return Response(self.response_data, status=status.HTTP_200_OK)
        except Exception as e:
            self.response_data['status'] = 'failed'
            self.response_data['error'] = str(e)
            return Response(self.response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

