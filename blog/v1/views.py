from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q

from blog.v1.serializers import BlogPostListSerializer, BlogPostSerializer
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
        :param: q: serach value if present.
        :return: queryset
        """
        query_params = self.request.query_params
        search_value = query_params.get('q')
        
        filter_condition = Q(is_active=True)
        if self.request.user.id:
            filter_condition &= Q(author=self.request.user)
        if search_value:
            filter_condition &= (
                Q(title__icontains=search_value) | 
                Q(content__icontains=search_value)
                )

        queryset = self.model.objects.filter(filter_condition)
        return queryset
    
    def list(self, request, *args, **kwargs):
        try:
            resonse = super().list(request, *args, **kwargs)
            self.response_data = resonse.data
            self.response_data['status'] = 'Success'
            return Response(self.response_data, status=status.HTTP_200_OK)
        except Exception as e:
            self.response_data = {
                    'status': 'Failed',
                    'error': str(e)
                }
            return Response(self.response_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows CRUD operations on BlogPosts.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]
    response_data = dict()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                self.response_data = {
                    'status': 'Success',
                    'message': 'Blog has been created successfully.'
                }
                return Response(self.response_data, status=status.HTTP_201_CREATED)
            self.response_data = {
                    'status': 'Failed',
                    'error': serializer.errors
                }
            return Response(self.response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            self.response_data = {
                    'status': 'Failed',
                    'error': str(e)
                }
            return Response(self.response_data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                self.response_data = {
                    'status': 'Success',
                    'message': 'Blog has been updated successfully.'
                }
                return Response(self.response_data, status=status.HTTP_200_OK)
            self.response_data = {
                    'status': 'Failed',
                    'error': serializer.errors
                }
            return Response(self.response_data, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            self.response_data = {
                    'status': 'Failed',
                    'error': str(e)
                }
            return Response(self.response_data, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
            self.response_data = {
                    'status': 'Success',
                    'message': 'Blog has been deleted successfully.'
                }
            return Response(self.response_data, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            self.response_data = {
                    'status': 'Failed',
                    'error': str(e)
                }
            return Response(self.response_data, status=status.HTTP_400_BAD_REQUEST)
