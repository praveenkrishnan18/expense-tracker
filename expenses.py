import os
import json

def get_data(path):
    n_data = {}
    try:
        with open(path, "r") as file:
            data = json.load(file)

            if isinstance(data, list) and len(data) > 0:
                next_id = max(item.get("id",0) for item in data) + 1
            else:
                next_id = 1
    except json.JSONDecodeError:
        next_id = 1

    n_data["id"] = next_id

    items = ["amount", "category", "description", "date"]
    for key in items:
        if key == "amount":
            try:
                value = int(input("Enter Amount: "))
                n_data[key] = value
            except ValueError:
                print("Enter in numbers!")
        else:
            value = str(input(f"Enter {key}: "))
            n_data[key] = value

    return n_data

def add_data(n_data, path):
    if os.path.exists(path):
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("No data Found, Created new data!")
            data = []

        if isinstance(data, list):
            data.append(n_data)
        elif isinstance(data, dict):
            data.update(n_data)
            data = [data]
        else:
            raise TypeError("Unsupported Datatype")
    else:
        data = []

    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def drop_data(id, path):
    try:
        with open(path, "r") as file:
            data = json.load(file)

        for d in data:
            if d["id"] == id:
                data.remove(d)

        with open(path, "w") as file:
            json.dump(data, file, indent = 4)

        print("Data deleted successfully!")

    except FileNotFoundError:
        print("Data source is not found!")

def view_data(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data