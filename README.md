Solar Data Discovery – Week 0 Challenge

This project is part of the 10 Academy training program. It explores solar energy data from Benin, Sierra Leone, and Togo to identify which region has the best solar potential.

The main goal is to use data analysis to help MoonLight Energy Solutions make smarter decisions on where to invest in solar farms. This will support better energy efficiency and long-term sustainability for the company.



About the Project

This challenge focuses on understanding environmental data such as sunlight (GHI, DNI, DHI), temperature, humidity, wind speed, and cleaning events.  
By studying these factors, we can discover patterns that show how weather affects solar performance and recommend the best areas for new solar panel installations.

The analysis is carried out using Python and Jupyter notebooks following Exploratory Data Analysis (EDA) techniques.



Project Structure

Below is the folder layout of this project:

solar-challenge-week1/
├── .github/workflows/
│   └── ci.yml
├── notebooks/
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── compare_countries.ipynb
├── src/
│   └── utils.py
├── scripts/
│   ├── cleaning_script.py
│   └── pipeline.py
├── data/
├── tests/
├── requirements.txt
├── .gitignore
├── CHANGELOG.md
└── README.md



 Setup Instructions

1.Clone the repository
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1

markdown
Copy code

2.Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate # For Windows
source .venv/bin/activate # For Mac/Linux

markdown
Copy code

3.Install all required libraries
pip install -r requirements.txt

markdown
Copy code

4.Open Jupyter Notebook
jupyter notebook

yaml
Copy code
Then open the notebooks in the `notebooks` folder and start exploring.


Project Objectives

- Perform data cleaning and exploratory data analysis (EDA).  
- Find patterns between sunlight, humidity, temperature, and wind.  
- Compare solar data across Benin, Sierra Leone, and Togo.  
- Recommend the most suitable country for solar farm investment.  
- Practice version control with Git, GitHub Actions, and CI/CD workflows.  


Key Learnings

During this challenge, I learned how to:

- Use Git and GitHub for tracking and managing projects.  
- Organize a clean and professional data project structure.  
- Work with Python libraries like Pandas, NumPy, and Matplotlib.  
- Set up CI/CD workflows for continuous integration.  
- Write clear documentation to make teamwork easier and more effective.  


Project Status (Week 0)

 Environment setup completed  
 CI/CD successfully passing  
 DataCleaner class and cleaning pipeline implemented  
 Next: Comparative analysis and dashboard visualization  



Example Usage

```python
from src.utils import DataCleaner
import pandas as pd

df = pd.read_csv("data/benin.csv")
cleaner = DataCleaner(df)
cleaner.handle_missing().remove_outliers(["GHI", "DNI", "Tamb"]).save_cleaned("data/benin_clean.csv")
Author
Kaleab Million
10 Academy – Data Engineering, Financial Analytics, and Machine Learning Track