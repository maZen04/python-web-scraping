# Python Web Scraping

A collection of practical web scraping projects built with **Python**, **Requests**, **BeautifulSoup**, and **CSV**.

This repository contains multiple scraping projects focused on extracting, processing, and storing structured data from different websites.

## 🚀 Projects

### 1. YallaKora Scraper

Scrapes football match data from YallaKora.

**Extracted data:**

* Championship name
* First team
* Second team
* Match result
* Match time

**Features:**

* Scrapes matches for a specific date
* Handles multiple championships
* Extracts structured match information
* Saves the results to a CSV file
* Supports Arabic data using UTF-8 encoding

**Technologies:**

* Python
* Requests
* BeautifulSoup
* CSV

---

### 2. VisaIndex Scraper

Scrapes visa information from VisaIndex based on the selected country.

**Extracted data:**

* Visa Free Access countries
* Visa On Arrival countries
* ETA countries

**Features:**

* Retrieves available countries
* Searches for a specific country
* Extracts visa-related information
* Displays scraped data in a structured format

**Technologies:**

* Python
* Requests
* BeautifulSoup

---

### 3. Books to Scrape

A web scraping project built using the training website **Books to Scrape**.

The scraper collects book information across multiple pages.

**Extracted data:**

* Book title
* Price
* Availability
* Rating

**Features:**

* Scrapes multiple pages
* Handles pagination
* Collects structured book data
* Scrapes 50 pages
* Saves the collected data to a CSV file

**Technologies:**

* Python
* Requests
* BeautifulSoup
* CSV

## 🛠️ Technologies & Concepts

* Python
* Requests
* BeautifulSoup
* HTML Parsing
* Web Scraping
* Pagination
* Data Extraction
* Data Cleaning
* CSV File Handling
* HTTP Requests
* Basic Error Handling

## 📂 Repository Structure

```text
python-web-scraping/
│
├── books_scrapper/
│   └── books_scraper.py
│
├── visaindex_scapper/
│   └── visaindex_scraper.py
│
├── yallakora_scrapper/
│   └── yallakora_scraper.py
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/maZen04/python-web-scraping.git
```

Navigate to the repository:

```bash
cd python-web-scraping
```

Install all required dependencies:

```bash
pip install -r requirements.txt
```

The required Python libraries are listed in `requirements.txt`.

## ▶️ Running the Projects

Navigate to the desired project folder and run its Python script.

For example:

```bash
python books_scraper.py
```

or:

```bash
python visaindex_scraper.py
```

or:

```bash
python yallakora_scraper.py
```

## 📊 Output

Depending on the project, scraped data can be:

* Displayed directly in the terminal
* Saved as CSV files
* Processed into structured Python data

## 🎯 Purpose

The purpose of this repository is to practice and demonstrate practical **Python Web Scraping** skills, including:

1. Sending HTTP requests
2. Parsing HTML pages
3. Finding and extracting HTML elements
4. Cleaning extracted data
5. Handling multiple pages
6. Structuring scraped information
7. Exporting data to CSV

## 📦 Requirements

The project dependencies are listed in [`requirements.txt`](requirements.txt).


## 👨‍💻 Author

**Mazen Ayman**

GitHub: [@maZen04](https://github.com/maZen04)
