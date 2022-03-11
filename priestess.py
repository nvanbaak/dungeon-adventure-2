# name  : Shoby Gnanasekaran
# net id: shoby

from dungeonchar import DungeonCharacter
from healable import Healable
from hero import Hero
from dungeonchar_db_access import DungeonCharDb

class Priestess(Hero, Healable):
    def __init__(self, name = "name", model = None):
        super().__init__(name = name, model = model)
        super(DungeonCharacter, self).__init__()
        self.__update_values_from_db()

    def __update_values_from_db(self):
        db = DungeonCharDb()  # connects and accesses monster_stats table of dungeondb
        self.hp_total = db.get_data_hero("Priestess", "hp")
        self.hp = self.hp_total
        self.attack_speed = db.get_data_hero("Priestess", "attack_speed")
        self.hit_chance = db.get_data_hero("Priestess", "hit_chance")
        self.damage_min = db.get_data_hero("Priestess", "damage_min")
        self.damage_max = db.get_data_hero("Priestess", "damage_max")
        self.chance_to_block = db.get_data_hero("Priestess", "chance_to_block")
        self.chance_to_heal = db.get_healable_stats("Priestess","chance_to_heal")
        self.max_heal_point = db.get_healable_stats("Priestess","max_heal_point")
        self.min_heal_point = db.get_healable_stats("Priestess","min_heal_point")


    def take_damage(self, dmg, source):
        """ after taking damage, if the monster is not dead, it tries to heal itself"""
        hp_before_attack = self.hp
        super().take_damage(dmg, source)
        if self._is_alive and hp_before_attack > self.hp:
            heal_message = self.heal_itself()
            self._DungeonCharacter__model.announce(f"{self._DungeonCharacter__name}: {heal_message}")



