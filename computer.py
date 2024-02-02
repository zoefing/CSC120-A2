class Computer:

    # attributes - information about a specific computer
    
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # constructors
    def __str__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # methods
    
    def update_OS(self, new_operating_system):
        """ updates the computer's operating system

        args:
            new_operating_system (str): new operating system to be installed
        """
        self.operating_system == new_operating_system
        
    def refurbish(self, new_processor_type, new_hard_drive_capacity, new_memory):
        """ updates the computer's processor type, hard drive capacity, and memory

        args:
            processor_type (str): current processor type pre-refurbishment
            hard_drive_capacity (int): current hard drive capacity pre-refurbishment
            memory (int): current memory pre-refurbishment
        """
        self.processor_type == new_processor_type
        self.hard_drive_capacity == new_hard_drive_capacity
        self.memory == new_memory