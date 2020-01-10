# Private properties should be prefixed by __
# Protected properties should be prefixed by _

# import Class from sub directory
from MyModule.Programmer import Programmer

# Create class object
kid = Programmer()

# access Human class extended by Programmer
kid._updatePersonalInfo("Test", "02-07-86")
kid._updateContactInfo("Dhaka, Bangladesh", "01670746301", "kid@world.com")

# access Programmer class methods
kid.train("HTML", "Biginner")
kid.train("HTML", "Advanced")
kid.train("JS", "Advanced")
kid.train("PHP", "Advanced")
kid.train("PYTHON", "Biginner")
resume = kid.prepareResume()

print(resume)
