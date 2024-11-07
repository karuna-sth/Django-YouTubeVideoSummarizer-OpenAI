# YouTube Video Summarizer

A Django REST Framework application that summarizes YouTube videos using OpenAI's API for text summaries and AssemblyAI for speech-to-text conversion. The application also includes functionality to download audio from YouTube videos using `pytubefix`.

## Features

- **Video Summarization**: Summarizes the content of YouTube videos.
- **Speech to Text**: Converts video audio to text using AssemblyAI.
- **Audio Downloading**: Downloads audio from YouTube videos using `pytubefix`.
- **PostgreSQL Database**: Stores data and summaries.
- **Environment Variables**: Configurable API keys through a `.env` file.
- **Version Management**: Managed with Poetry.

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL

### Steps

1. **Clone the repository**:

   ```
   git clone https://github.com/yourusername/youtube-video-summarizer.git
   cd youtube-video-summarizer
   ```

2. **Install Poetry**:
    ```
    curl -sSL https://install.python-poetry.org | python3 - 
    ```

3. **Install dependencies:**
    ```
    poetry install
    ```

4. **Set up your `.env` file**:
    ```
    ASSEMBLY_API_KEY=your_assemblyai_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Update your `settings.py` file in the Django project**
    ```
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'VideoSummarizer',
                'USER': 'YourUsername',
                'PASSWORD': 'YourPassword',
                'HOST': 'localhost',
            }
        }
    ```

6. **Run migrations:**
    ```
    poetry run python manage.py migrate
    ```

7. **Run the development server:**
    ```
    poetry run python manage.py runserver 0.0.0.0:8000
    ```

8. Navigate to `localhost:8000/swagger`

## API Endpoints

### Summary Endpoints

- **Create Summary**: `POST /summarizer/create/` - Creates a summary for a specified YouTube video.
  
- **List Summaries**: `GET /summarizer/list/` - Retrieves a list of all created summaries.

- **Summary Detail**: `GET /summarizer/<std:uuid>/detail/` - Retrieves details of a specific summary by ID.

- **Delete Summary**: `DELETE /summarizer/<std:uuid>/delete/` - Deletes a specified summary by ID.

### Swagger Documentation

- **Swagger UI**: Access interactive API documentation at `/swagger/`.

- **ReDoc UI**: Access alternative API documentation at `/redoc/`.
