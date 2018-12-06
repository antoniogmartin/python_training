import webbrowser
class Movie:
    """ THIS CLASS PROVIDE A WAY TO STORE MOVIE RELATED INFO """
    valid_ratings=["G","PG","PG-13","R"]
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title=movie_title
        self.story_line=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer)
