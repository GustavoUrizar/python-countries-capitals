"""COUNTRIES AND CAPITALS"""

import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class countryandcap(object):
    """ Countries and Capitals """

    def __init__(self):
        self.country = {}

    def addcountry(self):
        """add countries and capitals"""
        os.system("clear")
        count = True
        while count == True:
            countries = raw_input("Insert a country: ")
            countries = countries.title()
            try:
                text = countries.decode("utf-8") #turn into a string
                variable = True
                for i in text:
                    if i.isalpha() == True or i == " ": #if the string is alfhabet
                        if variable == True: #if variable is true
                            variable = True
                    else:
                        variable = False #else, make it false
                if variable == False: #if variable is false
                    print "Invalid Country" #print message
                    count = True
                    #convert the original variable in true so it can repeat itself
                elif len(countries) <= 2:
                    count = True #if not, kill this part and go on
                else:
                    count = False

            except (ValueError, NameError, SyntaxError):
                print "Invalid Country" #just verifies, any possible mistake
                count = False
        cap = True
        while cap == True:
            capital = raw_input("Insert capital: ") #asks to insert the item
            capital = capital.title()
            try:
                text = capital.decode("utf-8") #turn into a string
                variable = True #another variable to verify
                for i in text:
                    if i.isalpha() == True or i == " ": #if the string is alfhabet
                        if variable == True: #if variable is true
                            variable = True #make it true
                    else:
                        variable = False #else, make it false
                if variable == False: #if variable is false
                    print "Invalid Capital" #print message
                    cap = True
                    #convert the original variable in true so it can repeat itself
                elif len(capital) <= 2:
                    print "Invalid Capital"
                    cap = True
                else:
                    cap = False
            except (ValueError, NameError, SyntaxError):
                print "Invalid Capital" #just verifies, any possible mistake
                cap = False
        print "YOU HAVE ADDED: "
        self.country[countries] = capital
        print self.country
        self.anothercountry()

    def anothercountry(self):
        """ask if the user wants to add another country and capital"""
        others = True
        while others == True:
            other = raw_input("Do you want to add another country? yes or no: ")
            other = other.lower()
            if other == "yes":
                self.addcountry()
            elif other == "no":
                os.system("clear")
                self.menus()
            else:
                print "Insert only yes or no"

    def countries(self):
        """shows the list of countries"""
        os.system("clear")
        print "COUNTRIES"
        for i in self.country: #lists the countries
            print "*", i #prints a star and the countries
        raw_input("Press enter to continue")
        os.system("clear")
        self.menus()

    def capitals(self):
        """shows the list of capitals"""
        os.system("clear")
        print "CAPITALS"
        for i in self.country: #list of capitals
            print "*", self.country[i] #prints a star and the capitals
        raw_input("Press enter to continue")
        os.system("clear")
        self.menus()

    def all(self):
        """shows the list of countries and capitals"""
        os.system("clear")
        print "COUNTRIES AND CAPITALS"
        for i in self.country: #list of capitals
            print "*", i, "*", self.country[i] #prints a dash and the capitals
        raw_input("Press enter to continue")
        os.system("clear")
        self.menus()

    def allordered(self):
        """shows the list of countries and capitals ordered"""
        os.system("clear")
        print "List of all countries with capitals in order"
        for key, value in sorted(self.country.iteritems(), key=lambda (k, v): (v, k)):
            print "%s - %s" % (key, value)#internet way to sort a dic by its values
        raw_input("Press enter to continue")
        os.system("clear")
        self.menus()

    def sendmail(self):
        """send the email"""
        username = "eltavourizar@gmail.com"
        password = ""
        adress = "gustavo.urizar@hotmail.com"
        body = "Countries and Capitals: "

        # Body of email
        for key, item in self.country.items():
            body += """
            """ + str(key) + " - " + str(item)

        # Forming the body of email
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = adress
        msg['Subject'] = "Countries and capitals"
        msg.attach(MIMEText(body, 'plain'))

        # This try controls if the email was sent
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(username, password)
            text = msg.as_string()
            server.sendmail(username, adress, text)
            server.quit()
            print "Email sent correctly"
            raw_input("Press enter to continue...")
            self.menus()
        except ValueError:
            print "Error ocurred"
            self.menus()

    def instructions(self):
        """Instructions"""
        os.system("clear")
        print "INSTRUCTIONS"
        print """1- If you want to add a country and capital, insert the word "Country" """
        print """2- If you want the list of countries added, insert the word "Countries" """
        print """3- If you want the list of capitals added, insert the word "Capitals" """
        print """4- If you want both countries and capitals added, insert the word "All" """
        print """5- If you want both alphabetically ordered, insert the word "AllOrdered" """
        print """6- If you want to send list of countries and capitals to lgarcia@cognits.co,
    insert the word "AllMail" """
        print """7- If you want to close the program, insert the word "exit" """


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
            elif option == "capitals":
                self.capitals()
                menu = False
            elif option == "all":
                self.all()
                menu = False
            elif option == "allordered" or option == "all ordered":
                self.allordered()
                menu = False
            elif option == "allmail" or option == "all mail":
                self.sendmail()
                menu = False
            elif option == "exit":
                print "Thank you for using us"
                menu = False
                break
            else:
                print "please insert a valid option"
                menu = True
                os.system("clear")
                self.instructions()
                print "please insert a valid option"


ALL = countryandcap()
ALL.menus()

