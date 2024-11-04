from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Employee
from .serializers import EmployeeSerializer
from .filters import EmployeeFilter

class EmployeePagination(PageNumberPagination):
    page_size = 10  # Limit results per page to 10
    page_size_query_param = 'page_size'  # Allow clients to set the page size
    max_page_size = 100  # Limit the maximum page size to avoid heavy queries

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def GetAllEmployees(request):
    queryset = Employee.objects.all()
    filterset = EmployeeFilter(request.GET, queryset=queryset)
    
    if filterset.is_valid():
        employees = filterset.qs
    else:
        employees = queryset

    paginator = EmployeePagination()
    paginated_employees = paginator.paginate_queryset(employees, request)
    
    serializer = EmployeeSerializer(paginated_employees, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getSingleEmployee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee)
        return Response({
            'status': status.HTTP_200_OK,
            'payload': serializer.data
        }, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response({
            'status': status.HTTP_404_NOT_FOUND,
            'message': 'Employee not found'
        }, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_Employee(request):
    serializer = EmployeeSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(
            {'status': status.HTTP_400_BAD_REQUEST, 'errors': serializer.errors, 'message': 'Something went wrong'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    
    serializer.save()
    return Response({
        'status': status.HTTP_201_CREATED,
        'payload': serializer.data,
        'message': 'Your data is saved'
    }, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_Employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {'status': status.HTTP_400_BAD_REQUEST, 'errors': serializer.errors, 'message': 'Something went wrong'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'payload': serializer.data,
            'message': 'Employee data updated successfully'
        }, status=status.HTTP_200_OK)
    
    except Employee.DoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Invalid ID'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_Employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response({'status': status.HTTP_204_NO_CONTENT, 'message': 'Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    except Employee.DoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Invalid ID'}, status=status.HTTP_404_NOT_FOUND)