import cgi
import SentimentAnalysis
import csv

form = cgi.FieldStorage()
review = form.getvalue("q")

pred = SentimentAnalysis.test(review)
data = {'review':review, 'pred':pred}
with open("reviews.csv",'a',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data.values())

data = []
with open('reviews.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

pos_count = 0
neg_count = 0
for i in range(len(data)):
    if data[i][1] == 'Negative':
        neg_count += 1
    else:
        pos_count += 1

print("""
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
        <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Positive', %s],
          ['Negative', %s],
        ]);

        // Set chart options
        var options = {'title':'Review Analysis',
                       'width':400,
                       'height':300};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
</head>

<body>
<nav class="navbar navbar-light bg-light">
        <a class="navbar-brand" href="#">
            <img src="https://www.shareicon.net/download/2016/07/11/794345_message_512x512.png" width="30" height="30" class="d-inline-block align-top" alt=""> Review Analysis System
        </a>
    </nav>
"""%(pos_count, neg_count))

print("""
<div class='container'>
    <h1>Prediction is {}</h1>
""".format(pred))

print("""
<div class="row">
    <div class="col-md-6">
        <ul style='position:fixed;width:40%;height:70%;overflow-y:scroll;'>
""")
# print(data)
for i in range(len(data)):
    if data[i][1] == 'Negative':
        color = "red"
    else:
        color = 'green'
    print("<li style='color:{};'>{}</li>".format(color,data[i][0]))

print("""
</ul>
</div>
    <div class="col-md-6">
        <div id="chart_div"></div>
    </div>
</div>
</div>
""")

print("""
</body>
</html>
""")