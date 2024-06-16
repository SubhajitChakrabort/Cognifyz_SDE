import requests
from bs4 import BeautifulSoup

def fetch_bbc_headlines():
    url = 'https://www.bbc.com/news/world/asia/india'
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('h3')

    print("BBC News Headlines:")
    for i, headline in enumerate(headlines[:10], 1):  
        print(f"{i}. {headline.text.strip()}")

def fetch_techcrunch_headlines():
    url = 'https://techcrunch.com/tag/india/'
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('a', {'class': 'post-block__title__link'})

    print("TechCrunch Headlines:")
    for i, headline in enumerate(headlines[:10], 1):  
        print(f"{i}. {headline.text.strip()}")

def main():
    while True:
        print("\nWeb Scraper")
        print("1. Fetch BBC News Headlines")
        print("2. Fetch TechCrunch Headlines")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            fetch_bbc_headlines()
        elif choice == '2':
            fetch_techcrunch_headlines()
        elif choice == '3':
            print("Exiting the web scraper.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
