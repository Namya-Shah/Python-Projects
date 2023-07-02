# Weather Information Readme

This code fetches and displays weather information for a specified city using the OpenWeatherMap API. It retrieves the weather description and temperature of the given city.

## Prerequisites

- Python 3.x installed on your system
- Requests library installed (`pip install requests`)
- OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/) to obtain an API key)

## Getting Started

1. Ensure that you have the necessary prerequisites installed.
2. Download the code and save it to a Python file, e.g., `weather_info.py`.
3. Replace `api_weather` in the `passwords.py` file with your OpenWeatherMap API key.
4. Run the code using the command `python weather_info.py`.
5. Follow the prompts in the console to enter a city name.

## Usage

1. Upon running the code, you will be prompted to enter a city name.
2. Enter the desired city name and press Enter.
3. The program will send a request to the OpenWeatherMap API to retrieve weather information for the specified city.
4. If the request is successful (status code 200), the program will display the weather description and temperature in Celsius.
5. If an error occurs during the request, the program will display an error message.

## Customization

- You can modify the code to display additional weather information by accessing other fields in the `data` dictionary.
- Customize the error message or add error handling as per your requirements.
- Implement additional functionality using other available data from the OpenWeatherMap API.

## Dependencies

The code relies on the following library:

- `requests`: Used for making HTTP requests to the OpenWeatherMap API.

## Note

- Ensure that you keep your API key confidential and avoid sharing it in public repositories or insecure environments.
- This code provides a basic implementation and may require further enhancements for error handling, input validation, or additional data processing.
