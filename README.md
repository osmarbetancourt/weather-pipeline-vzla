# Weather Data Pipeline - Venezuela

A complete ETL (Extract, Transform, Load) pipeline focused on forecasted weather data. This project leverages Python to fetch hourly weather predictions (from [WeatherAPI.com](https://www.weatherapi.com/)) for a target city (like Caracas, Venezuela) from an external API, processes the raw data, and efficiently stores it within a Dockerized PostgreSQL database, making the data readily available for analysis.

---

## Table of Contents

* [Features](#features-current)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
    * [1. Clone the Repository](#1-clone-the-repository)
    * [2. Obtain Your WeatherAPI.com API Key](#2-obtain-your-weatherapicom-api-key)
    * [3. Configure Environment Variables in .env](#3-configure-environment-variables-in-env)
    * [4. Run the Pipeline with Docker Compose](#4-run-the-pipeline-with-docker-compose)
* [Project Structure (Relevant Files)](#project-structure-relevant-files)
* [Business Intelligence & Data Visualization (Metabase)](#business-intelligence--data-visualization-metabase)
    * [1. Average Hourly Temperature Cycle](#1-average-hourly-temperature-cycle)
    * [2. Average Daily Humidity](#2-average-daily-humidity)
    * [3. Daily Weather Averages Overview](#3-daily-weather-averages-overview)
    * [Comprehensive Weather Dashboard](#comprehensive-weather-dashboard)
* [Next Steps](#next-steps)

---

## Features

* **Containerized Environment:** Leverages Docker and Docker Compose for a consistent, isolated, and easily reproducible development and execution environment.
* **Targeted Hourly Forecasts:** Connects to the WeatherAPI.com forecast endpoint to extract detailed hourly weather information for specific cities.
* **Automated Data Transformation:** Processes and cleans raw API responses into a structured, tabular format suitable for database storage.
* **PostgreSQL Data Loading:** Efficiently loads transformed data into a PostgreSQL database using SQLAlchemy and Pandas, including built-in retry mechanisms to ensure successful connections even if the database isn't immediately available on startup.
* **Secure Configuration:** Utilizes `.env` files to manage sensitive API keys and configurable parameters, keeping them secure and out of version control.

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
    FORECAST_DAYS=8

    # PostgreSQL Database Configuration
    PG_DB="weather_db"
    PG_USER="db_user"
    PG_PASSWORD="db_pass"
    ```

* **`WEATHER_API_KEY`**: This variable will hold your unique API key from WeatherAPI.com.
* **`TARGET_CITY`**: This variable specifies the city for which you want to fetch weather data. You can change `Caracas` to any other city (e.g., `Maracaibo`, `Valencia`).
* **`FORECAST_DAYS`**: Defines how many days of future forecast data to retrieve (e.g., `1` for tomorrow's forecast).
* **`PG_DB`**: The name of the database to connect to.
* **`PG_USER`**: The username for connecting to the database.
* **`PG_PASSWORD`**: The password for the database user.

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
│   ├── __init__.py       # Marks 'app' as a Python package, enabling module imports.
│   ├── main.py           # The main entry point and orchestrator for the ETL pipeline.
│   ├── extract.py        # Contains functions for extracting raw weather data from the API.
│   ├── transform.py      # Contains functions for transforming and cleaning the extracted data.
│   ├── load.py           # Handles database connection, table creation, and data loading into PostgreSQL.
│   ├── requirements.txt  # Lists Python dependencies (e.g., requests, pandas, sqlalchemy, psycopg2-binary).
│   └── Dockerfile        # Defines how to build the Docker image for the Python application.
├── docker-compose.yml    # Orchestrates Docker services, defining the application's environment.
├── .env                  # Stores sensitive environment variables (API keys, city, DB credentials) and is excluded from Git.
├── .gitignore            # Specifies files and directories that Git should ignore (e.g., .env, pycache).
└── README.md             # This project's README file, providing an overview and instructions.
```
---

## Business Intelligence & Data Visualization (Metabase)

After the data is successfully extracted, transformed, and loaded into the PostgreSQL database, **Metabase** is used as the Business Intelligence (BI) tool to explore, analyze, and visualize the weather forecast data. Metabase provides an intuitive, browser-based interface for creating interactive dashboards and answering business questions without requiring deep SQL knowledge (though SQL can be used for advanced queries).

### Accessing Metabase

Once all Docker services are running, you can access the Metabase interface in your web browser:

[http://localhost:3000](http://localhost:3000)

Upon first access, you'll be guided through a quick setup process to create an admin user and connect to your PostgreSQL database (using `db` as the host, `5432` as the port, and your configured database name, username, and password from your `.env` file).

### Data Exploration & Example Dashboards

Metabase connects directly to the `hourly_weather_forecast` table in the PostgreSQL database, allowing users to build custom "Questions" (queries/charts) and organize them into comprehensive "Dashboards". Below are examples of key insights derived from the weather data for **Caracas**:

---

#### 1. Average Hourly Temperature Cycle

This visualization reveals the typical temperature pattern over a 24-hour cycle, averaged across all forecasted days. It helps in understanding the daily temperature fluctuations and identifying peak heat or cooler periods.

**How to create this chart in Metabase:**

1.  **Access Metabase:** Open your web browser and go to `http://localhost:3000`.
2.  **Start a New Native Query:**
    * From the Metabase homepage, click the **"+" icon** in the top right corner.
    * Select **"New question"**.
    * Choose **"Native query"**.
    * From the database dropdown, select your **"Weather DB"** (or whatever name you gave your PostgreSQL connection).
3.  **Paste and Run SQL:**
    * Copy the SQL query provided below and paste it into the Native Query editor.
    * Click the **"Visualize"** button in the bottom left to run the query.
4.  **Configure Chart Type and Settings:**
    * After the query runs, you'll see the results as a table. In the bottom left, click the **"Table"** button and select **"Line chart"**.
    * In the **Chart Settings panel** (the paint roller icon on the right sidebar):
        * For the **X-axis**, select `"Hour of Day"`.
        * For the **Y-axis**, select `"Average Temperature Celsius"`.
        * Optionally, add a Chart title like "Average Hourly Temperature Cycle".
5.  **Save Your Question:**
    * Click **"Save"** in the top right.
    * Give it a name (e.g., "Average Hourly Temperature Cycle (SQL)") and choose a collection (e.g., "Weather Dashboard Examples").

**SQL Query:**
```sql
SELECT
    EXTRACT(HOUR FROM CAST(time AS TIMESTAMP)) AS "Hour of Day",
    AVG(temp_c) AS "Average Temperature Celsius"
FROM
    hourly_weather_forecast
GROUP BY
    "Hour of Day"
ORDER BY
    "Hour of Day" ASC;
```
<img src="https://i.ibb.co/RXwNb80/Screenshot-2025-06-16-031356.png" alt="Average Hourly Temperature Cycle" style="max-width: 100%; height: auto;">

#### 2. Average Daily Humidity

This visualization shows the average humidity for each day across the forecast period. It's useful for understanding how humidity levels typically vary and can indicate general comfort levels.

**How to create this chart in Metabase:**

1.  **Access Metabase:** Open your web browser and go to `http://localhost:3000`.
2.  **Start a New Native Query:**
    * From the Metabase homepage, click the **"+" icon** in the top right corner.
    * Select **"New question"**.
    * Choose **"Native query"**.
    * From the database dropdown, select your **"Weather DB"** (or whatever name you gave your PostgreSQL connection).
3.  **Paste and Run SQL:**
    * Copy the SQL query provided below and paste it into the Native Query editor.
    * Click the **"Visualize"** button in the bottom left to run the query.
4.  **Configure Chart Type and Settings:**
    * After the query runs, you'll see the results as a table. In the bottom left, click the **"Table"** button and select **"Bar chart"**.
    * In the **Chart Settings panel** (the paint roller icon on the right sidebar):
        * For the **X-axis**, select `"Forecast Date"`.
        * For the **Y-axis**, select `"Average Humidity"`.
        * Optionally, add a Chart title like "Average Daily Humidity".
5.  **Save Your Question:**
    * Click **"Save"** in the top right.
    * Give it a name (e.g., "Average Daily Humidity (SQL)") and choose a collection (e.g., "Weather Dashboard Examples").

**SQL Query:**

```sql
SELECT
    CAST(time AS DATE) AS "Forecast Date",  -- Extracts just the date part for daily grouping
    AVG(humidity) AS "Average Humidity"
FROM
    hourly_weather_forecast
GROUP BY
    CAST(time AS DATE)
ORDER BY
    CAST(time AS DATE) ASC;
```
<img src="https://i.ibb.co/k68n7p4v/Screenshot-2025-06-16-033822.png" alt="Average Daily Humidity" style="max-width: 100%; height: auto;">

#### 3. Daily Weather Averages Overview

This table provides a daily summary of key weather metrics, displaying the average temperature, humidity, wind speed, precipitation, and cloud cover for each day in the forecast.

**How to create this chart in Metabase:**

1.  **Start a New Native Query:** (Follow steps 1-2 from "Average Hourly Temperature Cycle" above).
2.  **Paste and Run SQL:**
    * Copy the SQL query provided below and paste it into the Native Query editor.
    * Click the **"Visualize"** button in the bottom left to run the query.
3.  **Configure Chart Type and Settings:**
    * After the query runs, Metabase will automatically display the results as a **"Table"**. This is the intended chart type for this aggregated overview.
    * You can adjust column visibility or formatting in the **Chart Settings panel** (paint roller icon on the right sidebar) if desired.
4.  **Save Your Question:**
    * Click **"Save"** in the top right.
    * Give it a name (e.g., "Daily Weather Averages Overview (SQL)") and choose a collection (e.g., "Weather Dashboard Examples").

**SQL Query:**

```sql
SELECT
    CAST(time AS DATE) AS "Forecast Date", -- Group by the date
    AVG(temp_c) AS "Avg Temperature (C)",
    AVG(humidity) AS "Avg Humidity (%)",
    AVG(wind_kph) AS "Avg Wind Speed (kph)",
    AVG(precip_mm) AS "Avg Daily Precipitation (mm)", 
    AVG(cloud) AS "Avg Cloud Cover (%)"
FROM
    hourly_weather_forecast
GROUP BY
    CAST(time AS DATE)
ORDER BY
    CAST(time AS DATE) ASC;
```
<img src="https://i.ibb.co/W4q57Shf/Screenshot-2025-06-16-035106.png" alt="Daily Weather Averages Overview" style="max-width: 100%; height: auto;">

---

### Comprehensive Weather Dashboard

All individual charts have been combined into a single, interactive dashboard in Metabase. This dashboard provides a holistic and easily digestible view of the weather forecast data, allowing for quick insights into daily and hourly patterns. It can be further enhanced with filters (e.g., by date range) to enable more dynamic data exploration.

**How to create this dashboard in Metabase:**

1.  **Go to the Metabase Homepage:** Open your web browser and navigate to `http://localhost:3000`.
2.  **Start a New Dashboard:**
    * Click the **"+" icon** in the top right corner of the Metabase interface.
    * Select **"New dashboard"** from the dropdown menu.
3.  **Name Your Dashboard:**
    * Give your dashboard a descriptive name (e.g., "Caracas Weather Forecast Dashboard").
    * Click **"Create"**.
4.  **Add Your Saved Questions (Charts) to the Dashboard:**
    * Once the new, empty dashboard appears, click the **"Add a question"** button or the **"+" icon** (usually in the top right while in edit mode).
    * A sidebar will open showing all your saved questions. Select the ones you've created (e.g., "Average Hourly Temperature Cycle (SQL)", "Average Daily Humidity (SQL)", "Daily Weather Averages Overview (SQL)").
5.  **Arrange and Resize Widgets:**
    * While in "editing" mode (you'll see a pencil icon or "Done editing" button), click and drag the corners or edges of each chart to resize them.
    * Click and drag the charts themselves to rearrange their positions on the dashboard for an optimal layout.
6.  **Save the Dashboard:**
    * When you're satisfied with the layout, click the **"Done editing"** button (usually in the top right corner of the dashboard).

<img src="https://i.ibb.co/TxfV1yJ8/Screenshot-2025-06-16-035636.png" alt="Comprehensive Weather Dashboard" style="max-width: 100%; height: auto;"/>

## Next Steps

Here are some potential enhancements and future considerations for this project:

* **Scheduling:** Implement a scheduler (e.g., using Cron, Airflow, or a Docker-native scheduling tool) to automate the daily execution of the pipeline.
* **Error Handling & Monitoring:** Enhance error handling, add logging to external services, and set up monitoring for pipeline health.
* **Additional Data Sources:** Integrate data from other weather APIs or sources to enrich the dataset.
* **Data Deduplication/Upsert:** Implement more sophisticated logic for handling duplicate entries or updating existing records based on unique keys, instead of just appending.
* **Unit & Integration Tests:** Add comprehensive tests to ensure the reliability and correctness of the extraction, transformation, and loading processes.

---