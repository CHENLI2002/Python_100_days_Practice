travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above



def add_new_country(country_name, visit_times, city_names):
    new_dictionary = {
        "country": country_name,
        "visits": visit_times,
        "cities": city_names,
    }
    
    travel_log.append(new_dictionary)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)