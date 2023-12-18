import json

from domain.models.value_objects import QueryFilters


def get_query_filters(filters: str | None = "{}"):
    filters_dict = {
        "filters": json.loads(filters)
    }
    return QueryFilters.model_validate(filters_dict)
