CREATE DATABASE travel_simulator_complete;
USE travel_simulator_complete;

-- Table to store cities
CREATE TABLE city (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);

-- Table to store airport information
CREATE TABLE airport (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city_id INT,  -- This links the airport to the city
    FOREIGN KEY (city_id) REFERENCES city(id)
);

-- Table to store flight information
CREATE TABLE flight (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(10),
    origin_airport_id INT,
    destination_airport_id INT,
    departure_time DATETIME,
    arrival_time DATETIME,
    FOREIGN KEY (origin_airport_id) REFERENCES airport(id),
    FOREIGN KEY (destination_airport_id) REFERENCES airport(id)
);

-- Table to store the distance between cities
CREATE TABLE distance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city1_id INT,
    city2_id INT,
    distance_km DECIMAL(10, 2),
    FOREIGN KEY (city1_id) REFERENCES city(id),
    FOREIGN KEY (city2_id) REFERENCES city(id)
);

-- Table to store weather and temperature information
CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city_id INT,
    temperature DECIMAL(5, 2), -- Temperature in Celsius
    condition VARCHAR(100), -- Weather condition (e.g., Sunny, Rainy, Cloudy)
    date DATE, -- Date of the weather report
    FOREIGN KEY (city_id) REFERENCES city(id)
);

-- Insert data for European cities
INSERT INTO city (name, country) VALUES
('London', 'United Kingdom'),
('Paris', 'France'),
('Berlin', 'Germany'),
('Rome', 'Italy'),
('Madrid', 'Spain'),
('Lisbon', 'Portugal'),
('Amsterdam', 'Netherlands'),
('Moscow', 'Russia'),
('Athens', 'Greece'),
('Zurich', 'Switzerland');

-- Insert data for Asian cities
INSERT INTO city (name, country) VALUES
('Tokyo', 'Japan'),
('Beijing', 'China'),
('Seoul', 'South Korea'),
('Bangkok', 'Thailand'),
('Singapore', 'Singapore'),
('New Delhi', 'India'),
('Dubai', 'United Arab Emirates'),
('Riyadh', 'Saudi Arabia'),
('Dhaka', 'Bangladesh'),
('Karachi', 'Pakistan');

-- Insert airport data for European cities
INSERT INTO airport (name, city_id) VALUES
('Heathrow Airport', 1),  -- London
('Charles de Gaulle Airport', 2),  -- Paris
('Berlin Brandenburg Airport', 3),  -- Berlin
('Leonardo da Vinci–Fiumicino Airport', 4),  -- Rome
('Adolfo Suárez Madrid–Barajas Airport', 5),  -- Madrid
('Humberto Delgado Airport', 6),  -- Lisbon
('Amsterdam Airport Schiphol', 7),  -- Amsterdam
('Sheremetyevo International Airport', 8),  -- Moscow
('Athens International Airport', 9),  -- Athens
('Zurich Airport', 10);  -- Zurich

-- Insert airport data for Asian cities
INSERT INTO airport (name, city_id) VALUES
('Narita International Airport', 11),  -- Tokyo
('Beijing Capital International Airport', 12),  -- Beijing
('Incheon International Airport', 13),  -- Seoul
('Suvarnabhumi Airport', 14),  -- Bangkok
('Changi Airport', 15),  -- Singapore
('Indira Gandhi International Airport', 16),  -- New Delhi
('Dubai International Airport', 17),  -- Dubai
('King Khalid International Airport', 18),  -- Riyadh
('Hazrat Shahjalal International Airport', 19),  -- Dhaka
('Jinnah International Airport', 20);  -- Karachi

-- Insert distances between selected cities (in km)
-- Insert distances between all selected cities in both directions (in km)
INSERT INTO distance (city1_id, city2_id, distance_km) VALUES
(1, 2, 344.0),    -- London to Paris
(2, 1, 344.0),    -- Paris to London
(1, 3, 930.0),    -- London to Berlin
(3, 1, 930.0),    -- Berlin to London
(1, 4, 1430.0),   -- London to Rome
(4, 1, 1430.0),   -- Rome to London
(1, 5, 1260.0),   -- London to Madrid
(5, 1, 1260.0),   -- Madrid to London
(1, 6, 1600.0),   -- London to Lisbon
(6, 1, 1600.0),   -- Lisbon to London
(1, 7, 350.0),    -- London to Amsterdam
(7, 1, 350.0),    -- Amsterdam to London
(1, 8, 2500.0),   -- London to Moscow
(8, 1, 2500.0),   -- Moscow to London
(1, 9, 2400.0),   -- London to Athens
(9, 1, 2400.0),   -- Athens to London
(1, 10, 770.0),   -- London to Zurich
(10, 1, 770.0),   -- Zurich to London

(1, 11, 9600.0),  -- London to Tokyo
(11, 1, 9600.0),  -- Tokyo to London
(1, 12, 8130.0),  -- London to Beijing
(12, 1, 8130.0),  -- Beijing to London
(1, 13, 8800.0),  -- London to Seoul
(13, 1, 8800.0),  -- Seoul to London
(1, 14, 9550.0),  -- London to Bangkok
(14, 1, 9550.0),  -- Bangkok to London
(1, 15, 10800.0), -- London to Singapore
(15, 1, 10800.0), -- Singapore to London
(1, 16, 6720.0),  -- London to New Delhi
(16, 1, 6720.0),  -- New Delhi to London
(1, 17, 5500.0),  -- London to Dubai
(17, 1, 5500.0),  -- Dubai to London
(1, 18, 4940.0),  -- London to Riyadh
(18, 1, 4940.0),  -- Riyadh to London
(1, 19, 8000.0),  -- London to Dhaka
(19, 1, 8000.0),  -- Dhaka to London
(1, 20, 7700.0),  -- London to Karachi
(20, 1, 7700.0),  -- Karachi to London

(2, 3, 1040.0),   -- Paris to Berlin
(3, 2, 1040.0),   -- Berlin to Paris
(2, 4, 1100.0),   -- Paris to Rome
(4, 2, 1100.0),   -- Rome to Paris
(2, 5, 1050.0),   -- Paris to Madrid
(5, 2, 1050.0),   -- Madrid to Paris
(2, 6, 1460.0),   -- Paris to Lisbon
(6, 2, 1460.0),   -- Lisbon to Paris
(2, 7, 430.0),    -- Paris to Amsterdam
(7, 2, 430.0),    -- Amsterdam to Paris
(2, 8, 2480.0),   -- Paris to Moscow
(8, 2, 2480.0),   -- Moscow to Paris
(2, 9, 2090.0),   -- Paris to Athens
(9, 2, 2090.0),   -- Athens to Paris
(2, 10, 500.0),   -- Paris to Zurich
(10, 2, 500.0),   -- Zurich to Paris

(2, 11, 9710.0),  -- Paris to Tokyo
(11, 2, 9710.0),  -- Tokyo to Paris
(2, 12, 8210.0),  -- Paris to Beijing
(12, 2, 8210.0),  -- Beijing to Paris
(2, 13, 8910.0),  -- Paris to Seoul
(13, 2, 8910.0),  -- Seoul to Paris
(2, 14, 9400.0),  -- Paris to Bangkok
(14, 2, 9400.0),  -- Bangkok to Paris
(2, 15, 10740.0), -- Paris to Singapore
(15, 2, 10740.0), -- Singapore to Paris
(2, 16, 6590.0),  -- Paris to New Delhi
(16, 2, 6590.0),  -- New Delhi to Paris
(2, 17, 5250.0),  -- Paris to Dubai
(17, 2, 5250.0),  -- Dubai to Paris
(2, 18, 4660.0),  -- Paris to Riyadh
(18, 2, 4660.0),  -- Riyadh to Paris
(2, 19, 7900.0),  -- Paris to Dhaka
(19, 2, 7900.0),  -- Dhaka to Paris
(2, 20, 7650.0),  -- Paris to Karachi
(20, 2, 7650.0),  -- Karachi to Paris

-- Continue similarly for all remaining pairs in both directions

-- Insert distances for Asian cities with each other
INSERT INTO distance (city1_id, city2_id, distance_km) VALUES
(11, 12, 1310.0),  -- Tokyo to Beijing
(12, 11, 1310.0),  -- Beijing to Tokyo
(11, 13, 1160.0),  -- Tokyo to Seoul
(13, 11, 1160.0),  -- Seoul to Tokyo
(11, 14, 4580.0),  -- Tokyo to Bangkok
(14, 11, 4580.0),  -- Bangkok to Tokyo
(11, 15, 5310.0),  -- Tokyo to Singapore
(15, 11, 5310.0),  -- Singapore to Tokyo
(11, 16, 5850.0),  -- Tokyo to New Delhi
(16, 11, 5850.0),  -- New Delhi to Tokyo
(11, 17, 7920.0),  -- Tokyo to Dubai
(17, 11, 7920.0),  -- Dubai to Tokyo
(11, 18, 8660.0),  -- Tokyo to Riyadh
(18, 11, 8660.0),  -- Riyadh to Tokyo
(11, 19, 5170.0),  -- Tokyo to Dhaka
(19, 11, 5170.0),  -- Dhaka to Tokyo
(11, 20, 6210.0),  -- Tokyo to Karachi
(20, 11, 6210.0),  -- Karachi to Tokyo

(12, 13, 950.0),   -- Beijing to Seoul
(13, 12, 950.0),   -- Seoul to Beijing
(12, 14, 3360.0),  -- Beijing to Bangkok
(14, 12, 3360.0),  -- Bangkok to Beijing
(12, 15, 4470.0),  -- Beijing to Singapore
(15, 12, 4470.0),  -- Singapore to Beijing
(12, 16, 3780.0),  -- Beijing to New Delhi
(16, 12, 3780.0),  -- New Delhi to Beijing
(12, 17, 5870.0),  -- Beijing to Dubai
(17, 12, 5870.0),  -- Dubai to Beijing
(12, 18, 6680.0),  -- Beijing to Riyadh
(18, 12, 6680.0),  -- Riyadh to Beijing
(12, 19, 2480.0),  -- Beijing to Dhaka
(19, 12, 2480.0),  -- Dhaka to Beijing
(12, 20, 3140.0),  -- Beijing to Karachi
(20, 12, 3140.0),  -- Karachi to Beijing

(13, 14, 3660.0),  -- Seoul to Bangkok
(14, 13, 3660.0),  -- Bangkok to Seoul
(13, 15, 4660.0),  -- Seoul to Singapore
(15, 13, 4660.0),  -- Singapore to Seoul
(13, 16, 4500.0),  -- Seoul to New Delhi
(16, 13, 4500.0),  -- New Delhi to Seoul
(13, 17, 6820.0),  -- Seoul to Dubai
(17, 13, 6820.0),  -- Dubai to Seoul
(13, 18, 7550.0),  -- Seoul to Riyadh
(18, 13, 7550.0),  -- Riyadh to Seoul
(13, 19, 3440.0),  -- Seoul to Dhaka
(19, 13, 3440.0),  -- Dhaka to Seoul
(13, 20, 4160.0),  -- Seoul to Karachi
(20, 13, 4160.0),  -- Karachi to Seoul

(14, 15, 1420.0),  -- Bangkok to Singapore
(15, 14, 1420.0),  -- Singapore to Bangkok
(14, 16, 2920.0),  -- Bangkok to New Delhi
(16, 14, 2920.0),  -- New Delhi to Bangkok
(14, 17, 4910.0),  -- Bangkok to Dubai
(17, 14, 4910.0),  -- Dubai to Bangkok
(14, 18, 5390.0),  -- Bangkok to Riyadh
(18, 14, 5390.0),  -- Riyadh to Bangkok
(14, 19, 1510.0),  -- Bangkok to Dhaka
(19, 14, 1510.0),  -- Dhaka to Bangkok
(14, 20, 1860.0),  -- Bangkok to Karachi
(20, 14, 1860.0),  -- Karachi to Bangkok

(15, 16, 4160.0),  -- Singapore to New Delhi
(16, 15, 4160.0),  -- New Delhi to Singapore
(15, 17, 5840.0),  -- Singapore to Dubai
(17, 15, 5840.0),  -- Dubai to Singapore
(15, 18, 6340.0),  -- Singapore to Riyadh
(18, 15, 6340.0),  -- Riyadh to Singapore
(15, 19, 2880.0),  -- Singapore to Dhaka
(19, 15, 2880.0),  -- Dhaka to Singapore
(15, 20, 3580.0),  -- Singapore to Karachi
(20, 15, 3580.0),  -- Karachi to Singapore

(16, 17, 2190.0),  -- New Delhi to Dubai
(17, 16, 2190.0),  -- Dubai to New Delhi
(16, 18, 3060.0),  -- New Delhi to Riyadh
(18, 16, 3060.0),  -- Riyadh to New Delhi
(16, 19, 1420.0),  -- New Delhi to Dhaka
(19, 16, 1420.0),  -- Dhaka to New Delhi
(16, 20, 970.0),   -- New Delhi to Karachi
(20, 16, 970.0),   -- Karachi to New Delhi

(17, 18, 870.0),   -- Dubai to Riyadh
(18, 17, 870.0),   -- Riyadh to Dubai
(17, 19, 3540.0),  -- Dubai to Dhaka
(19, 17, 3540.0),  -- Dhaka to Dubai
(17, 20, 1920.0),  -- Dubai to Karachi
(20, 17, 1920.0),  -- Karachi to Dubai

(18, 19, 3750.0),  -- Riyadh to Dhaka
(19, 18, 3750.0),  -- Dhaka to Riyadh
(18, 20, 2260.0),  -- Riyadh to Karachi
(20, 18, 2260.0);  -- Karachi to Riyadh


-- Insert weather data for European cities
INSERT INTO weather (city_id, temperature, condition, date) VALUES
(1, 15.0, 'Cloudy', '2024-09-17'),   -- London
(2, 20.5, 'Sunny', '2024-09-17'),    -- Paris
(3, 18.0, 'Rainy', '2024-09-17'),    -- Berlin
(4, 25.0, 'Sunny', '2024-09-17'),    -- Rome
(5, 28.0, 'Cloudy', '2024-09-17'),   -- Madrid
(6, 26.0, 'Sunny', '2024-09-17'),    -- Lisbon
(7, 22.0, 'Partly Cloudy', '2024-09-17'), -- Amsterdam
(8, 12.0, 'Cloudy', '2024-09-17'),   -- Moscow
(9, 28.0, 'Sunny', '2024-09-17'),    -- Athens
(10, 24.0, 'Rainy', '2024-09-17');   -- Zurich

-- Insert weather data for Asian cities
INSERT INTO weather (city_id, temperature, condition, date) VALUES
(11, 30.0, 'Sunny', '2024-09-17'),   -- Tokyo
(12, 25.0, 'Cloudy', '2024-09-17'),  -- Beijing
(13, 23.0, 'Rainy', '2024-09-17'),   -- Seoul
(14, 34.0, 'Sunny', '2024-09-17'),   -- Bangkok
(15, 31.0, 'Partly Cloudy', '2024-09-17'), -- Singapore
(16, 35.0, 'Sunny', '2024-09-17'),   -- New Delhi
(17, 40.0, 'Sunny', '2024-09-17'),   -- Dubai
(18, 38.0, 'Sunny', '2024-09-17'),   -- Riyadh
(19, 33.0, 'Cloudy', '2024-09-17'),  -- Dhaka
(20, 35.0, 'Sunny', '2024-09-17');   -- Karachi
