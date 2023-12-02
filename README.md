# Vendor Management System

## Overview
The Vendor Management System is a Django-based application designed to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
- [Core Features](#core-features)
  - [1. Vendor Profile Management](#1-vendor-profile-management)
  - [2. Purchase Order Tracking](#2-purchase-order-tracking)
  - [3. Vendor Performance Evaluation](#3-vendor-performance-evaluation)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SaurabhVishwakarma826/VendorManagementSystem.git

2. Navigate to the project directory:
    ```bash
   cd vendor-management-system
   
3. Create and activate a virtual environment:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install dependencies:

    ```bash
   pip install -r requirements.txt

5. Apply database migrations:
    ```bash
   python manage.py makemigrations
   python manage.py migrate

6. Create a superuser (for accessing the Django admin panel):
    ```bash
   python manage.py createsuperuser

7. Run the development server:
    ```bash
   python manage.py runserver

## Usage

### API Endpoints
- Vendor Management: **/api/vendors/**
- Purchase Order Tracking: **/api/purchase_orders/**
- Vendor Performance: **/api/vendors/{vendor_id}/performance/**
- Acknowledge Purchase Order: **/api/purchase_orders/{po_id}/acknowledge/**

### Authentication
Token-based authentication is used. Obtain a token by making a POST request to **/api-token-auth/** with your credentials.

## Core Features
### 1. Vendor Profile Management
- Create a new vendor: **POST /api/vendors/**
- List all vendors: **GET /api/vendors/**
- Retrieve a specific vendor's details: **GET /api/vendors/{vendor_id}/**
- Update a vendor's details: **PUT /api/vendors/{vendor_id}/**
- Delete a vendor: **DELETE /api/vendors/{vendor_id}/**

### 2. Purchase Order Tracking
- Create a new purchase order: **POST /api/purchase_orders/**
- List all purchase orders: **GET /api/purchase_orders/**
- Retrieve details of a specific purchase order: **GET /api/purchase_orders/{po_id}/**
- Update a purchase order: **PUT /api/purchase_orders/{po_id}/**
- Delete a purchase order: **DELETE /api/purchase_orders/{po_id}/**

### 3. Vendor Performance Evaluation

Retrieve a vendor's performance metrics: **GET /api/vendors/{vendor_id}/performance/**


## Contributing
Feel free to contribute to the project by opening issues or creating pull requests.

## License
This project is licensed under the Saurabh Vishwakarma










