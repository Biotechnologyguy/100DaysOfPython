# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
# Nesting dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "India": {
        "cities_visited": ["Pune", "Mumbai", "Delhi"]
    }
}

# Nesting dictionary in a  list
country_data = [capitals, travel_log]

# Travel log modified
travel_log2 = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "Country": "India",
        "cities_visited": ["Pune", "Mumbai", "Delhi"],
        "total_visits": 73
    },
]

print(travel_log)
print(travel_log2)
