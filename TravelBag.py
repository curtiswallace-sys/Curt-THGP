room_items = [
    "toothbrush",
    "toothpaste", 
    "rag", 
    "towel", 
    "clothes",
    "shoes",
    "socks",
    "PS5",
    "Weights",
    "Basketball"
    ]

travel_bag = []


while room_items:
    print("\nItems in your room:")
    for i, item in enumerate(room_items):
        print(f"{i}: {item}")

    choice = input("\nEnter the index of the item to pack (or type 'done' to finish): ")

    if choice.lower() == "done":
        break

    try:
        index = int(choice)
        if 0 <= index < len(room_items):
            
            item = room_items.pop(index)
            travel_bag.append(item)
            print(f"{item} packed!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number or 'done'.")


luggage = tuple(travel_bag)


travel_bag.clear()

print("\nYour luggage contains:")
print(luggage)
print("Number of items packed:", len(luggage))