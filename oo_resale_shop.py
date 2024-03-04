from computer import Computer

class ResaleShop:

    # attributes
    
    inventory: list

    # constructors

    def __init__(self):
        self.inventory = []

    # methods
    
    # not given a limited amount of funds, so no subtraction of shop money
    def buy(self, itemID):
        """ adds a new computer to the shop inventory

        args:
            itemID (int): computer being bought
       
        """
        # add computer to inventory dictionary
        self.inventory.append(itemID)
    
    def sell(self, itemID):
        """ removes a computer from the shop inventory

        args:
            itemID (int): computer being sold
        """
        # if computer in inventory, remove computer from inventory
        if itemID in self.inventory:
            self.inventory.remove(itemID)
        # error message
        else:
            print(f"{itemID} not in inventory.") 
            
    def update_computer_price(self, computer, new_price):
        """_summary_

        args:
            computer (str): computer with price being updated
            new_price (str): new price of computer
        """
        if computer in self.inventory:
            computer.price = new_price
            print("Price updated successfully.")
        else:
            print(f"{computer} not found in inventory.")   
                
    def check_inventory(self):
        """ checks and prints the inventory of the shop
        """
    # check that the inventory is not empty
        if self.inventory.__len__() != 0:
            i = 0
            computer:Computer
            for computer in self.inventory:
                print(f"Item ID: {i+1} : 'description: {computer.description}, 'processor_type': {computer.processor_type}, 'hard_drive_capacity': {computer.hard_drive_capacity}, 'memory': {computer.memory}, 'operating_system': {computer.operating_system}, 'year_made': {computer.year_made}, 'price': {computer.price}")
        # error message
        else:
            print("No inventory to display.")