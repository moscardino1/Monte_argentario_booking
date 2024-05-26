# Monte Argentario Beach Booking: A Vercel-Deployed Booking System

This project implements a simple beach booking system for Monte Argentario, Italy, showcasing a basic Flask web application deployed on Vercel.
https://monte-argentario-booking.vercel.app/ 

## Project Structure

- **index.html**: The home page, displaying a map with interactive markers representing various beaches. Each marker shows availability information.
- **booking.html**: The booking form for a specific beach, allowing users to select a date, spot, and time slot.
- **view_bookings.html**: Displays a table of all bookings, showcasing details like beach, date, time, spot, and booked status.
- **base.html**: A base template shared by all pages, defining the navigation bar and common styles.
- **app.py**: The Flask application logic handling routes, database interactions, and booking logic.
- **config.py**: Contains configurations for the Flask application, including database connection settings.

## Key Features

- **Interactive Map**: The home page displays a Leaflet map with markers for various beaches, dynamically fetching and displaying their availability status.
- **Booking Form**: The booking page allows users to select a specific beach, date, spot, and time slot, checking for real-time availability and confirming the booking.
- **Database Integration**: The application utilizes SQLAlchemy to interact with a SQLite database, storing booking information and enabling persistence.
- **Real-Time Availability**: The application fetches availability data dynamically using Flask API endpoints, providing real-time updates.
- **Vercel Deployment**: The project is deployed on Vercel, allowing for easy deployment and hosting of the web application.

## How it Works

1. **User Interaction**: Users interact with the home page map, clicking on markers to view beach availability information and booking details.
2. **Booking Form**: Clicking the booking link for a beach opens the booking form. Users choose the desired date, spot, and time slot.
3. **Availability Check**: The application queries the database and checks for available spots using the `api/available_spots` endpoint.
4. **Booking Confirmation**: If a slot is available, the booking is confirmed, and the information is stored in the database.
5. **Bookings View**: Users can access the `view_bookings` page to see all the bookings made.

## Deployment with Vercel

The project is deployed on Vercel, a popular platform for deploying static websites and serverless functions.

- **Vercel Integration**: The project uses a `vercel.json` file for configuring Vercel deployment, defining build commands and output directories.
- **Deployment Process**: Vercel automatically builds the application, deploys it to its infrastructure, and provides a public URL for access.

## Further Improvements

- **User Authentication**: Implement user registration and login to personalize bookings and manage accounts.
- **Payment Integration**: Add a payment system to allow users to pay for their bookings.
- **User Interface**: Improve the user interface and styling for better visual appeal and user experience.
- **Email Notifications**: Send email notifications to users confirming bookings and reminders.
- **Mobile Responsiveness**: Make the application responsive to mobile devices.

This project serves as a foundational example of a simple beach booking system. It demonstrates the use of Flask, database integration, real-time data fetching, and deployment on Vercel. You can further expand upon this project to create a more robust and feature-rich booking system.
