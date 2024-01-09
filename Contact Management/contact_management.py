import csv
import os

def save_to_csv(names, phone_numbers):
    filename = 'contacts.csv'

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone Number'])

        for name, phone_number in zip(names, phone_numbers):
            writer.writerow([name, phone_number])

    print(f"Contacts saved to {filename}")

def load_from_csv():
    filename = 'contacts.csv'
    
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            names = [row['Name'] for row in reader]
            phone_numbers = [row['Phone Number'] for row in reader]

        return names, phone_numbers
    else:
        return [], []

def get_user_input():
    names, phone_numbers = load_from_csv()

    while True:
        name = input("Enter Name (type 'stop' to finish): ")
        if name.lower() == 'stop':
            break

        phone_number = input("Enter Phone Number: ")

        names.append(name)
        phone_numbers.append(phone_number)

    save_to_csv(names, phone_numbers)

    return names, phone_numbers

def display_contacts(names, phone_numbers):
    print("\nName\t\t\tPhone Number\n")
    for i in range(len(names)):
        print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

def search_contact(names, phone_numbers):
    search_term = input("\nEnter search term (type 'stop' to exit search): ")

    while search_term.lower() != 'stop':
        found = False

        for i, name in enumerate(names):
            if search_term.lower() in name.lower():
                phone_number = phone_numbers[i]
                print("Search result: Name: {}, Phone Number: {}".format(name, phone_number))
                found = True

        if not found:
            print("Name Not Found")

        search_term = input("\nEnter search term (type 'stop' to exit search): ")

def main():
    names, phone_numbers = get_user_input()
    display_contacts(names, phone_numbers)

    search_contact(names, phone_numbers)

if __name__ == "__main__":
    main()
