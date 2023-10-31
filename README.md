# midterm_project

A lot of small businesses go bankrupt. I tried to create models that would account for the prospects of business bankruptcy.
## dataset_link:
https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction

## running project:
### 1.install packages from requirements.txt:
$ pip install -r requirements.txt

### 2.install flask in pipenv:
$ pipenv install flask 

### 3. Run application:
*   3.1 For LogisticRegression model:
    #### 3.1.1 run app:
     $ pipenv run waitress-serve --listen=localhost:9696 predict_linear_regression:app
    #### 3.1.2 run python file for checking:
     $ python run_linear_regression.py
*   3.2 For RandomForestClassifier model:
    #### 3.2.1 run app:
     $ pipenv run waitress-serve --listen=localhost:9696 predict_random_forest_classifier:app
    #### 3.2.2 run python file for checking:
     $ python run_random_forest_classifier.py
