import requests

def get_dictionary():
    url = "http://10.88.0.3:5000" \
    "/get-dict"  # URL of the server endpoint
    try:
        response = requests.get(url)  # Send GET request
        if response.status_code == 200:
            print("Dictionary received from server:")
            print(response.json())  # Print the JSON response
            return response.json()
        else:
            
            print(f"Failed to get dictionary. Status code: {response.status_code}")
            print(response.text)  # Print the error message
            return "error"
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return "error"

if __name__ == "__main__":
    while True:
        dict = get_dictionary()
        if dict == "error":
            print("error recieved")
        else:
            search = input("Enter a name to search for: ")
            if search in dict.keys():
                print(dict[search]["name"])
                print(dict[search]["age"])
                print(dict[search]["city"])
                print(dict[search]["favoriteSubject"])