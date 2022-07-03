class Store():
    def __init__(self,name):
        self.name =  name
        self.all_books = []

    def __str__(self):
        return self.name

    def addBook(self):
        name, author, price = input("[-] Enter Book details (name author price) : ").split(" ")
        code = str(len(self.all_books)+1) #book code
        for word in name.split(" "):
            code += word[0].upper()

        book = Book(name, author, price, code)
        self.all_books.append(book)
        return f"{name} is added successfully with code > {code}"

    def removeBook(self):
        code = input("[-] Enter Book Code : ")
        for book in self.all_books:
            if code == book.code:
                self.all_books.remove(book)
        return f"{code} is successfully removed !"

   
  


class Book():
    def __init__(self,name:str,author:str,price:int, code:str):
        self.name = name
        self.author = author
        self.price = price
        self.code = code
        
    
if __name__ == "__main__":
    st = Store("xyz")
    st.addBook()
    st.addBook()
    print(st.all_books)
    st.removeBook()
    print(st.all_books)
