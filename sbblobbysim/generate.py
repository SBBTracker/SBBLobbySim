import random

from sbbbattlesim.characters import registry as character_registry
from sbbbattlesim.spells import registry as spell_registry
from sbbbattlesim.treasures import registry as treasure_registry
from sbbbattlesim.heroes import registry as hero_registry


def hero_selection(hero_options=4):
    hero_ids = list(hero_registry.heroes.keys())
    random.shuffle(hero_ids)
    return [hero_ids[i:i + hero_options] for i in range(0, len(hero_ids), hero_options)]


def shop(chars, spells, level):
    char_ids = character_registry.filter()