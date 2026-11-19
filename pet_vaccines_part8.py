# === Stage 8: Фильтрация записей ===
# Project: PetVaccines
def filter_pets_by_species(pets, species):
    return [pet for pet in pets if pet["species"] == species]


def filter_pets_by_age_range(pets, from_date, to_date):
    from datetime import date

    def parse(value):
        if isinstance(value, date):
            return value
        return date.fromisoformat(value)

    start = parse(from_date)
    end = parse(to_date)

    filtered = []
    for pet in pets:
        birth = parse(pet["birth_date"])
        if start <= birth <= end:
            filtered.append(pet)
    return filtered


def filter_pets_by_species_and_age_range(pets, species, from_date, to_date):
    by_species = filter_pets_by_species(pets, species)
    return filter_pets_by_age_range(by_species, from_date, to_date)


def filter_pets_by_weight_range(pets, min_weight, max_weight):
    return [pet for pet in pets if min_weight <= pet["weight"] <= max_weight]


def filter_pets(pets, species=None, from_date=None, to_date=None, min_weight=None, max_weight=None):
    result = pets
    if species is not None:
        result = filter_pets_by_species(result, species)
    if from_date is not None or to_date is not None:
        result = filter_pets_by_age_range(result, from_date, to_date)
    if min_weight is not None or max_weight is not None:
        result = filter_pets_by_weight_range(result, min_weight, max_weight)
    return result
