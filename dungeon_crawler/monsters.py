from dataclasses import dataclass
import random

@dataclass
class Monster:
    name: str
    description: str
    attack: int

    def scare(self) -> int:
        return random.randint(self.attack // 2, self.attack)


# A simple factory to create a monster based on a scary idea

def create_nightmare(prompt: str) -> 'Monster':
    adjectives = [
        "grotesque", "shadowy", "whispering", "rotting", "faceless",
        "twisted", "crawling", "bleeding", "shrieking", "limbless"
    ]
    forms = [
        "wraith", "beast", "child", "statue", "doll", "mirror", "specter", "mass"
    ]
    seed = sum(map(ord, prompt))
    random.seed(seed)
    name = f"{random.choice(adjectives).title()} {random.choice(forms).title()}"
    description = (
        f"It resembles your fear of '{prompt}', manifesting as a {name.lower()}"
        f" that oozes dread."
    )
    attack = random.randint(5, 20)
    return Monster(name=name, description=description, attack=attack)
