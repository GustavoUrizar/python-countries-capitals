COUNTRY = {}

def addcountry():
    count = True
    while count == True:
        country = raw_input("Insert a country: ")
        if country.isalpha():
            country = country.lower()
            count = False
        else:
            print "invalid country"
            count = True
    cap = True
    while cap == True:
        capital = raw_input("Insert capital: ") #asks to insert the item
        if capital.isalpha():
            capital = capital.lower()
            cap = False
            COUNTRY[country] = capital
            print COUNTRY  
            anothercountry()
        else:
            print "invalid capital"
            cap = True

def anothercountry():
    """ask if the user wants to add another article to INVENTARY"""
    others = True
    while others == True:
        other = raw_input("Do you want to add another country? yes or no: ")
        other = other.lower()
        if other == "yes":
            addcountry()
        elif other == "no":
            os.system("clear")
            menus()
        else:
            print "Insert only yes or no"

def instructions():
    print """"If you want to add a country with its respective capital, insert the word "country" """

def menus():
    """provide the menu"""
    menu = True
    while menu == True:
        option = raw_input(" Insert here the word:  ")
        option = option.lower()
        if option == "country":
            addcountry()
            menu = False
        else:
            print "please insert a valid option"
            menu = True

print menus()