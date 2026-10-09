"""
Author: Mekkhi Adkins
Course Number and Name: CSC 212 - Data Structures
Programming Assignment: Project 3 - Classes and objects
Program Description: This program uses classes and objects
to create a class called pet, reads the data from a text file
and populates the data attributes and outputs the fields using the class's mutator and __str__ methods
"""

#creating class 
class Pet:
    '''
    This is the constucor header
    self: the new Pet object being constructed
    pet_name: receives something like "Pepper"
    species: receives "parrot"
    family_type: receives "bird"
    owner: receives "Edward_Lear"
    '''
    def __init__(self, pet_name, species, family_type, owner):
        '''
        Storing parameter values as private attributes
        self.__attribute_name = parameter_name
        '''
        self.__petName = pet_name
        self.__petSpecies = species
        self.__petFamilyType = family_type
        self.__petOwnerName = owner
        
        '''
        These are the MUTATOR methods, a mutator changes an atrribute
        def mutator_name(self, new_value):
            self.__attribute = new_value
        '''
    def set_Name(self, pet_name):
        self.__petName = pet_name

    def set_Species(self, species):
        self.__petSpecies = species

    def set_Family_Type(self, family_type):
        self.__petFamilyType = family_type
     
    def set_Owner(self, owner):
        self.__petOwnerName = owner
         
    '''
        ACCESOR methods, an accessor retrieves an attribute without changing it
        Does not need a new value and retunrs the existing value, only need self
        def get_Name(self):
            return self.__petName
    '''
    def get_Name(self):
        return self.__petName
    
    def get_Species(self):
        return self.__petSpecies

    def get_Family_Type(self):
        return self.__petFamilyType

    def get_owner(self):
        return self.__petOwnerName

    def __str__(self):
        return "Pet name: " + self.get_Name() + \
               "\nSpecies: " + self.get_Species() + \
               "\nFamily type: " + self.get_Family_Type() + \
               "\nOwner: " + self.get_owner()

