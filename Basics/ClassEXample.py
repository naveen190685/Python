class Book:
    # __personalCopyOfBook = "";
    classVar = 0
    globVar
    # We don't just declare variables here like java
    # Author, Publisher, Rate

    # Anything with "self." is considered as variable
    # self actually denotes an object and its always there in python class function
    # and all variables in the class are accessed through it and declared through it
    # Below is a constructor
    # A constructor in Python a function with name __init(self, <Parameters>)
    def __init__(self, Author, Publisher, Rate):
        self.Author = Author
        self.Publisher = Publisher
        self.Rate = Rate
        self.classVar = self.classVar+1
        globVar = self.globVar+1


    def printDetails(self):
        print(self.Author)
        print(self.Publisher)
        print(self.Rate)

    def printClassVar(self):
        print("Class variable: "+self.classVar)


    def printGlobVar(self):
        print("Global variable: "+globVar)


Shiva_Trilogy = Book("Ram Prasad", "B.K Publication", 100)
Shiva_Trilogy.printDetails()
Shiva_Trilogy.printClassVar()
Sita = Book("Rajat Prashad", "B.K publisher", 150)
Sita.printDetails()
Sita.printClassVar()
Sita.printGlobVar()

