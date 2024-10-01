from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        
        non_allowed_fields = set(request.data.keys()) - set(['first_name', 'last_name'])
        if non_allowed_fields:
            return Response(
                {"detail": f"Changing these fields is not allowed: {', '.join(non_allowed_fields)}. You can only update 'first_name' and 'last_name'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
