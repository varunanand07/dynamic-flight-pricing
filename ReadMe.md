# Dynamic Flight Pricing Engine for Ryanair

## Description

In the highly competitive aviation industry, dynamic pricing plays a crucial role in maximizing revenue and optimizing seat occupancy. This project aims to provide real-time insights into flight pricing strategies for Ryanair by leveraging machine learning, data visualization, and responsive web design. The dashboard enables stakeholders to monitor, analyze, and make informed decisions based on predictive pricing models and comprehensive data analytics.

The Dynamic Flight Pricing Engine is a full-stack application comprising a Flask backend and a React frontend. The system integrates a machine learning model to predict flight prices, a robust database for data storage and retrieval, and an interactive frontend for data visualization and user interaction. The application simulates real-time flight bookings and competitor pricing data to ensure the machine learning model remains accurate and relevant.

## Objectives

- **Real-Time Price Prediction:** Develop a machine learning model to predict flight prices based on various features such as origin, destination, departure time, bookings, and competitor prices.
- **Interactive Dashboard:** Create a user-friendly frontend that visualizes flight data through charts, tables, and summary cards, allowing users to monitor pricing trends and make data-driven decisions.
- **Data Simulation and Management:** Implement scripts to simulate real-time flight bookings and competitor pricing data, ensuring the model is trained on up-to-date and relevant information.
- **Responsive Design:** Ensure the dashboard is accessible and visually appealing across various devices and screen sizes.
- **Scalability and Maintainability:** Design the system architecture to support future enhancements, scalability, and ease of maintenance.

## Key Features

- **Machine Learning Integration:** Utilizes a predictive model to forecast flight prices dynamically.
- **Comprehensive Data Visualization:** Interactive charts and tables provide clear insights into pricing trends and patterns.
- **Real-Time Data Simulation:** Simulates live flight bookings and competitor pricing to maintain model accuracy.
- **Responsive User Interface:** Ensures optimal user experience across desktops, tablets, and mobile devices.
- **Robust Backend Architecture:** Efficient data handling and API management using Flask and PostgreSQL.

## Technologies Used

### Backend

- **Flask**
- **Flask-CORS**
- **SQLAlchemy**
- **PostgreSQL**
- **Joblib**
- **Scikit-learn**
- **Pandas**

### Frontend

- **React**
- **Material-UI (MUI)**
- **Recharts**
- **React Router**

### Others

- **Git**
- **Node.js & npm**

## Skills

- **Flask**
- **React.js**
- **Pandas**
- **Machine Learning**
- **PostgreSQL**
- **Python (Programming Language)**
- **JavaScript**
- **Git**

## Getting Started

### Prerequisites

- **Backend:**
  - Python 3.x
  - Flask
  - PostgreSQL

- **Frontend:**
  - Node.js and npm

### How to run this project

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/dynamic-flight-pricing-engine.git
    cd dynamic-flight-pricing-engine
    ```

2. **Setup Backend**
    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

    - **Configure Database:**
      Ensure PostgreSQL is installed and running. Create a database for the project and update the database URI in the configuration file.

3. **Setup Frontend**
    ```bash
    cd ../frontend
    npm install
    ```

### Running the Application

1. **Start the Backend Server**
    ```bash
    cd backend
    flask run
    ```

2. **Start the Frontend Server**
    ```bash
    cd ../frontend
    npm start
    ```

    The application should now be accessible at `http://localhost:3000`.

### Testing

- **Backend Tests:**
    ```bash
    cd backend
    pytest
    ```

- **Frontend Tests:**
    ```bash
    cd frontend
    npm test
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

