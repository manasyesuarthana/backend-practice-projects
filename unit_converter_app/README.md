# Full-Stack Unit Converter Web Application

This is a full-stack web application for converting between different units of measurement, including length, weight, and temperature. The project features a standalone REST API backend built with Flask and a user-friendly frontend, with containerized deployment using Docker.

---

**NOTE**: I mainly worked on backend logic for the flask REST API as well as Docker containerization. The Frontend is mainly vibecoded :P

## Features

- **Three Conversion Categories**:
- **Length**: millimeters, centimeters, meters, kilometers, inches, feet, yards, miles
- **Weight**: milligrams, grams, kilograms, ounces, pounds
- **Temperature**: Celsius, Fahrenheit, Kelvin
- **User-Friendly Interface**: Clean, intuitive design with tab-based navigation for easy use.
- **RESTful API**: The backend provides a clean, stateless API for all conversion operations.
- **Docker Support**: Fully containerized with Docker and Docker Compose for easy setup and consistent deployment.
- **Real-time Conversion**: Get instant conversion results with built-in error handling.

---

## Technology Stack

### Backend
- **Framework**: Flask
- **API**: RESTful, JSON-based endpoints
- **CORS**: `flask-cors` for frontend-backend communication

### Frontend
- **Core**: HTML, CSS, JavaScript
- **Server**: Flask (for serving the static files and templating)
- **Design**: Responsive for both desktop and mobile devices

### Deployment
- **Containerization**: Docker
- **Orchestration**: Docker Compose

---

## Project Structure

The project is organized into two main services: `backend` and `frontend`, each with its own Dockerfile. A `docker-compose.yml` file at the root orchestrates the two containers.

```
unit_converter_app/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
└── docker-compose.yml
```

---

## API Endpoints

The backend API runs on port `5000`.

-   `POST /convert/length` - Convert length units.
-   `POST /convert/weight` - Convert weight units.
-   `POST /convert/temp` - Convert temperature units.

#### Request Format
```json
{
  "value": "10",
  "initial": "m",
  "final": "ft"
}
```

#### Response Format
```json
{
  "original_value": 10,
  "original_unit": "m",
  "converted_value": 32.8084,
  "converted_unit": "ft"
}
```

---

## Installation and Setup

### Prerequisites
-   Docker and Docker Compose must be installed on your system.

### Method 1: Quick Start with Docker Compose (Recommended)
1.  Navigate to the project root directory.
2.  Run the application using Docker Compose:
```bash
docker-compose up --build
```
3.  Open your browser and navigate to `http://localhost:3000`.

### Method 2: Manual Setup (Without Docker)

#### 1. Backend Setup
```bash
cd backend/
pip3 install -r requirements.txt
python3 main.py
```

The backend will be available at `http://localhost:5000`.

#### 2. Frontend Setup
```bash
cd frontend/
pip3 install -r requirements.txt
python3 app.py
```
The frontend application will be available at `http://localhost:3000`.

---

## Usage

1.  Select the conversion type (**Length**, **Weight**, or **Temperature**) using the tabs.
2.  Enter the value you want to convert in the input field.
3.  Select the unit to convert from.
4.  Select the unit to convert to.
5.  The result will be displayed automatically.

---

## Supported Units

### Length
-   Millimeter (mm)
-   Centimeter (cm)
-   Meter (m)
-   Kilometer (km)
-   Inch (in)
-   Foot (ft)
-   Yard (yd)
-   Mile (mi)

### Weight
-   Milligram (mg)
-   Gram (g)
-   Kilogram (kg)
-   Ounce (oz)
-   Pound (lb)

### Temperature
-   Celsius (°C)
-   Fahrenheit (°F)
-   Kelvin (K)