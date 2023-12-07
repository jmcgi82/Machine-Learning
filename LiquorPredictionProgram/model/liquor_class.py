class liquor:
    
    def __init__(self, id: str, name: str, type: str, price_per_ounce: str, alcohol_content: str) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.price_per_ounce = price_per_ounce
        self.alcohol_content = alcohol_content
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type

    def getPricePerOunce(self):
        return float(self.price_per_ounce)
    
    def getAlcoholContent(self):
        return float(self.alcohol_content)
    
    def __str__(self):
        return str(self.id) + "," + self.name + ',' + self.type + ',' + str(self.price_per_ounce) + ',' + str(self.alcohol_content)