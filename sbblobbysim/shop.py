import random
from dataclasses import dataclass

from sbbbattlesim.characters import registry as character_registry
from sbbbattlesim.spells import registry as spell_registry


CHARACTER_POOL_PER_LEVEL = {
    2: 15,
    3: 15,
    4: 15,
    5: 15,
    6: 10,
}

SHOP_CHAR_PER_ROUND = {
    1: 3,
    2: 3,
    3: 4,
    4: 4,
    5: 4,
    6: 4,
    7: 5,
}


@dataclass
class ShopOffer:
    shop: 'LobbyShop'
    characters: list
    spells: list


class LobbyShop():
    def __init__(self):
        self.character_pool = {
            char_id: CHARACTER_POOL_PER_LEVEL[char.level] for char_id, char in character_registry
        }
        self.round = 1

    def generate_offers(self, spells, level) -> ShopOffer:
        char_options = character_registry.filter(_lambda=lambda c: c.level <= level)
        spell_options = spell_registry.filter(_lambda=lambda c: c.level <= level)

        offered = ShopOffer(
            shop=self,
            characters=[random.choice(char_options) for _ in range(SHOP_CHAR_PER_ROUND[self.round])],
            spells=[random.choice(spell_options) for _ in range(spells)]
        )

        return offered
