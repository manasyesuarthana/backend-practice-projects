# Blog API Backend

This is the backend server for a full-stack blog application, built with Node.js, Express, and MongoDB. It provides a RESTful API for managing blog posts and user authentication, with role-based access control for admin users.

---

## Features

- **JWT Authentication**: Secure user login and registration using JSON Web Tokens.
- **Role-Based Access**: Distinction between regular `user` and `admin` roles.
- **Admin-Only Routes**: Protected endpoints for creating, editing, and deleting content.
- **Full CRUD for Blog Posts**: Complete Create, Read, Update, and Delete functionality for blog articles.
- **Password Hashing**: User passwords are securely hashed using `bcrypt` before being stored.
- **Environment Variable Management**: Securely manages secret keys and database strings using a `.env` file.

---

## Technologies Used

- **Node.js**: JavaScript runtime environment.
- **Express.js**: Web framework for Node.js.
- **MongoDB Atlas**: Cloud-hosted MongoDB database service.
- **Mongoose**: Object Data Modeling (ODM) library for MongoDB and Node.js.
- **JSON Web Token (JWT)**: For generating authentication tokens.
- **bcrypt**: For hashing passwords.
- **dotenv**: For loading environment variables from a `.env` file.
- **nodemon**: For automatic server restarts during development.
- **cors**: For enabling Cross-Origin Resource Sharing, just in case this API will be used with a separated Frontend Environment.

---

## Prerequisites

Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/en/) (LTS version recommended)
- [npm](https://www.npmjs.com/) (comes with Node.js)
- A free [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account.

---

## Installation and Setup

1. **Clone the repository:**
```sh
git clone https://manasyesuarthana/backend-practice-projects
cd blogging-platform-api
```

2. **Install dependencies:**
```sh
npm install
```

3. **Set up environment variables:**
Create a file named `.env` (i already provided a sample) in the `backend` root directory and add the following variables. Since I am a CTF player, I added a flag :)) -- You can change this to whatever string you want.

```ini
#use the name of your database before the '?' (e.g., blogDB)
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/blogDB?retryWrites=true&w=majority
flag="flag{fake_flag}
```

4. **Seed the database (Optional but Recommended):**
To create an initial admin user, run the seed script. Make sure to update the credentials inside `seed.js` first.
```sh
npm run seed
```

5. **Start the server:**
- For development (with automatic restarts):
```sh
npm run dev
```
- For production:
```sh
npm start
```

The server will be running on `http://localhost:3000`.

---

## API Endpoints

All endpoints are prefixed with `/api`.

### Authentication (`/auth`)

| Method | Endpoint         | Description                   | Access  |
| :----- | :--------------- | :---------------------------- | :------ |
| `POST` | `/auth/register` | Registers a new user.         | Public  |
| `POST` | `/auth/login`    | Logs in a user and returns a JWT. | Public  |

**POST `/auth/login`**
- **Request Body:**
```json
{
    "username": "your-username",
    "password": "your-password"
}
```
- **Success Response (200 OK):**
```json
{
    "message": "Login successful.",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Blog Posts (`/blog`)

| Method   | Endpoint     | Description                       | Access      |
| :------- | :----------- | :-------------------------------- | :---------- |
| `GET`    | `/blog`      | Fetches a list of all blog posts. | Public      |
| `GET`    | `/blog/:id`  | Fetches a single blog post by ID. | Public      |
| `POST`   | `/blog`      | Creates a new blog post.          | Admin Only  |
| `PUT`    | `/blog/:id`  | Updates an existing blog post.    | Admin Only  |
| `DELETE` | `/blog/:id`  | Deletes a blog post.              | Admin Only  |

**GET `/blog`**
- This endpoint returns an array of all blog posts.
- You can optionally add a `term` query parameter to filter posts where the `tags` field contains the search term (case-insensitive).

- **Example (Get all posts):**

```sh
curl "http://localhost:3000/api/blog"
```
- **Example (Filter posts with the tag "tech"):**

```sh
curl "http://localhost:3000/api/blog?term=tech"
```

**POST `/blog`** (Requires Bearer Token)
- **Request Body:**
```json
{
    "title": "My New Blog Post",
    "content": "This is the content of the post.",
    "tags": "tech, javascript"
}
```
- **Success Response (201 Created):**
```json
{
    "_id": "64c9c1b1c6d3e3a4b9f2d1e1",
    "title": "My New Blog Post",
    "content": "This is the content of the post.",
    "tags": "tech, javascript",
    "author": "64c9c1a0c6d3e3a4b9f2d1de",
    "createdAt": "2023-08-02T05:39:29.282Z",
    "updatedAt": "2023-08-02T05:39:29.282Z"
}
```

- **Success Response (201 Created):**
```json
{
    "_id": "64c9c1b1c6d3e3a4b9f2d1e1",
    "title": "My New Blog Post",
    "content": "This is the content of the post.",
    "author": "64c9c1a0c6d3e3a4b9f2d1de",
    "createdAt": "2023-08-02T05:39:29.282Z",
    "updatedAt": "2023-08-02T05:39:29.282Z"
}
```

### Admin (`/admin`)

| Method | Endpoint | Description                                       | Access     |
| :----- | :------- | :------------------------------------------------ | :--------- |
| `GET`  | `/admin` | Fetches all blogs and current user data for the dashboard. | Admin Only |

**GET `/admin`** (Requires Bearer Token)
- **Success Response (200 OK):**
```json
{
    "blogs": [
    {
        "_id": "64c9c1b1c6d3e3a4b9f2d1e1",
        "title": "My New Blog Post",
        "author": {
        "_id": "64c9c1a0c6d3e3a4b9f2d1de",
        "username": "admin"
        },
        "createdAt": "2023-08-02T05:39:29.282Z"
    }
    ],
    "flag": "flag{fake_flag}",
    "user": {
    "id": "64c9c1a0c6d3e3a4b9f2d1de",
    "username": "admin",
    "role": "admin"
    }
}

```
