from constants.constants import ITEM_TYPE_DAMAGE
from constants.constants import  ITEM_TYPE_CONSUMABLE
from constants.constants import ITEM_TYPE_WEARABLE

class Item:

    def __init__(self,name,type,rarity,weight,enchantments):
        self._name = name
        self._type = type
        self._rarity = rarity
        self._weight = weight
        self._enchantments = enchantments

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, value):
        self._rarity = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def enchantments(self):
        return self._enchantments

    @enchantments.setter
    def enchantments(self, value):
        self._enchantments = value


    def apply_enchantments(self):
        print("apply")

    def is_equippable(self):
        return self.type == ITEM_TYPE_DAMAGE or self.type == ITEM_TYPE_WEARABLE
    
    def is_consumable(self):
        return self.type == ITEM_TYPE_CONSUMABLE

