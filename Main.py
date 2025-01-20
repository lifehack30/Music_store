from Class.music_store import MusicStore

def main():
    store = MusicStore()

    while True:
        print("\nMusic Store Menu:")
        print("1. Manage Albums")
        print("2. Manage Artists")
        print("3. Manage Customers")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            manage_albums(store)
        elif choice == "2":
            manage_artists(store)
        elif choice == "3":
            manage_customers(store)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_albums(store):
    while True:
        print("\nAlbum Menu:")
        print("1. Add Album")
        print("2. Update Album")
        print("3. Delete Album")
        print("4. List Albums")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter album title: ")
            artist_name = input("Enter artist name: ")
            year = int(input("Enter album year: "))
            price = float(input("Enter album price: "))
            store.add_album(title, artist_name, year, price)
        elif choice == "2":
            title = input("Enter album title to update: ")
            new_title = input("Enter new album title (leave blank to skip): ")
            new_year = input("Enter new album year (leave blank to skip): ")
            new_price = input("Enter new album price (leave blank to skip): ")
            store.update_album(title, new_title if new_title else None, int(new_year) if new_year else None, float(new_price) if new_price else None)
        elif choice == "3":
            title = input("Enter album title to delete: ")
            store.delete_album(title)
        elif choice == "4":
            store.list_albums()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_artists(store):
    while True:
        print("\nArtist Menu:")
        print("1. Add Artist")
        print("2. Update Artist")
        print("3. Delete Artist")
        print("4. List Artists")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter artist name: ")
            genre = input("Enter artist genre: ")
            store.add_artist(name, genre)
        elif choice == "2":
            name = input("Enter artist name to update: ")
            new_name = input("Enter new artist name (leave blank to skip): ")
            new_genre = input("Enter new artist genre (leave blank to skip): ")
            store.update_artist(name, new_name if new_name else None, new_genre if new_genre else None)
        elif choice == "3":
            name = input("Enter artist name to delete: ")
            store.delete_artist(name)
        elif choice == "4":
            store.list_artists()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_customers(store):
    while True:
        print("\nCustomer Menu:")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. List Customers")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            store.add_customer(name, email)
        elif choice == "2":
            name = input("Enter customer name to update: ")
            new_name = input("Enter new customer name (leave blank to skip): ")
            new_email = input("Enter new customer email (leave blank to skip): ")
            store.update_customer(name, new_name if new_name else None, new_email if new_email else None)
        elif choice == "3":
            name = input("Enter customer name to delete: ")
            store.delete_customer(name)
        elif choice == "4":
            store.list_customers()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()