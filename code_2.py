
def generate_random_data():
    random_string = 'Night wait base herself company.'
    random_number = 79

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Night wait base herself company.")
        print(f"Random Number: 79")

if __name__ == "__main__":
    main()
