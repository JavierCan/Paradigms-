
#OOP in python 

#name of class 
"""class car():
    wheel = 4 #atribute

    def move(self) : #metod 
        print ("the car move in 4 wheels ")
class moto() :
    wheel = 2
    def move(self) :
        print ("the moto move in 2 wheels") 
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

my_object= car() #'my _car' belongs in class car()

print ("my car has",my_object.wheel, "wheels")
my_object.move() #give atribute for object 


print (":::::::::::second object:::::::::::")
my_object2 = moto()

print ("my moto has", my_object2.wheel, "wheels")
my_object2.move()"""

class cachorro() :
    def __init__( self, color ,raza, id) :
        self.color = color
        self.raza = raza
        self.id = id  
    def __str__(self) :
        return  """\
    raza : {}
    color : {} """.format(self.raza, self.color)

    def __repr__(self) -> str :
        return "<cachorro{}>".format(self.id)

perrito = cachorro('marron claro', "golden retriever" , 1)
#print ("este  es un cachorro de la raza {} y es de color {}".format(perrito.raza, perrito.color))
print (repr(perrito))
















