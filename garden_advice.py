# Store advice for each season in a dictionary.
season_advice = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from the frost with covers.",
    "spring": "Feed new growth and keep the soil moist.",
    "autumn": "Trim dead leaves and prepare plants for cooler weather.",
}

# Store advice for each plant type in a dictionary.
plant_advice = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Harvest regularly to encourage new growth.",
}

# Store plant recommendations for each season.
season_recommendations = {
    "summer": ["tomatoes", "marigolds", "basil"],
    "winter": ["spinach", "kale", "broccoli"],
    "spring": ["lettuce", "carrots", "petunias"],
    "autumn": ["garlic", "onions", "pansies"],
}


# Return gardening advice based on the season entered by the user.
def get_season_advice(season):
    return season_advice.get(season)


# Return gardening advice based on the plant type entered by the user.
def get_plant_advice(plant_type):
    return plant_advice.get(plant_type)


# Return a recommendation of plants that grow well in the selected season.
def recommend_plants(season):
    plants = season_recommendations.get(season)

    if plants:
        return "Recommended plants for this season: " + ", ".join(plants) + "."
    return None


# Main program function.
# It collects the user's input, gathers advice, and prints the final result.
def main():
    # Ask the user for the current season and plant type.
    # Plant type can be left blank if the user only wants recommendations.
    season = input("Enter the season: ").strip().lower()
    plant_type = (
        input("Enter the plant type (or press Enter to skip): ").strip().lower()
    )

    # Build the final advice as a list of separate lines.
    advice = []

    season_message = None
    plant_message = None
    recommendation_message = None

    season_message = get_season_advice(season)
    plant_message = get_plant_advice(plant_type)

    if season_message:
        advice.append(season_message)

    if plant_message:
        advice.append(plant_message)

    if season_message and not plant_type:
        season_message = get_season_advice(season)
        recommendation_message = recommend_plants(season)

    if recommendation_message:
        advice.append(recommendation_message)

    # Print only the advice that matches the user's input.
    if advice:
        print("\n" + "\n".join(advice))
    else:
        print("\nNo gardening advice found for your input.")


# Run the program.
main()
