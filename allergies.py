class Allergies:
    
    lst = [];
    
    def __init__(self, testres):
        self.lst = [];
        allergens = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats'];
        for i in range(8):
            if testres & 1 << i != 0:
                self.lst.append(allergens[i]);
            
    def is_allergic_to(self, testing):
        return (testing in self.lst);
