# import from same directory
from .Human import Human


class Programmer(Human):
    # attributes
    skill = []
    expertise = {}
    trainings = {
        "HTML": {
            "Biginner": {
                "Expertise": "Morderate"
            },
            "Advanced": {
                "Expertise": "Advance"
            }
        },
        "JS": {
            "Biginner": {
                "Expertise": "Morderate"
            },
            "Advanced": {
                "Expertise": "Advance"
            }
        },
        "PHP": {
            "Biginner": {
                "Expertise": "Morderate"
            },
            "Advanced": {
                "Expertise": "Advance"
            }
        },
        "PYTHON": {
            "Biginner": {
                "Expertise": "Morderate"
            },
            "Advanced": {
                "Expertise": "Advance"
            }
        }
    }
    # instance attribute

    def __init__(self, skill=[], expertise={}):
        self.skill = skill
        self.expertise = expertise

    # behavior
    def addSkill(self, newSkill):
        self.skill.append(newSkill)

    def addexpertise(self, newexpertise, expertise):
        self.expertise[newexpertise] = expertise

    def updateExpertise(self, expertise, newExpertise):
        self.expertise[expertise] = newExpertise

    def prepareResume(self):
        return {
            "skill": self.skill,
            "expertise": self.expertise,
            "personalInfo": self.personalInfo,
            "contactInfo": self.contactInfo
        }

    def train(self, subject, course):
        if subject not in self.skill:
            self.skill.append(subject)

        self.expertise[subject] = self.trainings[subject][course]["Expertise"]
    pass
