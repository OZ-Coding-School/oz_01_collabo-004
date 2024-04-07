from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response


class ProductReviewPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20


class ProductByCategoryPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50
