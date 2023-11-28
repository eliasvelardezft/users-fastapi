from abc import ABC
from typing import Any

from domain.models.value_objects import Id


class IRepository(ABC):
    def get(self, id: Id):
        raise NotImplementedError
    
    def filter(self, filters: dict[str, Any]):
        raise NotImplementedError
    
    def create(self, entity: Any):
        raise NotImplementedError
    
    def update(self, entity: Any):
        raise NotImplementedError
    
    def delete(self, id: Id):
        raise NotImplementedError
