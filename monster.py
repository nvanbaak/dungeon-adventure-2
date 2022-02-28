# name  : Shoby Gnanasekaran
# net id: shoby

from abc import ABC, abstractmethod
from dungeonchar import DungeonCharacter
from healable import Healable

class Monster(DungeonCharacter, Healable, ABC):
    """
    Abstract base class used for all monster. They attach the hero and heal itself after every time taking damage
    """

    def __init__(self, name, model, chance_to_heal = 0.0):
        super().__init__(name=name, model=model)
        super(DungeonCharacter, self).__init__(chance_to_heal)

    def combat(self, target):
        """
        Method for executing a full round of combat where this character attacks first
        """
        my_attacks = 0
        target_attacks = 0
        my_turn = True
        while my_attacks < self.attack_speed or target_attacks < target.attack_speed:
            # characters alternate attacking until one of them dies
            # or they both run out of attacks
            if my_turn:
                if my_attacks < self.attack_speed:
                    hp_before_attack = target.hp
                    self.attack_target(target)
                    if not target._is_alive:
                        break
                    if target.healable and target.hp < hp_before_attack:  # hero is healable and has been attacked
                        heal_message = target.heal_itself()
                        target._DungeonCharacter__model.announce(f"{target._DungeonCharacter__name}: {heal_message}")

                    my_turn = False
                    my_attacks += 1

            else:
                if target_attacks < target.attack_speed:
                    hp_before_attack = self.hp
                    target.attack_target(self)

                    if not self._is_alive:
                        break

                    if hp_before_attack > self.hp:
                        heal_message = self.heal_itself()
                        self._DungeonCharacter__model.announce(f"{self._DungeonCharacter__name}: {heal_message}")
                    my_turn = True
                    target_attacks += 1


    def attack_target(self, target):
        return super().attack_target(target)

    def take_damage(self, dmg, source):
        return super().take_damage(dmg, source)




