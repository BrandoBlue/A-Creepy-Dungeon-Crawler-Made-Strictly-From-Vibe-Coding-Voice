"""A minimalist text-based dungeon crawler that spawns a nightmare from your fear."""
import random
from .player import Player
from .dungeon import Room


def main() -> None:
    print("Welcome to the Nightmare Dungeon.")
    name = input("What is your name? ") or "Wanderer"
    player = Player(name=name)

    fear_prompt = input("Describe the scariest thing you can imagine: ")
    rooms = [Room(i + 1, fear_prompt) for i in range(3)]

    for room in rooms:
        room.encounter(player)
        if not player.is_alive():
            print("You collapse, overwhelmed by fear. The dungeon claims another soul.")
            break
    else:
        print(
            f"You emerge shaking but alive. Fear: {player.fear}%, Health: {player.health}%."
        )


if __name__ == "__main__":  # pragma: no cover
    main()
