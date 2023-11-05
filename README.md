# Library API documentation

This documentation provides details about the endpoints and responses of the Flask library API.

## Table of Contents

1. [Introduction](#introduction)
2. [Creating Tables](#creating-tables)
3. [Endpoints](#endpoints)
    1. [Get All Books](#get-all-books)
    2. [Get a Book by ID](#get-a-book-by-id)
    3. [Get Books of a Category](#get-books-of-a-category)
    4. [Get a Category by ID](#get-a-category-by-id)
    5. [List All Categories](#list-all-categories)
    6. [Delete a Book](#delete-a-book)
    7. [Delete a Category](#delete-a-category)
    8. [Update Book Information](#update-book-information)
    9. [Update Category Information](#update-category-information)

## Introduction

#### Setup

#### Database Configuration

Before running the Flask API, make sure to set up your database configuration by creating a `.env` file in the project root directory. Add the following content to the `.env` file:

```bash
# .env
DATABASE_URI=<your_database_uri_here>
````
## Creating Tables

To create the necessary tables in the database, run the following Flask CLI command:

```bash
flask create_tables
 
```

## Endpoints
### Get all books
- **URL**: `/books`
- **Method**: `GET`
- **Response**:
```JSON
[
   {
      "id": 1,
      "isbn": "978-0-385-29724-7",
      "title": "The Alchemist",
      "publication_date": "1988-04-12T00:00:00",
      "author": "Paulo Coelho",
      "editor": "HarperCollins"
    },
    {
      "id": 2,
      "isbn": "978-0-345-60179-0",
      "title": "The Hitchhiker's Guide to the Galaxy",
      "publication_date": "1979-10-12T00:00:00",
      "author": "Douglas Adams",
      "editor": "Pan Books"
    },
    {
      "id": 3,
      "isbn": "978-0-330-25864-5",
      "title": "1984",
      "publication_date": "1949-06-08T00:00:00",
      "author": "George Orwell",
      "editor": "Secker & Warburg"
    },
    // other books...
]


```
### Get a book by id
- **URL**: `/books/<int:book_id>`
- **Method**: `GET`
- **Response**:
```JSON
{
    "id": 5,
    "isbn": "978-1-5011-4114-1",
    "title": "The Girl on the Train",
    "publication_date": "2015-01-13T00:00:00",
    "author": "Paula Hawkins",
    "editor": "Riverhead Books"
},

```

### Get books of a category
- **URL**: `/categories/<int:category_id>/books`
- **Method**: `GET`
- **Response**:
```JSON
[
   {
      "id": 1,
      "isbn": "978-0-385-29724-7",
      "title": "The Alchemist",
      "publication_date": "1988-04-12T00:00:00",
      "author": "Paulo Coelho",
      "editor": "HarperCollins"
    },
    {
      "id": 2,
      "isbn": "978-0-345-60179-0",
      "title": "The Hitchhiker's Guide to the Galaxy",
      "publication_date": "1979-10-12T00:00:00",
      "author": "Douglas Adams",
      "editor": "Pan Books"
    },
    // other books...
]


```
### Get a book by id
- **URL**: `/categories/<int:category_id>/books`
- **Method**: `GET`
- **Response**:
```JSON
{
    "id": 5,
    "isbn": "978-1-5011-4114-1",
    "title": "The Girl on the Train",
    "publication_date": "2015-01-13T00:00:00",
    "author": "Paula Hawkins",
    "editor": "Riverhead Books"
},

```

### Get a Category by ID

- **URL:** `/categories/<int:category_id>`
- **Method:** `GET`
- **Response:**
```JSON
  {
    "id": 1,
    "category_name": "Fantasy"
  }
```

### List All Categories

- **URL:** `/categories`
- **Method:** `GET`
- **Response:**
```JSON
[
    {
        "id": 1,
        "category_name": "Fantasy"
    },
    {
        "id": 2,
        "category_name": "Science Fiction"
    },
    // other categories...
]
```



### Delete a Book

- **URL:** `/books/<int:book_id>`
- **Method:** `DELETE`
- **Response:**
```JSON
{
    "message": "Book deleted successfully"
}

// or

{
  "message" : "Book not found"
}
```

### Delete a Category

- **URL:** `/categories/<int:category_id>`
- **Method:** `DELETE`
- **Response:**
```JSON
{
    "message": "Category deleted successfully"
}

// or

{
    "message": "Category not found"
}
```


### Update Book Information

- **URL:** `/books/<int:book_id>`
- **Method:** `PUT`
- **Request:**
  - Body should contain a JSON object with the fields to be updated. For example:
```JSON
  {
      "isbn": "New ISBN",
      "title": "New Title",
      "publication_date": "New Publication Date",
      "author": "New Author",
      "editor": "New Editor",
      "category_id": 1
  }
```
**Response**:
```JSON
{
    "message": "Book updated successfully"
}

// or

{
    "message": "Book not found"
}

```

### Update Category Information

- **URL:** `/categories/<int:category_id>`
- **Method:** `PUT`
- **Request:**
  - Body should contain a JSON object with the fields to be updated. For example:
  ```JSON
  {
      "category_name": "New Category Name"
  }

- **Response**:
```JSON
{
    "message": "Category updated successfully"
}

// or

{
    "message": "Category not found"
}

```
