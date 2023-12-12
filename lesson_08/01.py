# Є список кличок тварин. Необхідно за допомогою функції map() створити
# новий список в якому перші літери всіх кличок будуть написані з великої
# літери, а решта всіх літер маленькі. Обмеження 5 знаків


my_pets = ['alfred', 'tabitha', 'WiLLiaM', 'Arla', 'REM']

new_pets = []
for item in my_pets:
    pet = item.title()
    pet = pet[:5] if len(pet) > 5 else pet
    new_pets.append(pet)
print(new_pets)

new_pets_2 = list(map(lambda x: x[:5].title() if len(x) > 5 else x.title(), my_pets))
print(new_pets_2)


def my_func(pet):
    pet = pet.title()
    pet = pet[:5] if len(pet) > 5 else pet
    return pet


new_pets_3 = list(map(my_func, my_pets))
print(new_pets_3)
