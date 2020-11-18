from flask_restplus import Resource
from flask_sqlalchemy import BaseQuery


def get_pagination_request_params():
    """
    Pagination request params for a @doc decorator in API view.
    """
    return {
        "page": "Page",
        "per_page": "Items per page",
    }


class APIView(Resource):
    page = 0
    per_page = 0
    total_items = 0

    def paginate_queryset(self, queryset):
        """
        Returns paginated queryset.
        """
        assert isinstance(queryset, BaseQuery), "Data must be a BaseQuery instance."
        paginated_queryset = queryset.paginate()

        self.page = paginated_queryset.page
        self.per_page = paginated_queryset.per_page
        self.total_items = paginated_queryset.total

        return paginated_queryset.items

    def get_paginated_response(self, queryset):
        """
        Returns paginated response.
        `paginate_queryset` method must be called first.
        """
        return {
            "page": self.page,
            "pages_count": max(1, self.total_items // self.per_page),
            "per_page": self.per_page,
            "count": len(queryset),
            "results": queryset,
        }
