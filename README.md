# Weather Data Pipeline - Venezuela

This project is a foundational data engineering pipeline designed to extract, transform, and load (ETL) weather data for a specified city in Venezuela (defaulting to Caracas). It leverages Docker and Docker Compose for environment management, ensuring reproducibility and easy setup.

**Current Stage:** **Extract (E)** - The pipeline is currently configured to fetch weather forecast data from [WeatherAPI.com](https://www.weatherapi.com/).

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
git clone [https://github.com/osmarbetancourt/weather-pipeline-vzla.git](https://github.com/osmarbetancourt/weather-pipeline-vzla.git)
cd weather-pipeline-vzla
```

### 2. Obtain Your WeatherAPI.com API Key

To fetch weather data, you'll need a free API key from WeatherAPI.com:

1.  Go to [**WeatherAPI.com**](https://www.weatherapi.com/).
2.  Sign up for a free account.
3.  Once registered and logged in, navigate to your **[My Account](https://www.weatherapi.com/my/)** dashboard.
4.  Your default API key should be visible there. **Copy this key.**