import pandas as p
import matplotlib.pyplot as plt

df = p.read_csv("6. IMDB-Movie-Data.csv")
df.info()


#       Вопрос 1: Фильмы с более высоким рейтингом получают больше голосов.
# Гипотезы:
# 1.Каково среднее количество голосов для фильмов с рейтингом выше 7?
# 2.Каково среднее количество голосов для фильмов с рейтингом 7 и ниже?
# 3.Насколько отличается среднее количество голосов между этими двумя группами?
#       Вопрос 2: Фильмы определенных жанров имеют тенденцию получать более высокие рейтинги.
# Гипотезы:
# 1.Какие жанры имеют наивысшие средние рейтинги?
# 2.Какие жанры имеют наинизшие средние рейтинги?
# 3.Насколько отличаются средние рейтинги между жанрами с наивысшими и наинизшими рейтингами?
#       Вопрос 3: Фильмы с известными актерами имеют более высокие рейтинги.
# Гипотезы:
# 1.Каково среднее значение рейтинга фильмов для топ-10 актеров?
# 2.Каково среднее значение рейтинга фильмов для топ-20 актёров?
df = df.dropna()
df.info()


top_10_actors = ["Vin Diesel", "Mackenzie Foy", "Heath Ledger", "Michael Caine", "Eli Roth", "Mélanie Laurent", "Jack Nicholson", "Jamie Foxx", "Leonardo DiCaprio", "Kerry Washington"]


top10_actors_ratingg = [757074.0, 1047747.0, 961034.5, 913152.0, 959065.0, 959065.0, 937414.0, 1039115.0, 1039115.0, 1039115.0]



top_20_actors = ["Daisy Ridley", "John Boyega", "Joseph Gordon-Levitt", "Tommy Lee Jones", "Stanley Tucci", "Martin Freeman", "Andy Serkis", "Saurabh Shukla", "Anil Kapoor", 
"Edward Asner"]

top_20_actors_rating = [661608.0, 661608.0, 701594.0, 660286.0, 735604.0, 668651.0, 668651.0, 677044.0, 677044.0, 722203.0]

top10_actors_rating = {}

p.Series(
    index=top_10_actors,
    data=top10_actors_ratingg
).plot(kind="bar")
plt.show()


def get_for_top10_actors_rating(column):

    all_actors = column['Actors'].split(',')

    for actor in all_actors:
        if actor not in top10_actors_rating:
            top10_actors_rating[actor] = {}
            top10_actors_rating[actor]["count"] = 1
            top10_actors_rating[actor]["votes_all"] = column["Votes"]
        else:
            top10_actors_rating[actor]["count"] += 1
            top10_actors_rating[actor]["votes_all"] += column["Votes"]



df.apply(get_for_top10_actors_rating, axis = 1)




