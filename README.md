# Bookstore API

This project is a simple API for a bookstore. It allows users to view a list of books, get details of a particular book, add a book to their shopping cart, remove a book from their cart, and place an order.

## Technologies Used

The following technologies were used to build this project:

- Python
- Django
- SQLite

## Installation

To get started with this project, follow the instructions below:

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/bookstore-api.git
```

2. Create a virtual environment and activate it:

```
python3 -m venv env
source env/bin/activate
```

3. Install the required packages:

```
pip install -r requirements.txt
```

4. Create the SQLite database:

```
python manage.py migrate
```

5. Load sample data (optional):

```
python manage.py loaddata fixtures/sample_data.json
```

## API Endpoints

The following API endpoints are available:

`GET /books/`

Returns a list of all books in the database.

**Example Response:**

```
[
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 9.99,
    "published_date": "1925-04-10",
    "genre": "Fiction",
    "description": "The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan."
  },
  {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "price": 7.99,
    "published_date": "1960-07-11",
    "genre": "Fiction",
    "description": "The story of racial injustice and the loss of innocence in a small Southern town."
  }
]

```

`GET /books/{id}/`

Returns the details of a particular book by its ID.

**Example Response:**

```
{
  "id": 1,
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "price": 9.99,
  "published_date": "1925-04-10",
  "genre": "Fiction",
  "description": "The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan."
}

```

`POST /cart/`

Adds a book to the user's shopping cart.

**Example Request:**

```
{
  "book_id": 1,
  "quantity": 2
}
```

`DELETE /cart/{id}/`

Removes a book from the user's shopping cart by its ID.

`POST /orders/`

Places an order for the books in the user's shopping cart.

**Example Request:**

```
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "johndoe@example.com",
  "phone_number": "+1 (555) 123-4567",
  "address": "123 Main St",
  "city": "Anytown",
  "state": "CA",
  "zipcode": "12345"
}
```
