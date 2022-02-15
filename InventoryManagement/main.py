import json      # For file saving and loading  
import os.path   # check if the file exists  

class Inventory: 
    pets = {}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        q = 0
        if key in self.pets:   # check if there are any keys in the inventory
            v = self.pets[key] # how many keys we have in the inventory
            q = v + qty
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key}: total = {self.pets[key]}')

    def remove(self, key, qty):
        q = 0
        if key in self.pets:   # check if there are any keys in the inventory
            v = self.pets[key] # how many keys we have in the inventory
            q = v - qty
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'Removed {qty} {key}: total = {self.pets[key]}')

    def display(self):
        for key, value in self.pets.items():
            print(f'{key} = {value}')

    def save(self):
        print('Saving Inventory')
        with open('inventory.txt', 'w') as f: # with automatically closes the file
            json.dump(self.pets, f)
        print('Saved!')

    def load(self):
        print('Loadinf Inventory')
        if not os.path.exists('inventory.txt'):
            print('Skipping, Nothing to load')
            return
        with open('inventory.txt', 'r') as f:
            self.pets = json.load(f)
        print('Loaded!')

def main():
    inv = Inventory()

    while True:
        action = input('Action: add, remove, list, save, exit: ').lower()
        if action == 'exit':
            break
        if action == 'add' or action == 'remove':
                key = input('Enter an animal: ').lower()
                qty = int(input('Enter the qty: '))
                if action == 'add':
                    inv.add(key, qty)
                if action == 'remove':
                    inv.remove(key, qty)
        if action == 'list':
            inv.display()
        if action == 'save':
            inv.save()

    inv.save()



if __name__ == "__main__":
    main()

