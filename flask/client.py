import requests

def get_dictionary():
    url = "http://10.0.10.30:5000" \
    "/get-dict"  # URL of the server endpoint
    try:
        response = requests.get(url)  # Send GET request
        if response.status_code == 200:
            print("Dictionary received from server:")
            print(response.json())  # Print the JSON response
        else:
            
            print(f"Failed to get dictionary. Status code: {response.status_code}")
            print(response.text)  # Print the error message
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_dictionary()