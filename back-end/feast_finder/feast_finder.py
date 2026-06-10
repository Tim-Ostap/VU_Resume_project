import requests
from bs4 import BeautifulSoup
import string

def scrape_job_description(url):
    #lets the server think we are a human 
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

    response= requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    clean_text= soup.get_text(separator= " ")
    return clean_text



def word_filter(job_text, target_keywords):
    
    found_skills= []
    
    lowercase_text= job_text.lower()
    
    text= lowercase_text
    
    new_text= text.translate(str.maketrans('','', string.punctuation))
    
    adj_text = " " + new_text + " "

    for keyword in target_keywords:
        adj_keyword = " " + keyword.lower() + " "

        if adj_keyword in adj_text:
            found_skills.append(keyword)

    return found_skills


    





    








        
            