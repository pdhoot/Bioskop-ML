import MySQLdb
import time
import datetime
db=MySQLdb.connect("localhost","root","hello123","bioskop")
cursor=db.cursor()

query = "ALTER TABLE MOVIE_DB ADD %s VARCHAR(1000)" % ("coverpic")
cursor.execute( query)

sql=""" UPDATE MOVIE_DB SET icon = %s ,coverpic = %s WHERE movie= %s """

data=("/o1sF8LTFogPULmYOn4f1B6GpaJS.jpg","https://i.ytimg.com/vi/Yj2Q2cTQYPQ/maxresdefault.jpg","Thor: Ragnarok (2017)")
cursor.execute(sql,data)
data=("/qfWLO0iXmbvxzyk0ez4pXrgkRDM.jpg","http://www.hdwallpapers.in/walls/hardcore_henry-HD.jpg","Hardcore Henry (2016)")
cursor.execute(sql,data)
data=("/6bCplVkhowCjTHXWv49UjRPn0eK.jpg","http://www.ochaplin.com/wp-content/uploads/2016/03/batman_v_superman___dawn_of_justice_wallpaper_by_lamboman7-d7p62tn1.png","Batman v Superman: Dawn of Justice (2016)")
cursor.execute(sql,data)
data=("/nK7poFj5zwywfOaWMUkVByvDMMl.jpg","http://espritcine.fr/wp-content/uploads/2016/01/la-chute-de-londres-photo-gerard-butler-947555.jpg","London Has Fallen (2016)")
cursor.execute(sql,data)
data=("/63XTc9wnF6GSFCXV0cZaV9XRX27.jpg","http://www.pacifymind.net/wp-content/uploads/10779d-x-men-apocalypse-photo-high-quality.jpg","X-Men: Apocalypse (2016)")
cursor.execute(sql,data)
data=("/5N20rQURev5CNDcMjHVUZhpoCNC.jpg","http://www.siwallpaperhd.com/wp-content/uploads/2016/03/captain_america_civil_war_computer_wallpaper_hd.jpg","Captain America: Civil War (2016)")
cursor.execute(sql,data)
data=("/vOipe2myi26UDwP978hsYOrnUWC.jpg","http://www.hdwallpapers.in/walls/the_jungle_book_2016_movie-wide.jpg","The Jungle Book (2016)")
cursor.execute(sql,data)
data=("/aeiVxTSTeGJ2ICf1iSDXkF3ivZp.jpg","http://image.tmdb.org/t/p/w1920/lZCfk1LNVK8LE9o7XYBHvpMgBc1.jpg","10 Cloverfield Lane (2016)")
cursor.execute(sql,data)
data=("/sM33SANp9z6rXW8Itn7NnG1GOEs.jpg","http://www.tabtabz.com/cn/wp-content/uploads/2016/03/zootopia_life.jpg","Zootopia (2016)")
cursor.execute(sql,data)
data=("/inVq3FRqcYIRl2la8iZikYYxFNR.jpg","http://wallpapersqq.net/wp-content/uploads/2016/01/Deadpool-photoshoot.jpg","Deadpool (2016)")
cursor.execute(sql,data)

sql=""" UPDATE MOVIE_DB SET trailer= %s, icon = %s WHERE movie= %s """

data=("8V4dEWPJKNk","/5hqbJSmtAimbaP3XcYshCixuUtk.jpg","Seven Samurai (1954)")
cursor.execute(sql,data)
data=("NmzuHjWmXOc","/9O7gLzmreU0nGkIB6K3BsJbzvNv.jpg","Shawshank Redemption, The (1994)")
cursor.execute(sql,data)
data=("fB_8VCwXydM","/d4KNaTrltq6bpkFS01pYtyXa09m.jpg","Godfather, The (1972)")
cursor.execute(sql,data)
data=("36GfaI0_B8E","/efFW4euBJIha6WVJoBPSfyui2Aa.jpg","Close Shave, A (1995)")
cursor.execute(sql,data)
data=("oiXdPolca5w","/jgJoRWltoS17nD5MAQ1yK2Ztefw.jpg","Usual Suspects, The (1995)")
cursor.execute(sql,data)
data=("_H6SG34EOqk","/2w8JYyCxK7GOIi68cPhFqknCESA.jpg","Wrong Trousers, The (1993)")
cursor.execute(sql,data)
data=("Y3P0Zpe-2og","/oFwzvRgfxJc0FUr2mwYTi10dk3G.jpg","Sunset Blvd. (a.k.a. Sunset Boulevard) (1950)")
cursor.execute(sql,data)
data=("8PyZCU2vpi8","/tHbMIIF51rguMNSastqoQwR0sBs.jpg","Godfather: Part II, The (1974)")


db.commit()
db.close()

# import MySQLdb
# import time
# import datetime
# db=MySQLdb.connect("localhost","root","hello123","bioskop")
# cursor=db.cursor()

# sql=""" UPDATE MOVIE_DB SET trailer = %s, icon= %s WHERE movie= %s """

# data=("uwN3jF6bCM4","https://i.ytimg.com/vi/Yj2Q2cTQYPQ/maxresdefault.jpg","Thor: Ragnarok (2017)")
# cursor.execute(sql,data)
# data=("F67oZ1LwEhU","http://www.hdwallpapers.in/walls/hardcore_henry-HD.jpg","Hardcore Henry (2016)")
# cursor.execute(sql,data)
# data=("nIGtF3J5kn8","http://www.ochaplin.com/wp-content/uploads/2016/03/batman_v_superman___dawn_of_justice_wallpaper_by_lamboman7-d7p62tn1.png","Batman v Superman: Dawn of Justice (2016)")
# cursor.execute(sql,data)
# data=("CaVHsRxnhto","http://espritcine.fr/wp-content/uploads/2016/01/la-chute-de-londres-photo-gerard-butler-947555.jpg","London Has Fallen (2016)")
# cursor.execute(sql,data)
# data=("CmOZOk9j0Sk","http://www.pacifymind.net/wp-content/uploads/10779d-x-men-apocalypse-photo-high-quality.jpg","X-Men: Apocalypse (2016)")
# cursor.execute(sql,data)
# data=("43NWzay3W4s","http://www.siwallpaperhd.com/wp-content/uploads/2016/03/captain_america_civil_war_computer_wallpaper_hd.jpg","Captain America: Civil War (2016)")
# cursor.execute(sql,data)
# data=("d-WPiRJni8w","http://www.hdwallpapers.in/walls/the_jungle_book_2016_movie-wide.jpg","The Jungle Book (2016)")
# cursor.execute(sql,data)
# data=("saHzng8fxLs","http://image.tmdb.org/t/p/w1920/lZCfk1LNVK8LE9o7XYBHvpMgBc1.jpg","10 Cloverfield Lane (2016)")
# cursor.execute(sql,data)
# data=("UPJGR8mFCUg","http://www.tabtabz.com/cn/wp-content/uploads/2016/03/zootopia_life.jpg","Zootopia (2016)")
# cursor.execute(sql,data)
# data=("7jIBCiYg58k","http://wallpapersqq.net/wp-content/uploads/2016/01/Deadpool-photoshoot.jpg","Deadpool (2016)")
# cursor.execute(sql,data)

# db.commit()
# db.close()