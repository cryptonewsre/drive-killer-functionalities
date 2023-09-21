
def generate_random_data():
    random_string = 'Control successful sometimes situation.'
    random_number = 78

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Control successful sometimes situation.")
        print(f"Random Number: 78")

if __name__ == "__main__":
    main()
