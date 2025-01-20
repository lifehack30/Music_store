from Class.music_store import MusicStore

def main():
    store = MusicStore()

    while True:
        print("\nМеню музыкального магазина:")
        print("1. Управление альбомами")
        print("2. Управление артистами")
        print("3. Управление покупателями")
        print("4. Выход")
        choice = input("Введите выбор: ")

        if choice == "1":
            manage_albums(store)
        elif choice == "2":
            manage_artists(store)
        elif choice == "3":
            manage_customers(store)
        elif choice == "4":
            break
        else:
            print("Не правильный ввод, повтори попытку")

def manage_albums(store):
    while True:
        print("\nУправление альбомами:")
        print("1. Добавить альбом")
        print("2. Обновить альбом")
        print("3. Удалить альбом")
        print("4. Посмотреть альбомы")
        print("5. Вернутся")
        choice = input("Введите выбор: ")

        if choice == "1":
            title = input("Введите название альбома: ")
            artist_name = input("Введите название артиста: ")
            year = int(input("Введите год выпуска: "))
            price = float(input("Введите цену: "))
            store.add_album(title, artist_name, year, price)
        elif choice == "2":
            title = input("Введите название альбома для его изменения: ")
            new_title = input("Введите новое название альбома (Оставте пустым для пропуска): ")
            new_year = input("Введите новой год выпуска (Оставте пустым для пропуска): ")
            new_price = input("Введите новую цену (Оставте пустым для пропуска): ")
            store.update_album(title, new_title if new_title else None, int(new_year) if new_year else None, float(new_price) if new_price else None)
        elif choice == "3":
            title = input("Введите название альбома для его удаления: ")
            store.delete_album(title)
        elif choice == "4":
            store.list_albums()
        elif choice == "5":
            break
        else:
            print("Некорректный выбор, попробуйте сново")

def manage_artists(store):
    while True:
        print("\nУправление артистами:")
        print("1. Добавить артиста")
        print("2. Изменить артиста")
        print("3. Удалить артиста")
        print("4. Список артистов")
        print("5. Назад")
        choice = input("Введите ваш выбор: ")

        if choice == "1":
            name = input("Введите имя артиста: ")
            genre = input("Введите пол артиста: ")
            store.add_artist(name, genre)
        elif choice == "2":
            name = input("Введите имя артиста для изменения: ")
            new_name = input("Введите новое имя артиста (Оставте пустым для пропуска):")
            new_genre = input("Введите новый пол артиста (Оставте пустым для пропуска):")
            store.update_artist(name, new_name if new_name else None, new_genre if new_genre else None)
        elif choice == "3":
            name = input("Введите имя артиста для удаления: ")
            store.delete_artist(name)
        elif choice == "4":
            store.list_artists()
        elif choice == "5":
            break
        else:
            print("Некорректный выбор, попробуйте сново")

def manage_customers(store):
    while True:
        print("\nУправление клиентами:")
        print("1. Добавить Клиента")
        print("2. Изменить Клиента")
        print("3. Удалить Клиента")
        print("4. Список Клиентов")
        print("5. Назад")
        choice = input("Введите ваш выбор: ")

        if choice == "1":
            name = input("Введите имя клиента ")
            email = input("Введите email клиента: ")
            store.add_customer(name, email)
        elif choice == "2":
            name = input("Введите имя клиента для изменения: ")
            new_name = input("Введите новое имя клиента (Оставте пустым для пропуска): ")
            new_email = input("Введите новый email клиента (Оставте пустым для пропуска): ")
            store.update_customer(name, new_name if new_name else None, new_email if new_email else None)
        elif choice == "3":
            name = input("Введите имя клиента для удаления: ")
            store.delete_customer(name)
        elif choice == "4":
            store.list_customers()
        elif choice == "5":
            break
        else:
            print("Некорректный выбор, попробуйте сново")

if __name__ == "__main__":
    main()
