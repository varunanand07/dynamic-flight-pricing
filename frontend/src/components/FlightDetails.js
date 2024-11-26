// frontend/src/components/FlightDetails.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const FlightDetails = () => {
    const { flightId } = useParams();
    const [flight, setFlight] = useState(null);

    useEffect(() => {
        fetchFlightDetails();
    }, []);

    const fetchFlightDetails = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/api/flight/${flightId}`);
            setFlight(response.data);
        } catch (error) {
            console.error("Error fetching flight details:", error);
        }
    };

    if (!flight) return <div>Loading...</div>;

    return (
        <div>
            <h2>Flight Details</h2>
            <p><strong>Flight ID:</strong> {flight.flight_id}</p>
            <p><strong>Origin:</strong> {flight.origin}</p>
            <p><strong>Destination:</strong> {flight.destination}</p>
            <p><strong>Departure Time:</strong> {new Date(flight.departure_time).toLocaleString()}</p>
            <p><strong>Predicted Price (€):</strong> {flight.predicted_price.toFixed(2)}</p>
        </div>
    );
};

export default FlightDetails;
