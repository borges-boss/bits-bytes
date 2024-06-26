import time
from content.inventory.views.inventory_view import InventoryView
from content.journal.views.journal_view import JournalView
from constants.constants import ITEM_RARITY_COMMON, ITEM_RARITY_EPIC, ITEM_RARITY_LEGENDARY, ITEM_RARITY_RARE
from content.player.controllers.player_controller import PlayerController
from services.data_store import DataStore


class ShopModel:


    def __init__(self):
        self.datastore = DataStore()

    def get_shops_by_current_player_city(self):
        return self.datastore .find_shops_by_city(PlayerController.get_player().city)

    def get_items_for_sale(self):
        return self.get_shops_by_current_player_city()[0].items_for_sale
    
    def evaluate_item_price(self, item):
        base_price = 10 

        if item.rarity == ITEM_RARITY_COMMON:
            price_multiplier = 1
        elif item.rarity == ITEM_RARITY_RARE:
            price_multiplier = 2
        elif item.rarity == ITEM_RARITY_EPIC:
            price_multiplier = 3
        elif item.rarity == ITEM_RARITY_LEGENDARY:
            price_multiplier = 5
        else:
            print(f"A raridade do item e desconhecida: {item.rarity} impossivel de avaliar o preco")
            return None

        price_multiplier += len(item.enchantments) * 0.5

        return base_price * price_multiplier

    def buy_item(self, item, player):
        item_price = self.evaluate_item_price(item)

        if player.wallet.coins >= item_price:
            added_to_inventory = player.inventory.add_item(item)

            if added_to_inventory:
                player.wallet.subtract_coins(item_price)
                print(f"Voce comprou {item.name} por {item_price}")
                time.sleep(3)

        else:
            print("\nVoce nao coins suficientes para comprar esse item.")
            time.sleep(3)
        
        return player

    def sell_item(self, item, player):
        # O preço de venda é 50% do preço de compra
        selling_price = self.evaluate_item_price(item) * 0.5
        removed_from_inventory = player.inventory.remove_item(item)

        if removed_from_inventory:
            player.wallet.add_coins(selling_price)
            print(f"\nVoce vendeu {item.name} por {selling_price} coins.")
        else:
            print("\nFalha ao vender o item. O item nao esta no seu inventario.")

     
        time.sleep(3)

        return player

    def open_inventory(self, player):
        view = InventoryView(player)
        view.init_view()

    def open_journal(self):
        view = JournalView()
        view.init_view()