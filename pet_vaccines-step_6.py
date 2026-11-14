# === Stage 6: Связи между сущностями ===
# Project: PetVaccines
from datetime import date


class Pet:
    def __init__(self, name, kind, birthdate, weight):
        self.name = name
        self.kind = kind
        self.birthdate = birthdate
        self.weight = weight


class Vaccine:
    def __init__(self, name, product, date_applied, pet_id, schedule_id):
        self.name = name
        self.product = product
        self.date_applied = date_applied
        self.pet_id = pet_id
        self.schedule_id = schedule_id


class VaccineSchedules:
    def __init__(self):
        self._pets = {}
        self._vaccines = {}
        self._schedules = {}

    def add_pet(self, pet):
        self._pets[pet.name] = pet

    def add_vaccine(self, vaccine):
        self._vaccines[vaccine.pet_id] = vaccine

    def add_schedule(self, schedule_id, pet_name, steps):
        self._schedules[schedule_id] = {
            "pet_name": pet_name,
            "steps": steps,
        }

    def get_all_vaccines(self, pet_name):
        pet = self._pets.get(pet_name)
        if pet is None:
            raise KeyError(f"Питомец '{pet_name}' не найден")
        pet_id = pet.name
        return [
            self._vaccines[vid]
            for vid in self._vaccines
            if self._vaccines[vid].pet_id == pet_id
        ]

    def check_integrity(self, pet_name):
        pet = self._pets.get(pet_name)
        if pet is None:
            return False
        pet_id = pet.name
        vaccines = self._vaccines
        return all(
            vid in vaccines
            and vaccines[vid].pet_id == pet_id
            and isinstance(vaccines[vid].date_applied, date)
            for vid in vaccines
            if vaccines[vid].pet_id == pet_id
        )


if __name__ == "__main__":
    app = VaccineSchedules()
    app.add_pet(Pet("Рекс", "собака", date(2022, 5, 1), 12.5))
    app.add_vaccine(Vaccine("Дистемпер", "Мурри-Рихт", date(2023, 6, 1), "Рекс", 1))
    app.add_vaccine(Vaccine("Бешенство", "Нобивак", date(2024, 1, 1), "Рекс", 2))
    print(app.get_all_vaccines("Рекс"))
    print(app.check_integrity("Рекс"))
