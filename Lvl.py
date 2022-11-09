# <========== import ==========>

from __future__ import annotations
from math import sqrt

# <========== class ==========>

class Lvl:
    
    # <----- init ----->
    
    def __init__(self: Lvl, exp: int) -> None:
        self.__exp: int = exp
        
    # <----- getter ----->
    
    @property
    def exp(self: Lvl) -> int: return self.__exp
    
    @property
    def lvl(self: Lvl) -> int:
        return (int((sqrt(self.exp) * 0.57 * 137 + 3 * self.exp * 2.85) / 1000)) + 1
    # <----- setter ----->
    
    @exp.setter
    def exp(self: Lvl, new_value: int) -> None: self.__exp = new_value
    
    # <----- operateur ----->
    
    def __iadd__(self: Lvl, x: int) -> Lvl: return Lvl(self.__exp + x)
    
    def __add__(self: Lvl, x: int) -> Lvl: return Lvl(self.__exp + x)
    
    def __isub__(self: Lvl, x: int) -> Lvl: return Lvl(self.__exp - x)
    
    def __sub__(self: Lvl, x: int) -> Lvl: return Lvl(self.__exp - x)
    
    # <-----comparateur ----->
    
    def __eq__(self: Lvl, other: Lvl | int) -> bool:
        if type(other) == Lvl: return self.__exp == other
        self.__exp == other.__exp
        
    def __ne__(self: Lvl, other: Lvl | int) -> bool:
        if type(other) == Lvl: return self.__exp != other
        self.__exp != other.__exp
        
    def __lt__(self: Lvl, other: Lvl | int) -> bool:
        if type(other) == Lvl: return self.__exp < other
        self.__exp < other.__exp
        
    def __le__(self: Lvl, other: Lvl | int) -> bool:
        if type(other) == Lvl: return self.__exp <= other
        self.__exp <= other.__exp
        
    def __gt__(self: Lvl, other: Lvl | int) -> bool:
        if type(other) == Lvl: return self.__exp > other
        self.__exp > other.__exp
        
    def __ge__(self: Lvl, other: Lvl | int) -> bool:
        if type(other) == Lvl: return self.__exp >= other
        self.__exp >= other.__exp
        
    # <----- str ----->
    
    def __str__(self) -> str: return f"lvl {self.lvl} avec {self.__exp} exp."