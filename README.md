# Maritano Music Store - QA Automation Testing

## Project Overview

This project demonstrates automated testing of a Music Store web application using Selenium WebDriver and Pytest.

The application is built with Flask and MySQL and allows users to manage music store products through Create, Read, Update, and Delete (CRUD) operations.

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Flask
* MySQL
* Page Object Model (POM)

## Test Scenarios

### Login Testing

* Verify successful login with valid credentials

### Product Testing

* Add Product
* Edit Product
* Delete Product

## Project Structure

```text
pages/
locators/
tests/
templates/
static/
config/
app.py
requirements.txt
```

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Run Automated Tests

```bash
pytest tests -v
```

## Test Results

All automated test cases are passing successfully.

* Login Test
* Add Product Test
* Edit Product Test
* Delete Product Test

## Author

Fakhri Amini
QA Automation Portfolio Project
