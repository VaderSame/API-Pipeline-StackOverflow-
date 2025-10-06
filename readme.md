# API Pipeline for StackOverflow Data

## Overview
This project implements a complete end-to-end API pipeline that interacts with StackOverflow data. The system demonstrates core data engineering principles by fetching, storing, and serving data through a RESTful API.

## Features
- Data fetching from StackOverflow API (`/fetch` endpoint)
- Local storage in SQLite database (`questions.db`)
- Data serving through REST endpoint (`/questions`)
- Error handling and rate limiting
- Efficient data caching
- RESTful API design patterns

## System Components
1. **Data Fetching**
    - Endpoint: `/fetch`
    - Pulls real-time data from StackOverflow
    - Handles API rate limiting and pagination
    - Implements error handling and retries
    - Supports configurable data filters

2. **Data Storage**
    - SQLite database (`questions.db`)
    - Relational schema for efficient querying
    - Local persistence of fetched data
    - Automatic schema migrations
    - Data validation and cleaning

3. **Data Serving**
    - Endpoint: `/questions`
    - RESTful API design
    - Serves stored data on demand
    - Supports filtering and pagination
    - JSON response format

## Project Structure
```
api-pipeline/
│
├── src/
│   ├── api/              # API endpoint handlers
│   ├── database/         # Database models and migrations
│   ├── services/         # Business logic and data processing
│   └── utils/            # Helper functions and utilities
│
├── tests/               # Test suites
│
├── config/             # Configuration files
│
└── data/              # Data storage directory
    └── questions.db   # SQLite database file
```

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables in `.env`
4. Initialize database: `python init_db.py`
5. Run the application: `python main.py`

## Usage
```bash
# Fetch new data from StackOverflow
curl localhost:port/fetch

# Retrieve stored questions
curl localhost:port/questions

# Filter questions by tag
curl localhost:port/questions?tag=python

# Paginate results
curl localhost:port/questions?page=1&size=10
```

## Technical Stack
- Database: SQLite
- API Framework: FastAPI
- Data Source: StackOverflow API
- Testing: pytest
- Documentation: Swagger/OpenAPI

## Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License
MIT License