# OpenSpy

![OpenSpy Logo](logo.jpg)

**OpenSpy** is an open-source OSINT (Open Source Intelligence) tool designed for cybersecurity professionals, investigators, and developers. It enables you to gather information on IP addresses, perform advanced Google searches using the `allintext` operator, and save the results in JSON files.

<p align="center">
<img src="https://img.shields.io/github/last-commit/clydedc/OpenSpy?style=flat">
<img src="https://img.shields.io/github/stars/clydedc/OpenSpy?color=brightgreen">
<img src="https://img.shields.io/github/forks/clydedc/OpenSpy?color=brightgreen">
</p>

---

## Key Features

- **IP Address Lookup**: Retrieve information about an IP address (location, organization, etc.).
- **Advanced Google Search (allintext)**: Perform advanced Google searches using the `allintext` operator for more targeted results.
- **Result Saving**: Search results from `allintext` queries are automatically saved as JSON files for future analysis.
- **Command-Line Interface**: Use an interactive menu to perform searches directly from your terminal.

---

![OpenSpy Logo](logo.gif)

## Usage

Once installed, you can use the tool directly from the terminal to perform searches. Here's how:

### IP Address Lookup

This feature allows you to retrieve detailed information about a specific IP address.

```bash
python main.py
```

The program will prompt you to enter the IP address and display information such as city, country, organization, and more.

### Advanced Google Search with allintext

You can perform advanced Google searches using the `allintext` operator. The program will prompt you to enter a query and automatically execute the search.

```bash
python main.py
```

The program will then ask for your `allintext` query and display results, including title, URL, and snippet.

Results will also be saved in a JSON file within the `save/` directory.

---

## How It Works

### IP Lookup

IP address lookups are performed via the `ipinfo.io` service. When you enter an IP address, the program sends a request to retrieve information about it. The results include city, country, organization, and other relevant details.

### Google allintext Search

Google searches using the `allintext` operator allow you to find highly specific results. After entering a query, the tool performs a search on Google and extracts results from the HTML page, including title, URL, and a snippet for each result.

The results are then saved in a JSON file in the `save/` directory, with a timestamp-based filename for each search performed.

---

## Create Your Own API/Search Engine

To use the advanced Google search functionality, you can easily create your own API and search engine:

- **Google API Key**: [Get your API key](https://developers.google.com/custom-search/v1/overview?hl=en) (Free, 100 queries per day, requires a Google account).
- **Search Engine**: [Create a programmable search engine](https://programmablesearchengine.google.com/controlpanel/all) (Free).

You will receive a link like this: `https://cse.google.com/cse?cx=`

```bash
cx=CXID
```

---

## Installation

To install **OpenSpy**, follow these steps:

```bash
pip install -r requirements.txt
```

---

## Example IP Lookup

```bash
🔍 | OpenSpy | IP Address: 192.168.1.1
🔍 | OpenSpy | City: Paris
🔍 | OpenSpy | Region: Île-de-France
🔍 | OpenSpy | Country: France
🔍 | OpenSpy | Organization: Orange
🔍 | OpenSpy | Location: 48.8566, 2.3522
🔍 | OpenSpy | Postal Code: 75001
🔍 | OpenSpy | Hostname: example.com
```

---

## Example Google Search

```bash
🔍 | OpenSpy | Result 1:
   - Title: Example Title 1
   - URL: https://www.example.com
   - Snippet: Here is a snippet of the content found in this result.

🔍 | OpenSpy | Result 2:
   - Title: Example Title 2
   - URL: https://www.example2.com
   - Snippet: Another snippet found for this result.

🔍 | OpenSpy [LOG🟢] Results have been saved in `save/results_1627589123.json`
```

---

## Clone This Repository

```bash
git clone https://github.com/clydedc/OpenSpy.git
cd OpenSpy
```

