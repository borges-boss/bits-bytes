from content.tavern.models.tavern_model import TavernModel

class TavernController:

    def __init__(self,city_name):
        self.city_name = city_name
        self.model = TavernModel()

    def get_taverns_by_city(self):
        return self.model.get_taverns_by_city(self.city_name)

    

    def explore(self):
        self.model.explore()

    def open_inventory(self, player):
        self.model.open_inventory(player)

    def open_journal(self):
        self.model.open_journal()

    def leave(self):
        self.model.leave()

    
