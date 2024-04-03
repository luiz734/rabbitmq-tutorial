car_types = ["normal", "utilitario", "luxo"]
neighborhoods = ["centro", "aguaverde", "batel"]

def ask_question(question, options):
    while True:
        print(question)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")
        try:
            choice = int(input("> "))
            if choice < 1 or choice > len(options):
                print("Invalid Option")
            else:
                return options[choice - 1]
        except ValueError:
            print("Invalid Option")
