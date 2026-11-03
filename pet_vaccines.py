# === Stage 1: Каркас модуля ===
# Project: PetVaccines
from dataclasses import dataclass
from datetime import date


@dataclass
class Pet:
    name: str
    kind: str
    birth_date: date
    weight: float


def make_demo_pets() -> list[Pet]:
    return [
        Pet("Рекс", "собака", date(2020, 5, 12), 14.5),
        Pet("Барсик", "кошка", date(2022, 8, 3), 3.8),
        Pet("Хамсон", "хомяк", date(2023, 1, 20), 0.12),
    ]


def main() -> None:
    pets = make_demo_pets()
    print("Демо-питомцы проекта PetVaccines:")
    for pet in pets:
        print(f"{pet.name} ({pet.kind}, {pet.birth_date}, {pet.weight} кг)")


if __name__ == "__main__":
    main()
