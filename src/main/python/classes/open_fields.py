from classes.dangerous_structure import DangerousStructure
from typing import List
from classes.monster import Monster

class OpenFields(DangerousStructure):

    def __init__(self, name, type, width, height, dificulty,monsters:List[Monster], structures, city):
        super().__init__(name, type, width, height, dificulty)
        self._monsters = monsters
        self._structures = structures
        self._city = city



    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def structures(self):
        return self._structures

    @structures.setter
    def structures(self, value):
        self._structures = value

    @property
    def monsters(self):
        return self._monsters

    @monsters.setter
    def monsters(self, value):
        self._monsters = value



    def to_dict(self):
        return {
            'name': self._name,
            'type': self._type,
            'width': self._width,
            'height': self._height,
            'dificulty': self._dificulty,
            'monsters': [monster.to_dict() for monster in self._monsters],
            'structures': [structure.to_dict() for structure in self._structures],
            'city': self._city
        }