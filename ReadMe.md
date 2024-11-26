# Dynamic Flight Pricing Engine

## Project Overview

A dynamic pricing system that optimizes flight ticket prices in real-time based on various factors such as demand, booking patterns, seasonal trends, and competitor pricing.

## Technologies Used

- **Backend:** Python, Flask
- **Machine Learning:** scikit-learn
- **Database:** PostgreSQL
- **Frontend:** React.js
- **Data Visualization:** Chart.js
- **Deployment:** Docker, AWS

## Features

- **Data Collection:** Simulates real-time booking and competitor pricing data.
- **Pricing Algorithm:** Machine learning model to predict optimal prices.
- **Dashboard:** Interactive frontend to monitor pricing trends.
- **Automation:** Scheduled retraining of the model.
- **Deployment:** Containerized using Docker and deployed on AWS.

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed.
- AWS account (for deployment).

### Running Locally

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/dynamic-flight-pricing.git
    cd dynamic-flight-pricing
    ```

2. **Set Up Backend:**

    ```bash
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python models/train_model.py
    python app.py
    ```

3. **Set Up Frontend:**

    ```bash
    cd ../frontend
    npm install
    npm start
    ```

4. **Access the Application:**

    - Frontend: `http://localhost:3000/`
    - Backend API: `http://localhost:5000/`

## Deployment

Instructions for deploying the application using Docker and AWS.

## Future Enhancements

- Integrate real-world data sources.
- Implement advanced machine learning models.
- Enhance security and scalability.
