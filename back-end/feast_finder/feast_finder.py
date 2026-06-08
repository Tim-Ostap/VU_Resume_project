import requests
from bs4 import BeautifulSoup

def scrape_job_description(url):
    #This is standard requests procedure, masking our script's identity, otherwise it would get blocked as a bot -> tells the server we are a human 
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

    response= requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    clean_text= soup.get_text(separator= " ")
    return clean_text

    #TESTBLOCK

if __name__ == "__main__":
    sample_url = "https://example.com"
    result = scrape_job_description(sample_url)
    print(result)
