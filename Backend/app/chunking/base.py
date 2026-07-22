from abc import ABC, abstractmethod
from typing import List

class BaseSplit(ABC):

    def split(self,text:str)->List[str]:
        pass
    