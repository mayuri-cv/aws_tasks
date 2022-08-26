from faker import Faker
import dumper

faker = Faker()

profile1 = faker.simple_profile()
dumper.dump(profile1)

print('--------------------------')

profile2 = faker.simple_profile('M')
dumper.dump(profile2)

print('--------------------------')

profile3 = faker.profile(sex='F')
dumper.dump(profile3)