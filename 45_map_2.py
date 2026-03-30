#example of filter 
countries = [
    "India", "Finland", "Pakistan", "Australia", "Brazil",
    "Thailand", "Iceland", "Germany", "Kazakhstan", "Italy",
    "Poland", "Somalia", "Japan", "New Zealand", "Canada",
    "Uzbekistan", "Argentina", "Netherlands", "Sri Lanka", "Switzerland",
    "Ireland", "Bangladesh", "Norway", "Denmark", "Afghanistan",
    "Malaysia", "Colombia", "Greenland", "Nepal", "Swaziland",
    "Mongolia", "Indonesia", "England", "Scotland", "Estonia",
    "Latvia", "Lithuania", "Romania", "Bulgaria", "Serbia",
    "Croatia", "Slovakia", "Slovenia", "Armenia", "Georgia",
    "Ethiopia", "Albania", "Austria", "Belgium", "Mexico"
]
print(countries)
lands = list(filter(lambda item: 'land' in item,countries))

#task 
# filter countries whose name ends with stan
# filter countries whose name ends with ia 
print(lands)