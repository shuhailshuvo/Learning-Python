from datetime import date, datetime


class Human:

    # instance attribute
    personalInfo = {
        "age": None,
        "name": None,
        "dob": None,
    }

    contactInfo = {
        "address": None,
        "phone": None,
        "email": None,
    }

    def __init__(self, name=""):
        self.personalInfo["name"] = name
        pass

    # Private
    def _updatePersonalInfo(self, name, dob):
        self.personalInfo["name"] = name
        self.personalInfo["dob"] = dob
        self.personalInfo["age"] = self.__calculateAge(dob)

    def _updateContactInfo(self, addr, phone, email):
        self.contactInfo["address"] = addr
        self.contactInfo["phone"] = phone
        self.contactInfo["email"] = email

    # protected
    def __calculateAge(self, dob):
        today = date.today()
        birthDate = datetime.strptime(dob, '%d-%m-%y')
        age = today.year - birthDate.year -\
            ((today.month, today.day) <
             (birthDate.month, birthDate.day))
        return age

    @property
    def basic(self):
        return self.personalInfo["name"]
