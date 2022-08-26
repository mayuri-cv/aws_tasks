from faker import Faker
faker = Faker('cz_CZ')

for i in range(3):

    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()

    print(f'{name}, {address}, {phone}')
