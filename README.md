# Weather Data Pipeline - Venezuela

This project is a foundational data engineering pipeline designed to extract, transform, and load (ETL) weather data for a specified city in Venezuela (defaulting to Caracas). It leverages Docker and Docker Compose for environment management, ensuring reproducibility and easy setup.

**Current Stage:** **Extract (E)** - The pipeline is currently configured to fetch weather forecast data from [WeatherAPI.com](https://www.weatherapi.com/).

---

## Table of Contents

* [Features (Current)](#features-current)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
    * [1. Clone the Repository](#1-clone-the-repository)
    * [2. Obtain Your WeatherAPI.com API Key](#2-obtain-your-weatherapicom-api-key)
    * [3. Configure Environment Variables in .env](#3-configure-environment-variables-in-env)
    * [4. Run the Pipeline with Docker Compose](#4-run-the-pipeline-with-docker-compose)
* [Project Structure (Relevant Files)](#project-structure-relevant-files)
* [Next Steps](#next-steps)

---

## Features (Current)

* **Containerized Environment:** Uses Docker and Docker Compose for a consistent and isolated development/execution environment.
* **API Data Extraction:** Connects to the WeatherAPI.com forecast endpoint to retrieve up-to-date weather information.
* **Secure Configuration:** Utilizes `.env` files to manage sensitive API keys and configurable parameters, keeping them out of source control.

---

## Prerequisites

Before running this project, ensure you have the following installed on your system:

* **[Docker Desktop](https://www.docker.com/products/docker-desktop)** (includes Docker Engine and Docker Compose)

---

## Getting Started

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

First, clone this GitHub repository to your local machine:

```bash
git clone https://github.com/osmarbetancourt/weather-pipeline-vzla.git
cd weather-pipeline-vzla
```

### 2. Obtain Your WeatherAPI.com API Key

To fetch weather data, you'll need a free API key from WeatherAPI.com:

1.  Go to [**WeatherAPI.com**](https://www.weatherapi.com/).
2.  Sign up for a free account.
3.  Once registered and logged in, navigate to your **[My Account](https://www.weatherapi.com/my/)** dashboard.
4.  Your default API key should be visible there. **Copy this key.**

### 3. Configure Environment Variables in `.env`

For security reasons, sensitive information like API keys are stored in a `.env` file, which is kept out of version control (`.gitignore` prevents it from being committed).

1.  In the **root directory** of your cloned project (the `weather-pipeline-vzla/` directory, where `docker-compose.yml` is located), create a new file named `.env`:

    ```bash
    touch .env
    ```

2.  Open the newly created `.env` file and add the following lines. **Replace `YOUR_ACTUAL_WEATHERAPI_KEY_HERE` with the API key you obtained in the previous step.**

    ```ini
    WEATHER_API_KEY="YOUR_ACTUAL_WEATHERAPI_KEY_HERE"
    TARGET_CITY="Caracas"
    ```

    * **`WEATHER_API_KEY`**: This variable will hold your unique API key from WeatherAPI.com.
    * **`TARGET_CITY`**: This variable specifies the city for which you want to fetch weather data. You can change `Caracas` to any other city (e.g., `Maracaibo`, `Valencia`). The Python script is currently configured to look for tomorrow's forecast for this city.

### 4. Run the Pipeline with Docker Compose

With your `.env` file configured, you can now run the Python script within its Dockerized environment:

From the root directory of your project, execute the following command:

```bash
docker-compose up --build
```

## Project Structure (Relevant Files)

```
weather-pipeline-vzla/
├── app/
│   ├── init.py       # Marks 'app' as a Python package, enabling module imports.
│   ├── main.py           # The main entry point and orchestrator for the ETL pipeline.
│   ├── extract.py        # Contains functions for extracting raw weather data from the API.
│   ├── transform.py      # Contains functions for transforming and cleaning the extracted data.
│   ├── requirements.txt  # Lists Python dependencies (e.g., requests, pandas).
│   └── Dockerfile        # Defines how to build the Docker image for the Python application.
├── docker-compose.yml      # Orchestrates the Docker services (currently just the app)
├── .env                    # Stores sensitive environment variables (not committed to Git)
├── .gitignore              # Ensures .env is not committed
└── README.md               # This file
```
---