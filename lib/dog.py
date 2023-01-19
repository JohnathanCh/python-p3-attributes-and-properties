#!/usr/bin/env python3

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
    
    def set_dog_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
            
    def get_dog_name(self):
        return self._name
    
    def set_dog_breed(self, breed):
        if type(breed) == str and breed in Dog.approved_breeds:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    def get_dog_breed(self):
        return self._breed
    
    name = property(get_dog_name, set_dog_name)
    breed = property(get_dog_breed, set_dog_breed)
