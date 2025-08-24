import random
from .monsters import create_nightmare, Monster

class Room:
    def __init__(self, number: int, fear_prompt: str):
        self.number = number
        self.monster = create_nightmare(fear_prompt)

    def encounter(self, player) -> None:
        print(f"You enter room {self.number}. {self.monster.description}")
        fear = self.monster.scare()
        player.apply_fear(fear)
        player.take_damage(fear // 2)
        print(
            f"The {self.monster.name} lashes out! Fear +{fear}, Health -{fear // 2}."
        )
