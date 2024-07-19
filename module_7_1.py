from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = "product.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        result = str(file.read())
        file.close()
        return result

    def add(self, *products):
        existing_products = self.get_products().split('\n')
        existing_names = {line.split(', ')[0] for line in existing_products if line}
        file = open(self.__file_name, "a")
        for prod in products:
            if prod.name in existing_names:
                print(f"Продукт {prod.name} уже есть в магазине")
            else:
                file.write(f"{prod}\n")
                existing_names.add(prod.name)
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
