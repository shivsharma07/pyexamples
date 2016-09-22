class AdoptionCenter:
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = location
        
    def get_name(self):
        return self.name
    
    def get_location(self):
        location = []
        for coordinate in self.location:
            location.append(float(coordinate))
        return tuple(location)
        
    def get_species_count(self): 
        species = {}       
        for key, value in self.species_types.items():
            if self.species_types[key] > 0:
                species[key] = value
        return species
        
    def get_number_of_species(self, species_name):
        return self.species_types[species_name]
        
    def adopt_pet(self, species_name):
        if self.species_types[species_name] == 0:
            del self.species_types[species_name]
        if self.species_types[species_name] > 0:
            self.species_types[species_name] = self.species_types[species_name] - 1


testobj = AdoptionCenter('xyz', {'Dog':3,'Cat':1}, (1,1))
testobj.adopt_pet('Cat')
print testobj.get_species_count()
print testobj.get_number_of_species('Cat')
