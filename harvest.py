############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller 
    ):
        """Initialize a melon."""

        self.pairings = []

        #Make attributes for each descriptor under init
        #append each attribute to pairing list for next function
        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        

        # Fill in the rest

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest

        #append the items pairing into the list pairings.

        self.pairings.append(pairing)

        return pairing



    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

        return new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    pairings = []

    #call MelonType function to create our melon types
    #call add_pairings() method to create pairings for each melon

    musk = MelonType(
    "musk",
    "Muskmelon",
    1998,
    "green",
    True,
    True
    )
    
    musk.add_pairing("mint")

    casaba = MelonType(
    "cas",
    "Casaba",
    2003,
    "orange",
    True,
    False
    )
    
    casaba.add_pairing("strawberries and mint")

    crenshaw = MelonType(
    "cren",
    "Crenshaw",
    1996,
    "green",
    True,
    False
    )
    
    crenshaw.add_pairing("prosciutto")

    yellow_watermelon = MelonType(
    "yw",
    "Yellow Watermelon",
    2013,
    "yellow",
    False,
    True
    )
    
    yellow_watermelon.add_pairing("ice cream")

    melons = [musk, casaba, crenshaw, yellow_watermelon]

    #for loop to add name to all_melon_types
    
    # all_melon_types.append(melon.name)

    for melon in melons:
        all_melon_types.append(melon)
        pairings.append(melon.pairings)

    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with \n{melon.pairings}")

    return
    


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_basket = {}
    

    for melon in melon_types:
        melon_values = [
        melon.pairings, 
        melon.code, 
        melon.name, 
        melon.first_harvest, 
        melon.color, 
        melon.is_seedless, 
        melon.is_bestseller
        ]
        # melon.code = key
        #word_count_dict[individual_words] = word_count_dict.get(individual_words, 0) + 1
        melon_basket[melon.code] = melon_values

    return melon_basket


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvested_from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by
        self.sellable = None

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvested_from_field != 3:
            self.sellable = True
        else:
            self.sellable = False

        return self.sellable




def make_melons():
    """Returns a list of Melon objects."""

    melon_objects = []
    
    melon1 = Melon(
        'yw',
        8,
        7,
        2,
        'Sheila'
    )

    melon2 = Melon(
        "yw", 
        3, 
        4, 
        2, 
        "Sheila"
    )

    melon3 = Melon(
        'yw',
        9,
        8,
        3,
        'Sheila'
    )

    melon4 = Melon(
        "cas", 
        10, 
        6, 
        35, 
        "Sheila"
    )
    
    melon5 = Melon(
        'cren',
        8,
        9,
        35,
        'Michael'
    )

    melon6 = Melon(
        "cren",
        8,
        9,
        35,
        "Michael"
    )


    melon7 = Melon(
        'cren',
        2,
        3,
        4,
        'Michael'
    )

    melon8 = Melon(
        "musk",
        6,
        7,
        4,
        "Michael"
    )
    
    melon9 = Melon(
        'yw',
        7,
        10,
        3,
        'Sheila'
    )
    melons = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

    for melon in melons:
        melon_objects.append(melon)

    return melon_objects
    
def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    sellable_melons = []

    for melon in melons:
        if melon.sellable == True:
            print(f'{melon} = sellable')
        if melon.sellable == False:
            print(f'{melon} = not sellable')

    pass

    
