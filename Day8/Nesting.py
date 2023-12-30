# Dict inside Dict
travel_log = {
    "France" :{"Most Beautiful": ["Paris", "Lille"], "Energatic": ["city1","city2"]},
    "Germany": {"Most Beautiul": ["Berlin", "Hamburg"],
                "Energatic": ["City1", "City2"]}
}
# Lists inside Lists
["A", "B", ["C", "D"]]
# Accessing Dict items
for discript in travel_log:
    print(f"Country list \n {travel_log[discript]}")

#  Lists inside Dict inside Lists
travel_log2 = [
    {
        "Country": "France",
        "Cites_visited": ["Paris", "Lille"],
        "total_visits": 12,
    },
    {
        "Country": "Germany",
        "Cities_visted": ["Berlin", "Hamburg"],
        "Total_visits": 4,
    }
]