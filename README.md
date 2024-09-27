# Secure File Storage on Cloud Using Hybrid Cryptography

## Project Overview

The Secure File Storage on Cloud Using Hybrid Cryptography project is designed to provide a secure platform for users to store and manage their sensitive files in the cloud. By employing hybrid cryptography techniques, this application ensures that users' data remains confidential, integral, and accessible only to authorized individuals.

## Key Features
Secure File Upload and Download: Users can upload and download files securely, with encryption applied to protect their data.

Hybrid Cryptography: Utilizes a combination of symmetric (e.g., AES) and asymmetric (e.g., RSA) encryption methods to enhance data security.

User Authentication: Ensures that only authenticated users can access and manage their files, preventing unauthorized access.

Cloud Storage Integration: Files are stored in a cloud storage service, enabling scalability and ease of access.

## Tech Stack
## Backend:
Python: The core programming language used for server-side development.

Django: A high-level web framework that facilitates rapid development and clean design.

Database:

SQLite or PostgreSQL: Used for managing user data and file metadata.

Cryptography:

Cryptography Library: Provides tools for implementing secure encryption and decryption processes.

Frontend:

HTML, CSS, JavaScript: Used for creating an intuitive and responsive user interface.

## Deployment:

Cloud Service: The application is hosted on a cloud platform (e.g., AWS, Google Cloud) for enhanced scalability and reliability.

## Installation and Setup

To set up the project locally, follow these steps:

## Clone the Repository:

git clone <repository_url>

cd <repository_directory>

### Create a Virtual Environment:

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### Install Dependencies:

pip install -r requirements.txt

### Run Migrations:

python manage.py migrate

### Start the Development Server:

python manage.py runserver

Access the Application: Open your browser and navigate to http://127.0.0.1:8000/.

## Usage

User Registration: New users can register an account to start using the application.

File Management: After logging in, users can upload, download, and manage their files securely.

Contributing

Contributions are welcome! If you wish to contribute to the project, please follow these steps:

## Fork the repository.

Create a new branch for your feature or bug fix.

Make your changes and commit them.

Push your changes to your fork.

Open a pull request with a clear description of your changes.
