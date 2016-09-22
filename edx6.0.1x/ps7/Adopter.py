class Adopter:
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
        
    def get_name(self):
        return self.name
        
    def get_desired_species(self):
        return self.desired_species
        
    def get_score(self, adoption_center):
        num_desired = adoption_center.get_number_of_species(self.desired_species)
        return 1 * float(num_desired)
        
class FlexibleAdopter(Adopter):
    def __init__(self, name, desired_species, considered_species):
        self.name = name
        self.desired_species = desired_species
        self.considered_species = considered_species
        
    def get_score(self, adoption_center):
        num_other = 0
        adopter_score = Adopter.get_score(self, adoption_center)
        for consideredspecies in self.considered_species:
            num_other += adoption_center.get_number_of_species(consideredspecies)
        score = adopter_score + 0.3 * num_other
        if score > 0:
            return score
        else:
            return 0.0
        
class FearfulAdopter(Adopter):
    def __init__(self, name, desired_species, feared_species):
        self.name = name
        self.desired_species = desired_species
        self.feared_species = feared_species
        
    def get_score(self, adoption_center):
        num_feared = 0
        adopter_score = Adopter.get_score(self, adoption_center)
        num_feared += adoption_center.get_number_of_species(self.feared_species)
        score = adopter_score - 0.3 * num_feared
        if score > 0:
            return score
        else:
            return 0.0
