# To-Do List API

A simple RESTful API for managing a personal to-do list. It features user authentication with JSON Web Tokens (JWT) and full CRUD (Create, Read, Update, Delete) functionality for tasks. Each user's tasks are private and can only be accessed by them.

---

## Features

- **User Authentication**: Secure user registration and login system.
- **JWT Authorization**: Endpoints are protected using JWTs, ensuring that users can only access their own data.
- **CRUD Operations for Tasks**: Full support for creating, reading, updating, and deleting tasks.
- **User-Task Association**: Each task is automatically linked to the authenticated user who created it.
- **Pagination**: The endpoint for retrieving tasks supports pagination to efficiently handle large numbers of tasks.

---

## Technology Stack

- **Backend**: Node.js, Express.js
- **Database**: MongoDB with Mongoose ODM
- **Authentication**: JSON Web Tokens (JWT), bcrypt.js for password hashing

---

## Prerequisites
Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/)
- [MongoDB](https://www.mongodb.com/try/download/community) (or a MongoDB Atlas account)

---

## Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/manasyesuarthana/backend-practice-projects
cd todo_list_api/
```

2. **Install dependencies:**
```bash
npm install
```

3. **Create a `.env` file:**
Create a file named `.env` in the root of your project and add the following environment variables.

```env
# Your MongoDB connection string
MONGO_URI="mongodb+srv://..."

# A strong, secret string for signing JWTs
JWT_SECRET="your_super_secret_and_long_jwt_key"
```
I have alreay provided an example .env in the repo.

4. **Start the server:**
```bash
npm start
```
The API should now be running at `http://localhost:3000`.

---

## API Endpoints

### Authentication

#### `POST /auth/register`
Registers a new user.

- **Body:**
```json
{
    "name": "Alex Ryder",
    "email": "alex.ryder@example.com",
    "password": "a-very-secure-password123"
}
```
- **Success Response (201 Created):**
```json
{
    "message": "User registered successfully."
}
```

#### `POST /auth/login`
Logs in an existing user and returns a JWT.

- **Body:**
```json
{
    "email": "alex.ryder@example.com",
    "password": "a-very-secure-password123"
}
```
- **Success Response (200 OK):**
```json
{
    "message": "Login Successful.",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Tasks
**Note:** All task endpoints are protected and require a valid JWT in the `Authorization` header.
-   **Header:** `Authorization: Bearer <YOUR_TOKEN>`

#### `POST /todos`
Creates a new task for the authenticated user.

- **Body:**
```json
{
    "title": "Buy groceries",
    "description": "Milk, bread, and eggs."
}
```
- **Success Response (201 Created):** Returns the newly created task object.
```json
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, bread, and eggs.",
    "user": "67e9b2eb34d8a1c8f4c3a2b1",
    "_id": "67e9b31234d8a1c8f4c3a2b3",
    "createdAt": "2025-09-15T06:30:00.000Z",
    "updatedAt": "2025-09-15T06:30:00.000Z"
}
```

#### `GET /todos`
Retrieves a paginated list of tasks for the authenticated user.

- **Query Parameters:**
    - `page` (optional, default: 1): The page number.
    - `limit` (optional, default: 10): The number of tasks per page.
- **Example Request:** `GET /todos?page=1&limit=5`
- **Success Response (200 OK):**
```json
{
    "tasks": [
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, bread, and eggs.",
            "user": "67e9b2eb34d8a1c8f4c3a2b1",
            "_id": "67e9b31234d8a1c8f4c3a2b3",
            "createdAt": "2025-09-15T06:30:00.000Z",
            "updatedAt": "2025-09-15T06:30:00.000Z"
        }
    ],
    "currentPage": 1,
    "limit": 5,
    "totalPages": 1
}
```

#### `PUT /todos/:id`
Updates an existing task belonging to the authenticated user. The `:id` is the custom auto-incrementing number.

- **Body:**
    ```json
    {
        "title": "UPDATED - Buy groceries",
        "description": "Milk, bread, eggs, and cheese."
    }
    ```
- **Success Response (200 OK):** Returns the updated task object.
```json
{
    "id": 1,
    "title": "UPDATED - Buy groceries",
    "description": "Milk, bread, eggs, and cheese.",
    "user": "67e9b2eb34d8a1c8f4c3a2b1",
    "_id": "67e9b31234d8a1c8f4c3a2b3",
    "createdAt": "2025-09-15T06:30:00.000Z",
    "updatedAt": "2025-09-15T06:35:10.000Z"
}
```

#### `DELETE /todos/:id`
Deletes a task belonging to the authenticated user. The `:id` is the custom auto-incrementing number.

- **Success Response (200 OK):**
```json
{
    "message": "Task deleted successfully."
}
```