import requests
import time

url = "https://zora3-backend.onrender.com/api/products"

max_retries = 5
retry_delay = 5  # seconds

for attempt in range(max_retries):
    try:
        response = requests.get(url, timeout=10)

        # Raise an exception if the response code is not 200 OK
        response.raise_for_status()

        # Attempt to parse JSON
        data = response.json()
        print("Successfully fetched JSON data:")
        print(data)
        break

    except requests.exceptions.RequestException as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        time.sleep(retry_delay)
    except ValueError:
        print(f"Attempt {attempt + 1} failed: Invalid JSON response")
        time.sleep(retry_delay)
else:
    print("Failed to fetch valid JSON data after multiple attempts.")
