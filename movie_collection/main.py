import json


#   *************** Adding Movies ****************************

def add_to_fav():
    name = input("Enter movie name: ").lower
    year = input("Enter movie year: ")
    genre = input("Enter the movie genre: ").lower
    director = input("Enter movie director: ").lower

    new_addition = {
        name: {
            "year": int(year),
            "genre": genre,
            "director": director
        }
    }

    try:
        file = open("./my_movies.json", "r")
        data = json.load(file)

    except FileNotFoundError:
        # Creating the file if it doesn't exit
        file = open("./my_movies.json", "w")
        json.dump(new_addition, file, indent=4)

    else:
        # Updating the old file
        data.update(new_addition)
        # Saving the new data to the old file i.e writing
        file = open("./my_movies.json", "w")
        json.dump(data, file, indent=4)


# ****************** Search Movies ****************************
def search():
    search_param = input("Would you like to search by movie name or year? ").lower()

    file = open("./my_movies.json", "r")
    data = json.load(file)

    if search_param == "year":
        keyword = int(input(f"Please enter movie {search_param}: "))
        for key in data:
            if data[key][search_param] == keyword:
                print(key, data[key])
    else:
        keyword = input(f"Please enter movie {search_param}: ")
        for key in data:
            if key == keyword:
                print(key, data[key])


# ************* List all movies *****************************************
def list_all():
    file = open("./my_movies.json", "r")
    data = json.load(file)
    for key in data:
        print(key, data[key])



# ****************** Operations ********************************


operation = input("What would like to do? 'add', 'search' or 'list' and 'q' to quit: ")

while operation != "q":
    if operation == "add":
        add_to_fav()
    elif operation == "search":
        search()
    elif operation == "list":
        list_all()
    else:
        operation = "q"
        print("Exiting the program...")


    operation = input("What would like to do? 'add', 'search' or 'list' and 'q' to quit: ")
