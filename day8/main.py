from storeManagementSystem import Store

# colors
red    = '\u001b[31m'
green  = '\u001b[32m'
yellow = '\u001b[33m'
reset  = '\u001b[0m'


def store_window(store):
    tasks = ("All Books", "Add Book", "Remove Book", "Exit")
    print(yellow,end="")
    print(("Welcome to "+store.name).center(50))
    for ind, task in enumerate(tasks):
        print(f"  [{ind+1}] {task}")
    print(reset)

if __name__=="__main__":
    store = Store("Mohit Book Store")
    while True:
        store_window(store)

        task = input(green+"[-] What do you want to do? ")

        if task == "1"  or task.strip().lower() == "all books":
            print(yellow)
            print("Code".center(10)+"Name".center(25)+"Author".center(20)+"Price".center(10))
            print("-"*65)
            for book in store.all_books:
                print(book.code.center(10)+book.name.center(25)+book.author.center(20)+book.price.center(10))
            print("_"*65)

        elif task == "2" or task.strip().lower() == "add book":
            book = store.addBook()
            print(green+book)

        elif task == "3" or task.strip().lower() =="remove book":
            result = store.removeBook()
            print(result)  
            
        elif task == "5" or task.strip().lower() == "exit":
            break
                