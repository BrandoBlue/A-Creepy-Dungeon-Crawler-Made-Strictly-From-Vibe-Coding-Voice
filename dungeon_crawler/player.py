from dataclasses import dataclass

@dataclass
class Player:
    name: str
    health: int = 100
    fear: int = 0

    def is_alive(self) -> bool:
        return self.health > 0

    def apply_fear(self, amount: int) -> None:
        self.fear = min(100, self.fear + amount)

    def take_damage(self, amount: int) -> None:
        self.health = max(0, self.health - amount)
