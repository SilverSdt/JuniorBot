# <========== import ==========>

from __future__ import annotations
from json import dumps, load

from Lvl import Lvl

# <========== class ==========>

class Junior:
    
    # <----- init ----->
    
    def __init__(self: Junior, owner: str = "unknown", name:str = "Junior", exp: Lvl = Lvl(0)) -> None:
        self.__owner: str = owner
        self.__name: str = name
        self.__exp: Lvl = exp
        
    # <----- getter ----->

    @property
    def owner(self: Junior) -> str: return self.__owner
    
    @property
    def name(self: Junior) -> str: return self.__name
    
    @property
    def exp(self: Junior) -> int: return self.__exp.exp
    
    @property
    def lvl(self: Junior) -> int: return self.__exp.lvl
    # <----- setter ----->
    
    @owner.setter
    def owner(self: Junior, new_owner: str) -> None: self.__owner = new_owner
    
    @name.setter
    def name(self: Junior, new_name: str) -> None: self.__name = new_name 
    
    @exp.setter
    def exp(self: Junior, new_exp_value: Lvl | int) -> None:
        if isinstance(new_exp_value, Lvl): self.__exp = new_exp_value
        else: self.__exp = Lvl(new_exp_value) 
    
    # <----- comparateur ----->
    
    def __eq__(self: Junior, other: Junior | int) -> bool:
        if isinstance(other,Junior): return self.__exp == other.__exp
        return self.__exp == other
    
    def __ne__(self: Junior, other: Junior | int) -> bool:
        if isinstance(other,Junior): return self.__exp != other.__exp
        return self.__exp != other
    
    def __lt__(self: Junior, other: Junior | int) -> bool:
        if isinstance(other,Junior): return self.__exp < other.__exp
        return self.__exp < other
    
    def __le__(self: Junior, other: Junior | int) -> bool:
        if isinstance(other,Junior): return self.__exp <= other.__exp
        return self.__exp <= other
    
    def __gt__(self: Junior, other: Junior | int) -> bool:
        if isinstance(other,Junior): return self.__exp > other.__exp
        return self.__exp > other
    
    def __ge__(self: Junior, other: Junior | int) -> bool:
        if isinstance(other,Junior): return self.__exp >= other.__exp
        return self.__exp >= other
    
    # <----- operator ----->
    
    def __iadd__(self: Junior, x: int) -> Junior: 
        if self.__exp.exp + x < 0: return Junior(self.__owner, self.__name, 0)
        return Junior(self.__owner, self.__name, self.__exp + x)
    
    def __add__(self: Junior, x: int) -> Junior:
        if self.__exp.exp + x < 0: return Junior(self.__owner, self.__name, 0)
        return Junior(self.__owner, self.__name, self.__exp + x)
    
    def __isub__(self: Junior, x: int) -> Junior:
        if self.__exp.exp - x < 0: return Junior(self.__owner, self.__name, 0)
        return Junior(self.__owner, self.__name, self.__exp - x)
    
    def __sub__(self: Junior, x: int) -> Junior:
        if self.__exp.exp - x < 0: return Junior(self.__owner, self.__name, 0)
        return Junior(self.__owner, self.__name, self.__exp - x)
    
    # <----- str ----->
    
    def __str__(self: Junior) -> str: return f"{self.__name} est {self.__exp}"
    
    # <----- save_junior ----->
    
    def save_junior(self: Junior) -> None:
        profil: dict = {
            "owner": self.__owner,
            "name": self.__name,
            "exp": self.__exp.exp
        }
        
        with open(f'Junior_Data/{self.__owner}.json', 'w+') as file:
            file.write(dumps(profil))
            
    # <----- load_junior ----->
    
    @classmethod
    def load_junior(self: Junior, owner: str) -> Junior:
        try:
            with open(f'Junior_Data/{owner}.json', 'r') as file:
                data = load(file)
                return Junior(data["owner"], data["name"], Lvl(data["exp"]))
        except:
            new_junior: Junior = Junior(owner)
            new_junior.save_junior()
            
