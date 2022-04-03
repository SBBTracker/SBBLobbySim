import random
from collections import OrderedDict

from sbbbattlesim.heroes import registry as hero_registry

from sbblobbysim.shop import ShopOffer, LobbyShop


class LobbyPlayer:
    def __init__(self):
        self.health = 0
        self.gold = 0
        self.level = 2
        self.sub_level = 0
        self.hand = []
        self.characters = OrderedDict({i+1: None for i in range(7)})

    @property
    def alive(self):
        return self.health > 0

    def select_hero(self, options):
        #TODO make this better I guess?
        self.hero = random.choice(options)
        self.health = getattr(hero_registry[self.hero], 'health', 40)

    def level_up(self):
        if self.sub_level + 1 == 3:
            self.level += 1
            self.sub_level = 0
        else:
            self.sub_level += 1

    def use_shop(self, shop: LobbyShop):
        while self.gold > 0:
            #TODO purchase things
            offers = shop.generate_offers(spells=1, level=self.level)
            char, price = offers.purchase_character(random.randint(0, len(offers.characters)))

            open_board_slot = next((i for i, char in self.characters.keys() if char is None), False)
            if open_board_slot:
                self.characters[open_board_slot] = char
            elif

    def