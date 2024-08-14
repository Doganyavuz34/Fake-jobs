# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:44:28 2024

@author: Fujitsu
"""
import requests
from bs4 import BeautifulSoup
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
whole_jobs = soup.find("div", attrs={"id":"ResultsContainer"})
jobs = whole_jobs.find_all("div", attrs={"class":"column is-half"})
for job in jobs:
    is_tanimi = job.find("h2").text
    isveren_adi = job.find("h3").text
    is_konumu = job.find("p", attrs={"class":"location"}).text
    is_tarihi = job.find("p", attrs={"class":"is-small has-text-grey"}).text
    print("\nİş tanımı: " + str(is_tanimi))
    print("\nİşveren adı: " + str(isveren_adi))
    print("\nİş konumu: " + str(is_konumu.strip()))
    print("\nİş tarihi: " + str(is_tarihi.strip()))
    print("\n#############\n")
    
    
    
    
    
    
    
    










