class Entity:

    def __init__(self,name,health,damage:float,defence,stamina,race,type):
        self._name = name
        self._helth = health
        self._damage = damage
        self._defence = defence
        self._stamina = stamina
        self._race = race
        self._type = type



    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def health(self):
        return self._helth

    @health.setter
    def health(self, value):
        self._helth = value

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, value):
        self._defence = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        self._stamina = value

    @property
    def race(self):
        return self._race

    @race.setter
    def race(self, value):
        self._race = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

