# Project Overview

In this project, we'll predict the winner of international volleyball matches.  

**Project Details**

* Scrape match data from Volleyball World using Selenium and pandas.
* Build features like rolling averages to capture team performance trends.
* Train a Random Forest model to predict match outcomes using scikit-learn.
* Use the trained model to simulate and predict winners of future matches.

## Code

This project was inspired by the football matches predictor project [here](https://github.com/dataquestio/project-walkthroughs/tree/master/football_matches).

File overview:

* `scraper.py` - Scrapes match data and stores it in a structured format.
* `prediction.ipynb` - Processes data, builds rolling averages, and trains the machine learning model.

# Local Setup

## Installation

To follow this project, please install the following locally:

* JupyerLab
* Python 3.8+
* Python packages
    * pandas
    * Selenium
    * webdriver-manager
    * scikit-learn
    
## Data

We'll be scraping [Volleyball World](https://en.volleyballworld.com/) to get our data in the first part of this project (`scraper.py`).

If you only want to do the second part of the project (`prediction.ipynb`) you can download `mens_stats.csv`.
