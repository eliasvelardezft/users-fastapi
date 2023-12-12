from abc import ABC


class IPersistanceAdapter(ABC):
    @staticmethod
    def domain_to_persistance():
        raise NotImplementedError

    @staticmethod
    def persistance_to_domain():
        raise NotImplementedError
