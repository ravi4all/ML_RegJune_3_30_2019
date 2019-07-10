import cgi
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('home_data.csv')

X = data.iloc[:,3:9].values
y = data['price'].values

sc = StandardScaler()
X = sc.fit_transform(X)
y = sc.fit_transform(y.reshape(-1,1))

b = np.array([-0.00100342, -0.00100342, -0.14412359,  0.04628725,  0.75167023,
       -0.03842886, -0.00866364])

form = cgi.FieldStorage()
bedrooms = int(form.getvalue('bedrooms'))
bathrooms = int(form.getvalue('bathrooms'))
sqft_living = int(form.getvalue('sqft_living'))
sqft_lot = int(form.getvalue('sqft_lot'))
floors = int(form.getvalue('floors'))
waterfront = int(form.getvalue('waterfront'))

newX = np.array([[1, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront]])

newX = sc.transform(newX)
pred = newX.dot(b)
pred = sc.inverse_transform(pred)
pred = round(pred[0],2)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Prediction for House Price is {}</h1>
<h3>Bedrooms : {}</h3>
<h3>Bathrooms : {}</h3>
<h3>Living Area (Sqft) : {}</h3>
<h3>Lot Size (Sqft) : {}</h3>
<h3>Floors : {}</h3>
<h3>Waterfront : {}</h3>
</body>
</html>
""".format(pred, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront))