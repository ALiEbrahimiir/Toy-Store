
# Toy Store API

This is a simple API built with FastAPI that provides authentication and toy management functionality. The API allows users to log in and manage a list of toys by performing CRUD operations (Create, Read, Update).

## Requirements

- Python 3.7+
- FastAPI
- Pydantic

## Installation

1. **Clone the repository** (if necessary):

   ```bash
   git clone https://github.com/AliEbrX/Toy-Store.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Toy-Store
   ```

3. **Install the dependencies**:

   ```bash
   pip install fastapi uvicorn pydantic
   ```

## Running the Application

You can run the application locally using Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## Endpoints

### 1. **Login**

   - **URL**: `/login/`
   - **Method**: `POST`
   - **Description**: Authenticates a user and sets a cookie if the credentials are correct.
   - **Request Body**:
     ```json
     {
       "username": "Admin",
       "password": "admin"
     }
     ```
   - **Response**:
     - Success: `{"Msg" : "Login Successfully"}`
     - Error: `401 Unauthorized` with `{"detail": "Invalid User"}`

### 2. **Get Toy List**

   - **URL**: `/store/`
   - **Method**: `GET`
   - **Description**: Retrieves the list of toys.
   - **Headers**: Requires `auth_token` cookie.
   - **Response**:
     - Success: A list of toys.
     - Error: `401 Unauthorized` with `{"detail": "Not Logged In!"}`

### 3. **Add a New Toy**

   - **URL**: `/store/`
   - **Method**: `POST`
   - **Description**: Adds a new toy to the list.
   - **Request Body**:
     ```json
     {
       "number": 1,
       "name": "Toy Name",
       "desc": "Toy Description",
       "has_discount": true
     }
     ```
   - **Headers**: Requires `auth_token` cookie.
   - **Response**:
     - Success: `{"Msg": "Save Successful"}`
     - Error: `401 Unauthorized` with `{"detail": "Not Logged In!"}`

### 4. **Update an Existing Toy**

   - **URL**: `/store/{number}`
   - **Method**: `PUT`
   - **Description**: Updates the details of an existing toy based on its number.
   - **Request Body**:
     ```json
     {
       "number": 1,
       "name": "Updated Toy Name",
       "desc": "Updated Toy Description",
       "has_discount": false
     }
     ```
   - **Headers**: Requires `auth_token` cookie.
   - **Response**:
     - Success: `{"Msg": "Update Successful"}`
     - Error: `404 Not Found` with `{"detail": "number not found!"}`

## License

This project is licensed under the MIT License.
