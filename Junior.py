# <========== import ==========>

from __future__ import annotations
from typing import Final

from Lvl import Lvl

# <========== class ==========>

class Junior:
    
    # <----- init ----->
    
    def __init__(self: Junior, owner: str) -> None:
        self.__owner: Final[str] = owner
        self.__name: str = "Junior"
        self.__exp: Lvl = Lvl(0)
        
    # <----- getter ----->

    @property
    def id(self: Junior) -> str: return self.__id
    
    @property
    def name(self: Junior) -> str: return self.__name
    
    # <----- setter ----->
    
    @name.setter
    def name(self: Junior, new_name: str): self.__name = new_name 
    
    # <----- comparateur ----->
    
    def __eq__(self: Junior, other: Junior | int) -> bool:
        if type(other) == Junior: return self.__exp == other.__exp
        return self.__exp == other
    
    def __ne__(self: Junior, other: Junior | int) -> bool:
        if type(other) == Junior: return self.__exp != other.__exp
        return self.__exp != other
    
    def __lt__(self: Junior, other: Junior | int) -> bool:
        if type(other) == Junior: return self.__exp < other.__exp
        return self.__exp < other
    
    def __le__(self: Junior, other: Junior | int) -> bool:
        if type(other) == Junior: return self.__exp <= other.__exp
        return self.__exp <= other
    
    def __gt__(self: Junior, other: Junior | int) -> bool:
        if type(other) == Junior: return self.__exp > other.__exp
        return self.__exp > other
    
    def __ge__(self: Junior, other: Junior | int) -> bool:
        if type(other) == Junior: return self.__exp >= other.__exp
        return self.__exp >= other