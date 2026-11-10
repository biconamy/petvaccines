# === Stage 4: Удаление и восстановление ===
# Project: PetVaccines
from datetime import date


class Pet:
    def __init__(self, name, kind, birth_date, weight):
        self.name = name
        self.kind = kind
        self.birth_date = birth_date
        self.weight = weight
        self.deleted = False
        self._id = None

    def __repr__(self):
        return f"Pet(name={self.name!r}, kind={self!r}, birth_date={self.birth_date!r}, weight={self.weight!r}, deleted={self.deleted!r})"

    def soft_delete(self):
        self.deleted = True

    def restore(self):
        self.deleted = False

    def is_active(self):
        return not self.deleted


class PetStorage:
    def __init__(self):
        self._pets = {}
        self._counter = 0

    def add_pet(self, name, kind, birth_date, weight):
        pet = Pet(name, kind, birth_date, weight)
        self._counter += 1
        pet._id = self._counter
        self._pets[pet._id] = pet
        return pet

    def get_pet(self, pet_id):
        return self._pets.get(pet_id)

    def list_active(self):
        return [pet for pet in self._pets.values() if not pet.deleted]

    def delete_pet(self, pet_id):
        pet = self._pets.get(pet_id)
        if pet is not None:
            pet.soft_delete()
            return True
        return False

    def restore_pet(self, pet_id):
        pet = self._pets.get(pet_id)
        if pet is not None:
            pet.restore()
            return True
        return False
