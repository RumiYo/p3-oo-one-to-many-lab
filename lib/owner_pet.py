class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        Pet.add_pet_to_all(self)

    @property 
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if not value in Pet.PET_TYPES:
            raise Exception
        self._pet_type = value

    @classmethod
    def add_pet_to_all(cls, pet):
        cls.all.append(pet)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        pet.owner = self

    def get_sorted_pets(self):
        owners_pet = Owner.pets(self)
        return sorted(owners_pet, key=lambda pet: pet.name)