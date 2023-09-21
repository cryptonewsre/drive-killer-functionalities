
def generate_random_data():
    random_string = 'Role range loss yard instead.'
    random_number = 47

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Role range loss yard instead.")
        print(f"Random Number: 47")

if __name__ == "__main__":
    main()
