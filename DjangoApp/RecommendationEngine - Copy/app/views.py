from django.shortcuts import render
from django.http import HttpResponse
import pymysql

connection = pymysql.connect(host='localhost',port=3306,user='root',database='movie_db',
autocommit = True)

cursor = connection.cursor()

query = "select * from movies where m_category like '%action%'"
cursor.execute(query)
actionMovies = cursor.fetchall()

query = "select * from movies where m_category like '%comedy%'"
cursor.execute(query)
comedyMovies = cursor.fetchall()

query = "select * from movies inner join users on users.m_id = movies.m_id"
cursor.execute(query)
watchedMovies = cursor.fetchall()

query = "select * from movies"
cursor.execute(query)
all_movies = cursor.fetchall()

user_cat_2 = watchedMovies[0][4]
user_cat_2 = user_cat_2.split(",")
for i in range(len(user_cat_2)):
	user_cat_2[i] = user_cat_2[i].strip()

recommended = []
for i in range(len(all_movies)):
	if watchedMovies[0][1] == all_movies[i][1]:
		continue
	movies_cat = all_movies[i][4].split(',')
	for j in range(len(movies_cat)):
		movies_cat[j] = movies_cat[j].strip()
	n = len(set(movies_cat).intersection(user_cat_2))
	d = len(set(movies_cat).union(user_cat_2))
	score = n/d
	if score > 0:
		recommended.append(all_movies[i])

# print(comedyMovies)
def index(req):
    data = {"action":actionMovies,"comedy":comedyMovies,"watched":watchedMovies,
    "recommended":recommended}
    return render(req, 'index.html', context={"data":data})

def details(req,pk):
    query = "select * from movies where m_id=%s"
    cursor.execute(query, (pk))
    data = cursor.fetchall()
    return render(req, "details.html",context={"data":data})