from typing import Dict
from enum import Enum


class IngredientType(Enum):
    milk = 1
    coffee = 2
    water = 3


class CoffeeType(Enum):
    Cappuccino = 1
    Latte = 2
    Espresso = 3


class Ingredient():
    def __init__(self, name: IngredientType, qty: int):
        self.name = name
        self.quantity = qty

    def getName(self):
        return self.name

    def getQty(self):
        return self.quantity


class Coffee():
    def __init__(self, name: CoffeeType, price: int, recipe: Dict[str, Ingredient]):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getRecipe(self):
        return self.recipe


class CoffeePayement():
    def __init__(self, coffee: Coffee):
        self.status = False
        self.amount = coffee.getPrice()
        self.product = coffee.getName()
        self._initializePayement()

    def getAmount(self):
        return self.amount

    def getStatus(self):
        return self.status

    def getProduct(self):
        return self.product

    def _initializePayement(self):
        # code
        pass


class CoffeeVendor():
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(CoffeeVendor, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "menu"):
            self.ingredients = {}
            self.menu = {}
            self._initialize_ingredients()
            self._initialize_menu()

    @staticmethod
    def getInstance():
        if CoffeeVendor._instance is None:
            CoffeeVendor()
        return CoffeeVendor._instance

    def _initialize_ingredients(self):
        self.ingredients["milk"] = Ingredient(IngredientType.milk, 100)
        self.ingredients["coffee"] = Ingredient(IngredientType.coffee, 100)
        self.ingredients["water"] = Ingredient(IngredientType.water, 100)

    def _initialize_menu(self):
        espresso_recipe = {
            'coffee': Ingredient(IngredientType.coffee, 10),
            'water': Ingredient(IngredientType.water, 10),
        }
        latte_recipe = {
            'coffee': Ingredient(IngredientType.coffee, 10),
            'milk': Ingredient(IngredientType.milk, 10),
            'water': Ingredient(IngredientType.water, 10)
        }
        cappuccion_recipe = {
            'coffee': Ingredient(IngredientType.coffee, 5),
            'milk': Ingredient(IngredientType.milk, 10),
            'water': Ingredient(IngredientType.water, 10)
        }
        self.menu = {
            'cappuccino': Coffee(CoffeeType.Cappuccino, 120, cappuccion_recipe),
            'latte': Coffee(CoffeeType.Latte, 150, latte_recipe),
            'espresso': Coffee(CoffeeType.Espresso, 100, espresso_recipe),
        }

    def orderCoffee(self, coffee: Coffee):
        payement = CoffeePayement(coffee)
        return payement

    def pourCoffee(self, payObj: CoffeePayement):
        if payObj.getStatus:
            return CoffeePayement.getProduct()
        else:
            None
