import sys


class ConCap(object):
    """ This Program saves in a dictionary, countries with capitals """

    def __init__(self):
        self.country = {}

    def addcountry(self):
        count = True
        while count == True:
            countries = raw_input("Insert a country: ")
            if countries.isalpha():
                countries = countries.lower()
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
                self.country[countries] = capital
                print self.country 
                self.anothercountry()
            else:
                print "invalid capital"
                cap = True

    def anothercountry(self):
        """ask if the user wants to add another article to INVENTARY"""
        others = True
        while others == True:
            other = raw_input("Do you want to add another country? yes or no: ")
            other = other.lower()
            if other == "yes":
                self.addcountry()
            elif other == "no":
                self.menus()
            else:
                print "Insert only yes or no"

    def countries(self):
        print "COUNTRIES"
        for i in self.country: #lists the countries
            print "-", i #prints a dash and the countries

    def instructions(self):
        print "INSTRUCTIONS"
        print """If you want to add a country with its respective capital, insert the word "Country" """
        print """If you want to check the list of countries that you already added, insert the word "Countries" """
        print """If you want to check the list of capitals that you already added, insert the word "Capitals" """
        print """If you want to check both countries and capitals that you already added, insert the word "All" """
        print """If you want to check both alphabetically ordered, insert the word "AllOrdered" """
        print """If you want to send of countries and capitals to lgarcia@cognits.co, insert the word "AllMail" """


    def menus(self):
        """provide the menu"""
        self.instructions()
        menu = True
        while menu == True:
            option = raw_input(" Insert here the word:  ")
            option = option.lower()
            if option == "country":
                self.addcountry()
                menu = False
            elif option == "countries":
                self.countries()
                menu = False

            else:
                print "please insert a valid option"
                menu = True


PRUEBA = ConCap()
PRUEBA.menus()
print "hola mundo"

