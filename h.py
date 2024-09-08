import pandas as p
import matplotlib.pyplot as plt

df = p.read_csv("6. IMDB-Movie-Data.csv")
df.info()


#       Гипотеза 1: Фильмы с более высоким рейтингом получают больше голосов.
# Вопросы:
# 1.Каково среднее количество голосов для фильмов с рейтингом выше 7?
# 2.Каково среднее количество голосов для фильмов с рейтингом 7 и ниже?
# 3.Насколько отличается среднее количество голосов между этими двумя группами?
#       Гипотеза 2: Фильмы определенных жанров имеют тенденцию получать более высокие рейтинги.
# Вопросы:
# 1.Какие жанры имеют наивысшие средние рейтинги?
# 2.Какие жанры имеют наинизшие средние рейтинги?
# 3.Насколько отличаются среднее количество голосов у жанров с наивысшими и наинизшими рейтингами?
#       Гипотеза 3: Фильмы с известными актерами получают более высокое количество голосов.
# Вопросы:
# 1.Каково среднее значение голосов у фильмов для топ-10 актеров?
# 2.Каково среднее значение голосов у фильмов для топ-20 актёров?
# 3.Насколько отличаються эти значения
df = df.dropna()
df.info()




rating_more_than_7 = df[df["Rating"]>= 7]["Votes"].mean()
rating_less_than_7 = df[df["Rating"]<= 7]["Votes"].mean()

print(df["Genre"].value_counts())
print(rating_more_than_7)


#p.Series(
    #data=[rating_more_than_7, rating_less_than_7],
    #index=["Rating >= 7", "Rating < 7"]
#).plot(kind='barh')
#plt.show()





text_actors = ["top 10 actors", "top 20 actors"]


top10_actors_ratingg = [757074.0, 1047747.0, 961034.5, 913152.0, 959065.0, 959065.0, 937414.0, 1039115.0, 1039115.0, 1039115.0]
top_actors_rating_mean = [869283, 683429]




top_20_actors_rating = [661608.0, 661608.0, 701594.0, 660286.0, 735604.0, 668651.0, 668651.0, 677044.0, 677044.0, 722203.0]

top10_actors_rating = {}

#p.Series(
    #index=text_actors,
    #data=top_actors_rating_mean
#).plot(kind="bar")
#plt.show()


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





genres_rating = {}


def get_for_genre_rating(column):
    
    genres_splitted = column["Genre"].split(",")

    
    for genre in genres_splitted:
        if not genre in genres_rating:
            genres_rating[genre] = {"count": 1, "rating_all": column["Rating"]}
        else:
            genres_rating[genre]["count"] += 1
            genres_rating[genre]["rating_all"] += column["Rating"]


df.apply(get_for_genre_rating, axis=1)


Action_mean = genres_rating["Action"]["rating_all"] / genres_rating["Action"]["count"]
drama_mean = genres_rating["Drama"]["rating_all"] / genres_rating["Drama"]["count"]
Sci_Fi_mean = genres_rating["Sci-Fi"]["rating_all"] / genres_rating["Sci-Fi"]["count"]
Fantasy_mean = genres_rating["Fantasy"]["rating_all"] / genres_rating["Fantasy"]["count"]
Romance_mean = genres_rating["Romance"]["rating_all"] / genres_rating["Romance"]["count"]
Adventure_mean = genres_rating["Adventure"]["rating_all"] / genres_rating["Adventure"]["count"]
Comedy_mean = genres_rating["Comedy"]["rating_all"] / genres_rating["Comedy"]["count"]
horror_mean = genres_rating["Horror"]["rating_all"] / genres_rating["Horror"]["count"]
thriller_mean = genres_rating["Thriller"]["rating_all"] / genres_rating["Thriller"]["count"]
Animation_mean = genres_rating["Animation"]["rating_all"] / genres_rating["Animation"]["count"]
bio_mean = genres_rating["Biography"]["rating_all"] / genres_rating["Biography"]["count"]
Crime_mean = genres_rating["Crime"]["rating_all"] / genres_rating["Crime"]["count"]
History_mean = genres_rating["History"]["rating_all"] / genres_rating["History"]["count"]

print(f"Средний рейтинг фильмов с жанром 'Action': {Action_mean}")
print(f"Средний рейтинг фильмов с жанром 'Drama': {drama_mean}")
print(f"Средний рейтинг фильмов с жанром 'scifi': {Sci_Fi_mean}")
print(f"Средний рейтинг фильмов с жанром 'fantasy': {Fantasy_mean}")
print(f"Средний рейтинг фильмов с жанром 'romance': {Romance_mean}")
print(f"Средний рейтинг фильмов с жанром 'adv': {Adventure_mean}")
print(f"Средний рейтинг фильмов с жанром 'comedy': {Comedy_mean}")
print(f"Средний рейтинг фильмов с жанром 'horror': {horror_mean}")
print(f"Средний рейтинг фильмов с жанром 'thriller': {thriller_mean}")
print(f"Средний рейтинг фильмов с жанром 'animation': {Animation_mean}")
print(f"Средний рейтинг фильмов с жанром 'bio': {bio_mean}")
print(f"Средний рейтинг фильмов с жанром 'crime': {Crime_mean}")
print(f"Средний рейтинг фильмов с жанром 'history': {History_mean}")

three_high = df[df["Genre"] == "Drama"]["Votes"].mean() + df[df["Genre"] == "Action"]["Votes"].mean() + df[df["Genre"] == "Comedy"]["Votes"].mean()
print(three_high /3)

three_low = df[df["Genre"] == "Adventure"]["Votes"].mean() + + df[df["Genre"] == "Horror"]["Votes"].mean() + df[df["Genre"] == "Thriller"]["Votes"].mean()
print(three_low / 3)









