import json
import os

file_path = "cs2statstai.json"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def load_stats():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    
    return {"matches": [], "total_stats": {}, "map_stats": {}}


def save_stats(data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def add_match(map_name, kills, deaths):
    data = load_stats()

    kdr = round(kills / deaths if deaths > 0 else kills, 2)

    match_entry = {
        "map": map_name,
        "kills": kills,
        "deaths": deaths,
        "kdr": kdr
    }
    data["matches"].append(match_entry)

    total = data.setdefault("total_stats",{})
    total["matches_played"] = total.get("matches_played", 0) + 1
    total["total_kills"] = total.get("kills", 0) + kills
    total["total_deaths"] = total.get("deaths", 0) + deaths
    total["overall_kdr"] = round(total["total_kills"] / total["total_deaths"], 2) if total["total_deaths"] > 0 else total["total_kills"]

    map_stats = data.setdefault("map_stats", {})
    if map_name not in map_stats:
        map_stats[map_name] = {
            "matches_played": 0, 
            "total_kills": 0,
            "total_deaths": 0,
            "overall_kdr": 0,
}
    map_entry = map_stats[map_name]
    map_entry["matches_played"] += 1
    map_entry["total_kills"] += kills
    map_entry["total_deaths"] += deaths
    map_entry["overall_kdr"] = round(map_entry["total_kills"] / map_entry["total_deaths"], 2) if map_entry["total_deaths"] > 0 else map_entry["total_kills"]

    save_stats(data)
    print(f"Match on {map_name} added successfully! KDR: {kdr}, Kills: {kills}, Deaths: {deaths}")

def list_stats():
    data = load_stats()
    print("Total Stats:")
    total = data.get("total_stats", {})
    print(f"Matches Played: {total['matches_played']}")
    print(f"Total Kills: {total['total_kills']}")
    print(f"Total Deaths: {total['total_deaths']}")
    print(f"Overall KDR: {total['overall_kdr']}")
    print("\nMap Stats:")
    map_stats = data["map_stats"]
    for map_name, map_entry in map_stats.items():
        print(f"Map: {map_name}")
        print(f"Matches Played: {map_entry['matches_played']}")
        print(f"Total Kills: {map_entry['total_kills']}")
        print(f"Total Deaths: {map_entry['total_deaths']}")
        print(f"Overall KDR: {map_entry['overall_kdr']}")
        print()

def clear_stats():
    if os.path.exists(file_path):
        os.remove(file_path)
        print("Stats cleared successfully!")
    else:
        print("No stats to clear!")

def main():
    while True:
        print("1. Add Match")
        print("2. List Stats")
        print("3. clear Stats")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            cls()
            map_name = input("Enter the map name: ")
            kills = int(input("Enter the number of kills: "))
            deaths = int(input("Enter the number of deaths: "))
            add_match(map_name, kills, deaths)
        elif choice == "2":
            cls()
            list_stats()
        elif choice == "3":
            cls()
            clear_stats()
        elif choice == "4":
            cls()
            break

        else:
            print("Invalid choice! Please try again.")

main()

