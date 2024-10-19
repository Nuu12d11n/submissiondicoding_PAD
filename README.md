1. Setup Environment

cd submission

pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt

# Generate requirements.txt with current environment's dependencies
pip freeze > requirements.txt

# Run the Streamlit app located in the 'dashboard' folder
streamlit run dashboard/dashboard.py
