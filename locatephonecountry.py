import phonenumbers
from phonenumbers import geocoder

phone_numb_input = input("Type Phone Number With Country Code: ")
phone_numb = phonenumbers.parse(phone_numb_input)

print(geocoder.description_for_number(phone_numb,"en"))