from abc import ABC


class IClientAdapter(ABC):
    @staticmethod
    def client_to_domain():
        raise NotImplementedError

    @staticmethod
    def domain_to_client():
        raise NotImplementedError
