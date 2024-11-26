// frontend/src/components/Dashboard.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Bar } from 'react-chartjs-2';

const Dashboard = () => {
    const [flights, setFlights] = useState([]);
    const [chartData, setChartData] = useState({});

    useEffect(() => {
        fetchFlights();
    }, []);

    const fetchFlights = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:5000/api/predict');
            setFlights(response.data);
            prepareChartData(response.data);
        } catch (error) {
            console.error("Error fetching flight data:", error);
        }
    };

    const prepareChartData = (data) => {
        const labels = data.map(flight => `Flight ${flight.flight_id}`);
        const prices = data.map(flight => flight.predicted_price);
        
        setChartData({
            labels: labels,
            datasets: [
                {
                    label: 'Predicted Price (€)',
                    data: prices,
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                }
            ]
        });
    };

    return (
        <div>
            <h2>Dynamic Flight Pricing Dashboard</h2>
            <Bar data={chartData} />
            <table>
                <thead>
                    <tr>
                        <th>Flight ID</th>
                        <th>Origin</th>
                        <th>Destination</th>
                        <th>Departure Time</th>
                        <th>Predicted Price (€)</th>
                    </tr>
                </thead>
                <tbody>
                    {flights.map(flight => (
                        <tr key={flight.flight_id}>
                            <td>{flight.flight_id}</td>
                            <td>{flight.origin}</td>
                            <td>{flight.destination}</td>
                            <td>{new Date(flight.departure_time).toLocaleString()}</td>
                            <td>{flight.predicted_price.toFixed(2)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Dashboard;
