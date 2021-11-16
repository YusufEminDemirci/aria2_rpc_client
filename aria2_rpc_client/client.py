from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import List

from .connection import Connection
from .types import GID
from .types import GlobalStat
from .types import Version


class Client(ABC):
    def __init__(self, connection: Connection) -> None:
        self._connection = connection
        self.server = connection.make_connection()

    def call(self, method: str, *params: Any) -> Any:
        response = self.server.__getattr__(method)(self._connection.secret, *params)
        return response

    @abstractmethod
    def add_uri(self, urls: List[str], *params: Any) -> GID:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.addUri"""

        response = self.call("aria2.addUri", urls, *params)
        return GID(response)

    @abstractmethod
    def list_methods(self) -> List[str]:
        """https://aria2.github.io/manual/en/html/aria2c.html#system.listMethods"""

        response = self.call("system.listMethods")
        return list(response)

    @abstractmethod
    def get_global_stat(self) -> GlobalStat:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getGlobalStat"""

        response = self.call("aria2.getGlobalStat")
        global_stat = GlobalStat(**response)
        return global_stat

    @abstractmethod
    def get_version(self) -> Version:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getVersion"""

        response = self.call("aria2.getVersion")
        version = Version(**response)
        return version


class DefaultClient(Client):
    def add_uri(self, urls: List[str], *params: Any) -> GID:
        result = super().add_uri(urls, *params)
        return result

    def list_methods(self) -> List[str]:
        response = super().list_methods()
        return response

    def get_global_stat(self) -> GlobalStat:
        response = super().get_global_stat()
        return response

    def get_version(self) -> Version:
        response = super().get_version()
        return response