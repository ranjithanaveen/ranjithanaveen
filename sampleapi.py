from typing import Optional
from fastapi import FastAPI

app = FastAPI()



BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

# @app.get("/")
# async def first_api():
#     return {'meaasge':  "Hello Sai, Welcome to FAST API"}

# @app.get("/{book_name}")
# async def read_book(book_name: str):
#     return BOOKS[book_name]

@app.get("/")
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("books/mybook")
async def read_fav_book():
    return { "book_title":" My favourite book"}

#path parameters
@app.get("books/{book_id}")
async def read_fav_book(book_id: int):
    return { "book_title":" My favourite book id is "+ str(book_id)}



@app.post("/")
async def create_book(book_title, book_author):
    current_book_id = 0

    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split("_")[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f'book_{current_book_id + 1}'] = {"title":book_title, "author":book_author}
    return BOOKS[f'book_{current_book_id + 1}']



@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_information = {'tilte': book_title , "author": book_author }
    BOOKS[book_name] = book_information
    return book_information


@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted '



#query parameters
@app.get("/assignment/")
async def read_book_assign(book_name: str):
    return BOOKS[book_name]

@app.delete("/assignment/")
async def delete_book_assign(book_name: str):
    del BOOKS[book_name]
    return BOOKS

# unvicorn sampleapi:app --reload
# http://127.0.0.1:8000/openapi.json
# http://127.0.0.1:8000/docs





# 1. i need some thing from server   --- get 
# 2. we have some thing with us , we need to give that info and get some results  --- post  query 
# 3. I need to add some new stuff to server -- put 
# 4. I need to delete the info with is with server -- delete


# CRUD --> C - Create , R- Read U - Update , d - delete 

# CRUD operation,  validation 
# AUTHENTICATION,
# documentation,
# exception,
# DATABASE ----->  
# front end ---> html and css , bootstrap
# productionization ---> azure , heroku , aws , gcp 


