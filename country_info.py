from countryinfo import CountryInfo

count = input("Enter your country: ")
country = CountryInfo(count)

print("Capital:", country.capital())
print("Currencies:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())
print("TImezones:", country.timezones())