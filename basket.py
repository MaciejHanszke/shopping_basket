from constants import DISCOUNT_QUALIF_MAP, OFFERS
from exceptions import NotFoundException
from product import Product
from typing import List


class Basket:
    """Class representing the basket"""
    def __init__(self):
        """
        :param: None
        :return: None
        """
        self.content: List[Product] = []
        self.discounts = {}

    def add(self, product: Product):
        """
        :param Product product: The product to be added to basket.
        :return: None
        """
        self.content.append(product)

    def remove(self, product: Product):
        """
        :param Product product: The product to be removed from the basket.
        :return: None
        """
        if product not in self.content:
            raise NotFoundException(f'Product with name "{product.name}" is not in the basket')
        self.content.remove(product)

    def calculate_discount(self, promotion, item):
        """
        :param promotion: the object representing a single promotion
        :param item: object representing single item in the basket
        :return: a discount price for that particular item
        """
        discount = 0
        if promotion not in self.discounts:
            self.discounts[promotion] = {}
        counter = self.discounts[promotion].get("counter", 0) + 1
        if counter == OFFERS[promotion]["qualifying_no"]:
            discount += round(item.price * (OFFERS[promotion]['discount_size'] / 100), 2)
            counter = 0
        self.discounts[promotion]["counter"] = counter
        return discount

    def checkout(self):
        """
        Perform a checkout on the basket, checking the final undiscounted
        price of all the products in it, the discount price, and the final
        cost of all the items in the basket after the discount was applied
        """
        products_price = 0.0
        discount = 0.0
        for item in self.content:
            products_price += item.price
            for promotion in DISCOUNT_QUALIF_MAP.get(item.id, {}):
                discount += self.calculate_discount(promotion, item)

        products_price = round(products_price, 2)
        discount = round(discount, 2)
        print(f"sub-total: £{products_price}")
        print(f"discount: £{discount}")
        print(f"total: £{round(products_price - discount, 2)}")