from faker import Faker

faker = Faker()

print(f'Date of birth: {faker.date_of_birth()}')
print(f'Century: {faker.century()}')
print(f'Year: {faker.year()}')
print(f'Month: {faker.month()}')
print(f'Month name: {faker.month_name()}')
print(f'Day of week: {faker.day_of_week()}')
print(f'Day of month: {faker.day_of_month()}')
print(f'Time zone: {faker.timezone()}')
print(f'AM/PM: {faker.am_pm()}')