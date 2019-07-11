import cgi
import SentimentAnalysis

form = cgi.FieldStorage()
review = form.getvalue("q")

pred = SentimentAnalysis.test(review)

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Prediction is {}</h1>
</body>
</html>
""".format(pred))