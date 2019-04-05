import scrapping


def ma_fonction(x):
    print(x)
    return True

scrapping.go_and_find(url="http://datavolley.lnv.fr/2017/EScoresheet/Men/", 
                      extensions=[".pdf"], 
                      filter_function=ma_fonction)

