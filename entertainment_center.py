import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story","Toys come to life","https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg/revision/latest?cb=20150108180742","https://www.youtube.com/watch?v=m9CvO0s6Tzw")

avatar=media.Movie("Avatar","Blue crazy aliens","https://www.abc.es/media/play/2017/09/28/avatar-kVmB--620x349@abc.jpeg","https://www.youtube.com/watch?v=kbA9TfGphOI")
camp_rock=media.Movie("Camp_Rock","Music film","https://is5-ssl.mzstatic.com/image/thumb/Features/d3/47/ce/dj.wgnrwxyp.jpg/268x0w.jpg","https://www.youtube.com/watch?v=kbA9TfGphOI")

list_movie=[toy_story,avatar,camp_rock]
#print (avatar.poster_url)
#toy_story.show_trailer()

#fresh_tomatoes.open_movies_page(list_movie)
print(media.Movie.__doc__) #documentacion clase
print(media.Movie.__name__) #nombre clase
print(media.Movi.__module__)
