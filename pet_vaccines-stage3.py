# === Stage 3: Хранилище в памяти ===
# Project: PetVaccines
pet_store.py

from datetime import date


class Pet:
    def __init__(self, name, kind, birth_date, weight):
        self.id = None
        self.name = name
        self.kind = kind
        self.birth_date = birth_date
        self.weight = weight

    def __repr__(self):
        return f"Pet(id={self.id}, name={self.name}, kind={self.kind}, birth_date={self.birth_date}, weight={self.weight})"


class PetStore:
    def __init__(self):
        self._store = {}

    def add_pet(self, name, kind, birth_date, weight):
        pet = Pet(name, kind, birth_date, weight)
        pet.id = self._next_id()
        self._store[pet.id] = pet
        return pet

    def get_pet(self, pet_id):
        return self._store.get(pet_id)

    def list_pets(self):
        return list(self._store.values())

    def _next_id(self):
        if not self._store:
            return 1
        return max(self._store.keys()) + 1


if __name__ == "__main__":
    store = PetStore()
    pet = store.add_pet("Рекс", "собака", date(2024, 1, 15), 12.5)
    print(pet)
    print(store.get_pet(pet.id))
    print(store.list_pets())
