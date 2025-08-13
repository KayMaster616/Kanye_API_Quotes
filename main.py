import requests

request = requests.get('https://api.kanye.rest')

def main():
    if request.status_code == 200:
        
        quote = request.json().get('quote')
        print("'" + quote + "' - Kanye West")
        
    else:
        print(f"Error: {request.status_code}")
        

if __name__ == "__main__":
    print("This script fetches a random Kanye West quote.")
    print("Make sure you have the requests library installed.")
    print("You can install it using: pip install requests")
    print("Enjoy the quote!")
    print("Fetching a quote from Kanye West...")
    main()
    
        
        