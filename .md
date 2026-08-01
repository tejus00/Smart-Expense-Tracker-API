# Personal Expense Tracker REST API

## Overview

A Flask-based REST API to manage personal expenses.

### Features

- Add Expense
- View All Expenses
- Search Expense by ID
- Filter Expenses by Category
- Calculate Total Expenses
- Group Expenses by Category
- Delete Expense
- Web Interface

## Tech Stack

- Python 3
- Flask
- HTML
- CSS
- JavaScript
- JSON File Storage

## Installation


Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## Run Server

```bash
cd src
python app.py
```

Server runs at

```
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home Page |
| POST | /expenses | Add Expense |
| GET | /expenses | View All Expenses |
| GET | /expenses/<id> | Search by ID |
| GET | /expenses/category/<category> | Search by Category |
| GET | /expenses/total | Total Expenses |
| GET | /expenses/group | Group by Category |
| DELETE | /expenses/<id> | Delete Expense |

## Running Tests

```bash
pytest
```
