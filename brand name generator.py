import random

def generate_business_name(name,specialty):
    specialties = {
        'medical': ['Healthcare', 'Medical Solutions', 'Wellness', 'LifeCare', 'MediCare', 'MediHealth'],
        'technical': ['Tech Solutions', 'Innovations', 'Tech Co', 'TechWorks', 'TechHive', 'Tech Wizards']
    }
    
    business_name = f"{name}'s {random.choice(specialties[specialty])}"
    return business_name


print("Welcome to the brand name generator.")
brand=generate_business_name(input("Enter you Name CEO ? "),input("Ehat is the specialties of the company medical OR technical ? "))
print(brand)
