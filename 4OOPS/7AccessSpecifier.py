"""
If you have knowledge of any other oop language then you had a knowledge of acess specifier named as
Public , Private and Protected.
Lets Discuss about all this.
In programing when you make the member as Public you are making accesbale to the class , to derived class
and anywhere outside the class. 
Similary When you are creating your member as protected its be accesbale to the class and Derived class only.
IN the case of Private that make sense that only base class have the access to that member.
In Python if we implement these concept we have to use some of the conventions.
#Public => name = membername
#protected => _membername
#private => __membername

"""
#protected and private member can be used outside the class it is not syntatically forced 
#but just a naming conventions that means the way of using these member outside the class
#is some how diffrent. Rest you can use out you own custom Logic as well at the last i will also show that.

class Car:
	numberofwheels = 4
	_colour = "Black"
	__yearofmanfacture = 2017

class Bmw(Car):
	def __init__(self):
		print("Protected Attribute  ",self._colour)

car = Car()
print("Public Attribute numberofwheels ",car.numberofwheels)
bmw = Bmw()
print("Private Attribute ",car.__yearofmanfacture)
#car object has no attribute __yearofmanufacture
#when you are starting your attribute with '__' name mangling is being done to your attribute
#so internally it is stored as _Car__yearofmanfacture
#that make sense when you are finding __yearofmanfacture python was unable to find that.
print("Private Attribute ",car._Car__yearofmanfacture) #this will work



class Furniture:
    def __init__(self):
        self._typeOfWood = "Teakwood"

class Chair(Furniture):
    def __init__(self):
        # super is used to call base class methods. You will learn more about super in next Code Examples.
        # Here we are calling the init of our base class to initialise the type of wood as Teakwood
        super().__init__()
        self.__numberOfLegs = 4

    def setWoodType(self, typeOfWood):
        self._typeOfWood = typeOfWood

    def displayChairSpecification(self):
        print("This chair is made of {} and has {} legs".format(self._typeOfWood, self.__numberOfLegs))

chair = Chair()
print("Would you like to change the type of wood from Teakwood? Y/N")
userChoice = input()
if userChoice is 'Y':
    print("Enter the type of wood you would like your chair to be made of")
    typeOfWood = input()
    chair.setWoodType(typeOfWood)
chair.displayChairSpecification()