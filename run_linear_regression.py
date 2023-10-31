import requests

features = [' ROA(C) before interest and depreciation before interest'
            ' ROA(A) before interest and % after tax'
            ' ROA(B) before interest and depreciation after tax'
            ' Persistent EPS in the Last Four Seasons'
            ' Per Share Net profit before tax (Yuan ¥)' ' Debt ratio %'
            ' Net worth/Assets' ' Net profit before tax/Paid-in capital'
            ' Retained Earnings to Total Assets' ' Net Income to Total Assets']

url = "http://localhost:9696/predict"

client = {' ROA(C) before interest and depreciation before interest': 0.51,
          ' ROA(A) before interest and % after tax': 0.21,
          ' ROA(B) before interest and depreciation after tax': 0.35,
          ' Persistent EPS in the Last Four Seasons': 0.70,
          ' Per Share Net profit before tax (Yuan ¥)': 0.56,
          ' Debt ratio %': 0.28,
          ' Net worth/Assets': 0.43,
          ' Net profit before tax/Paid-in capital': 0.81,
          ' Retained Earnings to Total Assets': 0.95,
          ' Net Income to Total Assets': 0.64}
response = requests.post(url, json=client).json()

print(response)
