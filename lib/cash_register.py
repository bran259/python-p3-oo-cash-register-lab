#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, item, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount

        for _ in range(quantity):
            self.items.append(item)

        self.last_transaction = transaction_amount

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0
