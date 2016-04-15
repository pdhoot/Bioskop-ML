from load_data import load_data

f1 = "../dataset/ratings.dat"
f2 = "../dataset/users.dat"
f3 = "../dataset/movies.dat"
l1 = load_data(f1, f2, f3, 3953, 6042)

l1.pred_update()
l1.find_similar_movies()
l1.make_recommendation()
l1.valid_count()