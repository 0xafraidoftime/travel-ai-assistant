#!/usr/bin/env python3
"""
Database setup script for Travel AI Assistant
Creates and populates the travel_info.db SQLite database with sample data
"""

import sqlite3
from datetime import datetime, timedelta

def create_travel_database():
    """Create and populate the travel database with sample data"""
    
    # Connect to the database (creates file if it doesn't exist)
    conn = sqlite3.connect('travel_info.db')
    cursor = conn.cursor()
    
    print("Creating travel_info.db database...")
    
    # Create flights table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number TEXT NOT NULL,
            airline TEXT NOT NULL,
            destination TEXT NOT NULL,
            origin TEXT NOT NULL,
            date TEXT NOT NULL,
            departure_time TEXT NOT NULL,
            arrival_time TEXT NOT NULL,
            price REAL,
            available_seats INTEGER
        )
    ''')
    
    # Create bookings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id TEXT PRIMARY KEY,
            flight_number TEXT NOT NULL,
            passenger_name TEXT NOT NULL,
            passenger_email TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            status TEXT DEFAULT 'confirmed',
            FOREIGN KEY (flight_number) REFERENCES flights (flight_number)
        )
    ''')
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            preferences TEXT,
            created_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Sample flight data
    sample_flights = [
        ('AA123', 'American Airlines', 'New York', 'Los Angeles', '2024-09-21', '08:30', '11:45', 299.99, 45),
        ('BA456', 'British Airways', 'London', 'New York', '2024-09-22', '14:20', '17:30', 599.99, 23),
        ('UA789', 'United Airlines', 'Chicago', 'Miami', '2024-09-23', '09:15', '12:45', 189.99, 67),
        ('DL101', 'Delta Airlines', 'Atlanta', 'Seattle', '2024-09-24', '16:00', '18:20', 349.99, 12),
        ('SW202', 'Southwest Airlines', 'Dallas', 'Las Vegas', '2024-09-25', '11:30', '12:45', 129.99, 89),
        ('JB303', 'JetBlue', 'Boston', 'Los Angeles', '2024-09-26', '07:45', '11:15', 279.99, 34),
        ('AA404', 'American Airlines', 'Miami', 'New York', '2024-09-27', '13:10', '16:25', 249.99, 56),
        ('UA505', 'United Airlines', 'San Francisco', 'Chicago', '2024-09-28', '10:00', '15:45', 319.99, 78),
        ('DL606', 'Delta Airlines', 'New York', 'Paris', '2024-09-29', '22:30', '11:45+1', 699.99, 19),
        ('LH707', 'Lufthansa', 'Frankfurt', 'Tokyo', '2024-09-30', '13:25', '08:30+1', 899.99, 8)
    ]
    
    # Insert sample flights
    cursor.executemany('''
        INSERT OR IGNORE INTO flights 
        (flight_number, airline, destination, origin, date, departure_time, arrival_time, price, available_seats)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', sample_flights)
    
    # Sample bookings data
    sample_bookings = [
        ('BK001', 'AA123', 'John Doe', 'john.doe@email.com', '2024-09-15', 'confirmed'),
        ('BK002', 'BA456', 'Jane Smith', 'jane.smith@email.com', '2024-09-16', 'confirmed'),
        ('BK003', 'UA789', 'Bob Johnson', 'bob.johnson@email.com', '2024-09-17', 'cancelled'),
        ('BK004', 'DL101', 'Alice Brown', 'alice.brown@email.com', '2024-09-18', 'confirmed'),
        ('BK005', 'SW202', 'Charlie Wilson', 'charlie.wilson@email.com', '2024-09-19', 'confirmed')
    ]
    
    # Insert sample bookings
    cursor.executemany('''
        INSERT OR IGNORE INTO bookings 
        (booking_id, flight_number, passenger_name, passenger_email, booking_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_bookings)
    
    # Sample users data
    sample_users = [
        ('John Doe', 'john.doe@email.com', '+1-555-0101', 'beach,luxury'),
        ('Jane Smith', 'jane.smith@email.com', '+1-555-0102', 'adventure,budget'),
        ('Bob Johnson', 'bob.johnson@email.com', '+1-555-0103', 'cultural,business'),
        ('Alice Brown', 'alice.brown@email.com', '+1-555-0104', 'family,comfort'),
        ('Charlie Wilson', 'charlie.wilson@email.com', '+1-555-0105', 'solo,backpacking')
    ]
    
    # Insert sample users
    cursor.executemany('''
        INSERT OR IGNORE INTO users 
        (name, email, phone, preferences)
        VALUES (?, ?, ?, ?)
    ''', sample_users)
    
    # Commit changes
    conn.commit()
    
    # Display summary
    cursor.execute("SELECT COUNT(*) FROM flights")
    flight_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM bookings")
    booking_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    
    print(f"Database created successfully!")
    print(f"- {flight_count} flights added")
    print(f"- {booking_count} bookings added")
    print(f"- {user_count} users added")
    
    # Close connection
    conn.close()
    
    return True

def test_database():
    """Test the database by running some sample queries"""
    
    conn = sqlite3.connect('travel_info.db')
    cursor = conn.cursor()
    
    print("\n" + "="*50)
    print("Testing database queries...")
    print("="*50)
    
    # Test 1: Search flights to New York
    print("\n1. Flights to New York:")
    cursor.execute("SELECT flight_number, airline, origin, date, departure_time, price FROM flights WHERE destination = 'New York'")
    results = cursor.fetchall()
    for row in results:
        print(f"   {row[0]} ({row[1]}): {row[2]} -> New York on {row[3]} at {row[4]} - ${row[5]}")
    
    # Test 2: Show all bookings
    print("\n2. Current bookings:")
    cursor.execute("""
        SELECT b.booking_id, b.passenger_name, f.flight_number, f.destination, b.status 
        FROM bookings b 
        JOIN flights f ON b.flight_number = f.flight_number
    """)
    results = cursor.fetchall()
    for row in results:
        print(f"   {row[0]}: {row[1]} -> {row[3]} (Flight {row[2]}) - {row[4]}")
    
    # Test 3: Available flights with seats
    print("\n3. Flights with available seats (>20):")
    cursor.execute("SELECT flight_number, airline, origin, destination, available_seats FROM flights WHERE available_seats > 20")
    results = cursor.fetchall()
    for row in results:
        print(f"   {row[0]} ({row[1]}): {row[2]} -> {row[3]} - {row[4]} seats available")
    
    conn.close()

if __name__ == "__main__":
    # Create the database
    create_travel_database()
    
    # Test the database
    test_database()
    
    print(f"\n{'='*50}")
    print("Setup complete! You can now use travel_info.db with your CAI application.")
    print("The database file 'travel_info.db' has been created in the current directory.")
    print("="*50)