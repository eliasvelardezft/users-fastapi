from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel

from .value_objects import Name, Id, Description, ComparisonFieldFilter, RangeFieldFilter


@dataclass(kw_only=True)
class Permission:
    id: Id | None = None
    name: Name
    description: Description

    created_date: datetime | None = None
    updated_date: datetime | None = None
    deleted_date: datetime | None = None
