# Translation Hub

Translation Hub is a FastAPI-based web application for managing translation jobs.

## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/joaosferreira/translation-hub.git
    cd translation-hub
    ```

2. Install Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the application

Start the web server:

```bash
cd app
uvicorn app.main:app --reload
```

The application will be available at http://127.0.0.1:8000. You can explore the API using the interactive documentation at http://127.0.0.1:8000/docs.

## API Endpoints

- GET /: Root endpoint.
- GET /docs: Interactive API documentation.
- GET /redoc: API documentation with a different style.

Job Endpoints

- POST /jobs/: Create a new translation job.
- GET /jobs/: Get a list of translation jobs.
- GET /jobs/{job_id}: Get details of a specific job by ID.