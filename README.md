# My Stocks

Organize and monitorate your stocks.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Celery
- Redis

### Installation

1. Clone the repository:

```bash
git clone git@github.com:arraisgbr/my-stocks-app.git
```

2. Create virtual environment and activate it

```bash
python3 -m venv venv
. venv/bin/activate
```

3. Install the project dependencies

```bash
pip install -r requirements.txt
```

4. Copy the .env-example to a .env file and adapt it with
   
```bash
cp .env-example .env
```
   
## Usage

1. Create/Update the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Execute the server

```bash
python manage.py runserver
```

3. Execute redis and celery

```bash
redis-server
celery -A my_stocks_app.celery worker
celery -A my_stocks_app.celery beat
```

## Features

- Create your account
- Create a stock
- Update a stock
- Delete a stock
- See the price history of your stocks
- Receive an email if any of your stocks go out of range previously defined
- Create a wallet
- Delete a wallet
- Associate stocks to wallets
- See other user's wallets

## License
This project is licensed under the MIT License.

## Acknowledgments
Project developed in a weekend to learn Django.
