Solar Data Discovery – Week 0 Challenge



This project is part of the 10 Academy training program. It explores solar energy data for Benin, Sierra Leone, and Togo to identify which region has the best solar potential.



The goal is to use data analysis to help MoonLight Energy Solutions make smarter decisions on where to invest in solar farms to improve efficiency and long-term sustainability.



About the Project



This challenge focuses on understanding environmental data such as sunlight (GHI, DNI, DHI), temperature, humidity, wind speed, and cleaning events.



By studying these measurements, we can find trends and recommend the best areas for solar panel installation. The analysis is done using Exploratory Data Analysis (EDA) techniques with Python and Jupyter notebooks.



Project Structure



Here is the folder layout of this project:



solar-challenge-week1/

.github/workflows/

&nbsp;  ci.yml

notebooks/

&nbsp;  benin\_eda.ipynb

&nbsp;  sierra\_leone\_eda.ipynb

&nbsp;  togo\_eda.ipynb

&nbsp;  compare\_countries.ipynb

src/

&nbsp;  utils.py

scripts/

&nbsp;  cleaning\_script.py

data/

tests/

requirements.txt

.gitignore

README.md



Setup Instructions



1\. Clone the repository

git clone https://github.com/<your-username>/solar-challenge-week1.git

cd solar-challenge-week1



2\. Create and activate a virtual environment

python -m venv .venv

.venv\\Scripts\\activate        # For Windows

source .venv/bin/activate     # For Mac/Linux



3\. Install all required libraries

pip install -r requirements.txt



4\. Open Jupyter Notebook

jupyter notebook

Then open the notebooks in the notebooks folder and start exploring.



Project Objectives



\- Perform data cleaning and exploratory data analysis (EDA)

\- Find patterns between sunlight, humidity, temperature, and wind

\- Compare solar data across Benin, Sierra Leone, and Togo

\- Recommend the best country for solar farm investment

\- Practice Git, GitHub Actions, and version control



Key Learnings



Through this challenge, I learned how to:

\- Use Git and GitHub for tracking and managing projects

\- Keep a clean and professional data project structure

\- Work with Python libraries like Pandas, NumPy, and Matplotlib

\- Set up CI/CD workflows for continuous integration

\- Write clear documentation for better collaboration



Author

Kaleab Million

10 Academy – Data Engineering, Financial Analytics, and Machine Learning Track



