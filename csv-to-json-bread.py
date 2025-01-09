import csv
import json

# Function to convert CSV to JSON
def csv_to_json(csv_file_path, json_file_path):
    # Open the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Initialize an empty list to hold recipes
        recipes = []
        current_recipe = None

        for row in csv_reader:
            print("Processing row:", row)  # Debugging statement
            name = row.get("Name", "").strip()
            weight = row.get("Weight", "").strip()
            print("Name:", name, "Weight:", weight)  # Debugging statement

            # If there's a new recipe name, create a new recipe object
            if name:
                current_recipe = {
                    "name": name,
                    "weights": {}  # Start with an empty weights dictionary
                }
                recipes.append(current_recipe)
                print("Added new recipe:", current_recipe)  # Debugging statement

            # If there's no weight and the recipe is standalone
            if current_recipe and not weight:
                # Add standalone recipe fields directly
                recipe_data = {
                    "time": row.get("Time", "").strip(),
                    "water": row.get("Water", "").strip(),
                    "oil": row.get("Oil", "").strip(),
                    "olive oil": row.get("Olive Oil", "").strip(),
                    "skimmed milk": row.get("Skimmed Milk", "").strip(),
                    "egg": row.get("Egg", "").strip(),
                    "salt": row.get("Salt", "").strip(),
                    "sugar": row.get("Sugar", "").strip(),
                    "brown sugar": row.get("Brown Sugar", "").strip(),
                    "white flour": row.get("White Flour", "").strip(),
                    "instant yeast": row.get("Instant Yeast", "").strip(),
                    "whole wheat flour": row.get("Whole Wheat Flour", "").strip(),
                    "rye flour": row.get("Rye Flour", "").strip(),
                    "maize flour": row.get("Maize Flour", "").strip(),
                    "gluten-free flour": row.get("Gluten-free Flour", "").strip(),
                    "high-gluten flour": row.get("High-Gluten Flour", "").strip(),
                    "cooked rice": row.get("Cooked Rice", "").strip(),
                    "fruit pulp": row.get("Fruit Pulp", "").strip(),
                    "lemon juice": row.get("Lemon Juice", "").strip(),
                    "whole milk": row.get("Whole Milk", "").strip(),
                    "natural yogurt": row.get("Natural Yogurt", "").strip()
                }

                # Remove empty fields
                recipe_data = {key: value for key, value in recipe_data.items() if value}
                current_recipe.update(recipe_data)

            # If there's a weight, add it to the current recipe's weights
            if current_recipe and weight:
                weight_data = {
                    "time": row.get("Time", "").strip(),
                    "water": row.get("Water", "").strip(),
                    "oil": row.get("Oil", "").strip(),
                    "olive oil": row.get("Olive Oil", "").strip(),
                    "skimmed milk": row.get("Skimmed Milk", "").strip(),
                    "egg": row.get("Egg", "").strip(),
                    "salt": row.get("Salt", "").strip(),
                    "sugar": row.get("Sugar", "").strip(),
                    "brown sugar": row.get("Brown Sugar", "").strip(),
                    "white flour": row.get("White Flour", "").strip(),
                    "instant yeast": row.get("Instant Yeast", "").strip(),
                    "whole wheat flour": row.get("Whole Wheat Flour", "").strip(),
                    "rye flour": row.get("Rye Flour", "").strip(),
                    "maize flour": row.get("Maize Flour", "").strip(),
                    "gluten-free flour": row.get("Gluten-free Flour", "").strip(),
                    "high-gluten flour": row.get("High-Gluten Flour", "").strip(),
                    "cooked rice": row.get("Cooked Rice", "").strip(),
                    "fruit pulp": row.get("Fruit Pulp", "").strip(),
                    "lemon juice": row.get("Lemon Juice", "").strip(),
                    "whole milk": row.get("Whole Milk", "").strip(),
                    "natural yogurt": row.get("Natural Yogurt", "").strip()
                }

                # Remove empty fields
                weight_data = {key: value for key, value in weight_data.items() if value}

                current_recipe["weights"][weight] = weight_data

        # Write the JSON data to a file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump({"recipes": recipes}, json_file, indent=2, ensure_ascii=False)
            print(f"JSON file has been created at: {json_file_path}")

# Example usage
# csv_to_json('path_to_your_csv.csv', 'output_json_file.json')
csv_to_json('ingredients.csv', 'recipe_master.json')
