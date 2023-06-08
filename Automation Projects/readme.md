# Automation Projects

A collection of scripts for various purposes

## Description

This repository contains several Python scripts that serve different purposes. Each script focuses on a specific task or functionality and can be used independently.

## Prerequisites

To run these scripts, you need to have Python installed on your system. Additionally, some scripts may require specific dependencies, which are mentioned in the individual script descriptions below.

## Usage

### Script 1: `selenium_script.py`

This script utilizes the Selenium library to automate interactions with a web browser. It opens the YouTube homepage, performs a search, and retrieves the search results.

**Dependencies:**
- Selenium
- WebDriver (Chrome driver)

### Script 2: `remote_jobs.py`

This script fetches remote job listings from the RemoteOK API and filters them based on specified tags. It sends an email containing the filtered job information.

**Dependencies:**
- Requests
- SendEmail (custom module)

### Script 3: `nasa_picture.py`

This script retrieves the "Picture of the Day" from the NASA API and downloads it. It sets the downloaded picture as the desktop wallpaper.

**Dependencies:**
- Requests
- Platform (built-in)
- Pwd (built-in)
- Os (built-in)

### Script 4: `amazon_product_info.py`

This script scrapes product information from an Amazon product page. It checks if the product is available and below a specified price limit. If it meets the criteria, it sends an email notification.

**Dependencies:**
- Requests
- Beautiful Soup (bs4)

### Script 5: `tweet_scheduler.py`

This script reads scheduled tweets from a Google Sheet and checks if they need to be posted based on the specified time. If the time has arrived, it posts the tweet using the Twitter API.

**Dependencies:**
- Tweepy
- Gspread
- Json (built-in)
- Datetime (built-in)
- Dotenv

## Configuration

Some scripts require additional configuration or setup before running. Please refer to the individual script sections above for specific instructions.