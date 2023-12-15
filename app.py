from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

DATABASE_URI = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# creating models
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(30), unique=True, nullable=False)
    title = db.Column(db.String(30), unique=True, nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False)
    author = db.Column(db.String(40), unique=True, nullable=False)
    editor = db.Column(db.String(40), unique=True, nullable=False)

    # foreign key
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(40), unique=True)
    books = db.relationship("Book", backref="categories", lazy=True)



# cli command to create tables
@app.cli.command("create_tables")
def create_tables():
    try:
        db.create_all()
        print("Tables created successfully!")
    except:
        print("an error occured")



# routes
@app.route("/")
def index():
    return jsonify({"greeting": "Hello, World!!!"})


# get all books
@app.route("/books")
def get_all_books():
    books = Book.query.all()
    book_list = [
        {
            "id": book.id,
            "isbn": book.isbn,
            "title": book.title,
            "publication_date": book.publication_date.isoformat(),  # Convert to string for JSON
            "author": book.author,
            "editor": book.editor
        }
        for book in books
    ]
    return jsonify(book_list)


# get a book by id
@app.route("/books/<int:book_id>")
def get_book_by_id(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(
            {
                "id": book.id,
                "isbn": book.isbn,
                "title": book.title,
                "publication_date": book.publication_date.isoformat(),
                "author": book.author,
                "editor": book.editor
            }
        )
    return jsonify({"message": "Book not found"}), 404


# Get books of a category
@app.route("/categories/<int:category_id>/books", methods=["GET"])
def get_books_by_category(category_id):
    category = Category.query.get(category_id)
    if category:
        books_in_category = [
            {
                "id": book.id,
                "isbn": book.isbn,
                "title": book.title,
                "publication_date": book.publication_date.isoformat(),
                "author": book.author,
                "editor": book.editor
            }
            for book in category.books
        ]
        return jsonify(books_in_category)
    else:
        return jsonify({"message": "Category not found"}), 404


# Get a category by id
@app.route("/categories/<int:category_id>")
def get_category(category_id):
    category = Category.query.get(category_id)
    if category:
        return jsonify({"id": category.id, "category_name": category.category_name})
    return jsonify({"message": "Category not found"}), 404


# List all categories
@app.route("/categories")
def get_all_categories():
    categories = Category.query.all()
    return jsonify([
        {
            "id": category.id,
            "category_name": category.category_name
        }
        for category in categories
    ])


# Delete a book
@app.route("/books/<int:book_id>", methods = ["DELETE"])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"})
    return jsonify({"message": "Book not found"}), 404


# Delete a category
@app.route("/categories/<int:category_id>", methods = ["DELETE"])
def delete_category(category_id):
    category = Category.query.get(category_id)
    if category:
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted sucessfully"})
    return jsonify({"message": "Category not found"}), 404


# Modify informations of a book
@app.route("/books/<int:book_id>", methods = ["PUT"])
def update_book(book_id):
    book = Book.query.get(book_id)
    if book:
        data = request.get_json()
        book.isbn = data.get("isbn", book.isbn)
        book.title = data.get("title", book.title)
        book.publication_date = data.get("publication_date", book.publication_date)
        book.author = data.get("author", book.author)
        book.editor = data.get("editor", book.editor)
        book.category_id = data.get("category_id", book.category_id)
        
        db.session.commit()
        return jsonify({"message": "Book updated successfully"})
    return jsonify({"message": "Book not found"}), 404


# Modify informations of a category
@app.route("/categories/<int:category_id>", methods = ["PUT"])
def update_category(category_id):
    category = Category.query.get(category_id)
    if category:
        data = request.get_json()
        category.category_name = data.get("category_name", category.category_name)
        db.session.commit()
        return jsonify({"message": "Category updated successfully"})
    return jsonify({"message": "Category not found"}), 404