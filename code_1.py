
def generate_random_data():
    random_string = 'Prepare shoulder miss family produce budget.'
    random_number = 58

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Prepare shoulder miss family produce budget.")
        print(f"Random Number: 58")

if __name__ == "__main__":
    main()
