import requests
from bs4 import BeautifulSoup

page = requests.get("https://visaindex.com/")
src = page.content
soup = BeautifulSoup(src,"lxml")

countries1 = [] # with html code
countries = [] # just names

countries1 = soup.find_all("span",{"class":"country-name"})
for country in countries1:
    countries.append(country.text.strip().lower())


visa_free_access_list = []
visa_on_arrival_list = []
eta_list = []

visa_free_access = []
visa_on_arrival = []
eta = []

country = (input("Enter Country: ")).strip().lower()

page = requests.get(f"https://visaindex.com/country/{country}-passport-ranking/")
src = page.content
soup = BeautifulSoup(src,'lxml')

group1 = soup.find("div",{"class":"col-md-6 px-lg-3 col-vfa countries-col"})
group2 = soup.find("div",{"class":"col-md-6 px-lg-3 col-voa countries-col"})
group3 = soup.find("div",{"class":"col-md-6 px-lg-3 col-eta countries-col"})

visa_free_access_list = group1.find_all("span",{"class":"country-name"})
visa_on_arrival_list = group2.find_all("span",{"class":"country-name"})
eta_list = group3.find_all("span",{"class":"country-name"})

for vfa in visa_free_access_list:
    visa_free_access.append(vfa.text.strip())

for voa in visa_on_arrival_list:
    visa_on_arrival.append(voa.text.strip())

for e in eta_list:
    eta.append(e.text.strip())


print("Visa free access:", visa_free_access)
print("\n\n\n")
print("Visa on arrival:", visa_on_arrival)
print("\n\n\n")
print("Eta:", eta)