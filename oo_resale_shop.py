class ResaleShop:

    # attributes
    
    inventory: dict

    # constructors

    def __init__(self, inventory):
        self.inventory = inventory

    # methods
    
    # not given a limited amount of funds, so no subtraction of shop money
    def buy_computer(self, new_computer):
        """ adds a new computer to the shop inventory

        args:
            new_computer (str): computer being bought
       
        """
        # add computer to inventory dictionary
        self.inventory.append(new_computer)
    
    def sell_computer(self, computer):
        """ removes a computer from the shop inventory

        args:
            computer (str): computer being sold
        """
        # if computer in inventory, remove computer from inventory
        if computer in self.inventory:
            self.inventory.remove(computer)
        # error message
        else:
            print("Computer not in inventory")
    
    def update_computer_price(self, computer, new_price):
        """ updates a computer's price in the shop inventory

        Args:
            computer (_type_): _description_
            new_price (_type_): _description_
        """
        # if computer in inventory, update computer price
        if computer in self.inventory:
            self.inventory["price"] = new_price
        # error message
        else:
            print("Computer not in inventory")