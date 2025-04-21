# Social Media Data API

This API provides a backend service for connecting a MySQL database to a dashboard built with Next.js. It is designed to aggregate and serve data from various social media platforms, making it easy to build analytics and reporting dashboards.

## Features

- **FastAPI Backend**: High-performance Python API using FastAPI.
- **MySQL Integration**: Stores and retrieves data from a MySQL database.
- **Social Media Services**: Pulls and aggregates data from multiple social media APIs (e.g., Twitter, Facebook, Instagram, etc.).
- **Data Models**: Well-structured models for platforms, clients, people, posts, campaigns, and more.
- **Dashboard Ready**: Designed to serve data to a Next.js frontend dashboard.

## Project Structure

```
/app
  main.py         # FastAPI app entrypoint
  models.py       # Data models (Pydantic & SQLModel)
  ...             # Additional service and route files
/README.md
```

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL server
- Node.js (for Next.js dashboard)
- [Poetry](https://python-poetry.org/) or `pip` for Python dependencies

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/social-media-data-api.git
    cd social-media-data-api
    ```

2. **Install Python dependencies**

    ```bash
    pip install -r requirements.txt
    # or with Poetry
    poetry install
    ```

3. **Configure environment variables**

    Create a `.env` file with your MySQL credentials and any API keys needed for social media services.

    ```
    MYSQL_HOST=localhost
    MYSQL_USER=youruser
    MYSQL_PASSWORD=yourpassword
    MYSQL_DB=yourdatabase
    # Add social media API keys as needed
    ```

4. **Run database migrations** (if applicable)

    ```bash
    # Example using Alembic or SQLModel's migration tools
    alembic upgrade head
    ```

5. **Start the FastAPI server**

    ```bash
    uvicorn app.main:app --reload
    ```

6. **(Optional) Start the Next.js dashboard**

    Follow the instructions in your dashboard project to connect it to this API.

## API Endpoints

- `GET /` — Health check endpoint.
- Additional endpoints for fetching social media data, clients, campaigns, posts, etc.

## Extending the API

- Add new services in `/app/services/` to connect to more social media platforms.
- Define new models in `/app/models.py` as needed.
- Add new API routes in `/app/` for new features.

## License

MIT License

---

**Note:** This project is a backend service only. The Next.js dashboard should be developed separately and configured to consume this API.# API
