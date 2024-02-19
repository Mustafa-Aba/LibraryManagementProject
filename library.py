class Library:
    def __init__(self):
        # Dosyayı "a+" modunda aç
        self.file = open("books.txt", "a+")

    def __del__(self):
        # Nesne yok edildiğinde dosyayı kapat
        self.file.close()

    def list_books(self):
        # Dosyanın başına giderek mevcut kitapları oku
        self.file.seek(0)
        books = self.file.readlines()
        # Eğer kitap yoksa bilgi ver
        if not books:
            print("No books found in the library.")
            return
        # Her kitap için bilgileri ekrana yaz
        for book in books:
            book_info = book.strip().split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]}")

    def get_valid_input(self, prompt, validator):
        # Kullanıcıdan geçerli bir giriş alana kadar döngüyü sürdür
        while True:
            user_input = input(prompt)
            if validator(user_input):
                return user_input
            else:
                print(f"Invalid input. {prompt}")

    def add_book(self):
        # Dosya boşsa uyarı ver
        if self.file.tell() == 0:
            print("Warning: The books.txt file is empty.")

        # Kullanıcıdan kitap bilgilerini al
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = self.get_valid_input("Enter release year: ", lambda x: x.isdigit() and int(x) <= 2024)
        num_pages = self.get_valid_input("Enter number of pages: ", lambda x: x.isdigit() and int(x) > 0)
        
        # Kitabın zaten kütüphanede olup olmadığını kontrol et
        with open("books.txt", "r") as file:
            existing_books = file.readlines()
            for book in existing_books:
                book_info = book.strip().split(',')
                if title == book_info[0] and author == book_info[1]:
                    print("This book already exists in the library.")
                    return

        # Kitap bilgilerini dosyaya yaz
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        self.file.flush()  # Dosyanın hemen yazılmasını sağla
        print("Book added successfully!")

    def remove_book(self):
        # Silinecek kitabın başlığını kullanıcıdan al
        title_to_remove = input("Enter the title of the book to remove: ")
        
        # Mevcut kitapları oku
        with open("books.txt", "r") as file:
            existing_books = file.readlines()
        print("Existing books:", existing_books)  # Kontrol amacıyla mevcut kitapları yazdır

        # Kitabın mevcut olup olmadığını kontrol et
        found = False
        updated_books = []
        for book in existing_books:
            book_info = book.strip().split(',')
            if title_to_remove != book_info[0]:
                updated_books.append(book)
            else:
                found = True

        print("Updated books:", updated_books)  # Kontrol amacıyla güncellenmiş kitapları yazdır

        if found:
            # Güncellenmiş kitap listesini dosyaya yaz
            with open("books.txt", "w") as file:
                file.writelines(updated_books)
            print(f"The book '{title_to_remove}' has been successfully removed.")
        else:
            print(f"The book '{title_to_remove}' is not found in the library.")


    def quit(self):
        # Programdan çıkış yaparken dosyayı kapat
        self.file.close()
        print("Exiting the program. Goodbye!")

lib = Library()

def menu():
    # Kullanıcı menüsünü yazdır
    print("*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Quit")

def main():
    # Ana döngü
    while True:
        menu()
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            lib.quit()
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
