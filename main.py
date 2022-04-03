import random
from copy import deepcopy

from sbblobbysim.player import LobbyPlayer
from sbblobbysim import generate
from sbblobbysim.shop import LobbyShop


if __name__ == '__main__':

    shop = LobbyShop()
    players = set(LobbyPlayer() for _ in range(8))

    hero_options = generate.hero_selection()

    for player in players:
        player.select_hero(random.choice(hero_options))

    # while sum(player.alive for player in player) > 1:
    #
    #     shop_gen =
