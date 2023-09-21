
def generate_random_data():
    random_string = 'Hope miss project cost speech size.'
    random_number = 12

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Hope miss project cost speech size.")
        print(f"Random Number: 12")

if __name__ == "__main__":
    main()
