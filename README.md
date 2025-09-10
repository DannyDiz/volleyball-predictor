# Project Overview

In this project, we'll predict the winner of international volleyball matches.  

**Project Steps**

* Scrape match data using Selenium and pandas.  
* Make predictions about who will win a match using scikit-learn.
* Measure error and improve our predictions.

## Code

This project was inspired by the football matches predictor project [here](https://github.com/dataquestio/project-walkthroughs/tree/master/football_matches).

File overview:

* `scraper.py` - a python file that scrapes our data.
* `predictions.ipynb` - a Jupyter notebook that makes predictions.

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

If you only want to do the second part of the project (`predictions.ipynb`) you can download `VNL_mens_stats.csv`.

## Next Steps

Currently, the functionality of this project is for retrospective match prediction. Stay tuned for a predictive match model.
