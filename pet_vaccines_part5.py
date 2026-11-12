# === Stage 5: Связанная сущность ===
# Project: PetVaccines
from datetime import date


VACCINE_ID = 1000


class Vaccine:
    def __init__(self, name, manufacturer, minimum_age_days,
                 interval_days, total_doses):
        self.id = VACCINE_ID
        VACCINE_ID += 1
        self.name = name
        self.manufacturer = manufacturer
        self.minimum_age_days = minimum_age_days
        self.interval_days = interval_days
        self.total_doses = total_doses

    def schedule(self, birth_date):
        first_date = date.fromtimestamp(
            birth_date.timestamp() + self.minimum_age_days * 86400
        )
        current_date = first_date
        doses = []
        for dose_number in range(1, self.total_doses + 1):
            doses.append(current_date)
            if dose_number < self.total_doses:
                current_date += date.fromtimestamp(
                    self.interval_days * 86400
                )
        return doses

    def __str__(self):
        return (
            f"{self.name} ({self.manufacturer}): "
            f"мин. возраст {self.minimum_age_days} дн., "
            f"интервал {self.interval_days} дн., "
            f"всего доз {self.total_doses}"
        )


vaccines = {}


def add_vaccine(name, manufacturer, minimum_age_days,
                interval_days, total_doses):
    vaccine = Vaccine(name, manufacturer, minimum_age_days,
                      interval_days, total_doses)
    vaccines[vaccine.id] = vaccine
    return vaccine


def get_vaccine_by_id(vaccine_id):
    return vaccines.get(vaccine_id)


def get_all_vaccines():
    return list(vaccines.values())


def get_vaccine_schedule(vaccine_id, birth_date):
    vaccine = vaccines.get(vaccine_id)
    if vaccine is None:
        return None
    return vaccine.schedule(birth_date)


if __name__ == "__main__":
    add_vaccine("DHC", "Merial", 45, 21, 2)
    add_vaccine("Nobivac", "MSD", 70, 30, 3)
    print(get_all_vaccines())
    print(get_vaccine_schedule(1000, date(2020, 1, 1)))
