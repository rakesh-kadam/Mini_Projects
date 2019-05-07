import media
import fresh_tomatoes

The_Godfather = media.Movie("The Godfather","The Godfather is a 1972 American crime film directed by Francis Ford Coppola and produced by Albert S. Ruddy from a screenplay by Mario Puzo and Coppola.","https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg","https://www.youtube.com/watch?v=sY1S34973zA")

The_Shawshank_Redemption = media.Movie("The Shawshank Redemption","The Shawshank Redemption is a 1994 American drama film written and directed by Frank Darabont and starring Tim Robbins and Morgan Freeman","https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

Pulp_Fiction = media.Movie("Pulp Fiction","Pulp Fiction is a 1994 American crime film directed by Quentin Tarantino. The lives of two mob hitmen (Samuel L. Jackson and John Travolta), a boxer (Bruce Willis), a gangster's wife (Uma Thurman), and a pair of diner bandits (Tim Roth and Amanda Plummer) intertwine in four tales of violence and redemption","https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg","https://www.youtube.com/watch?v=s7EdQ4FqbhY")

#Fight_Club = media.Movie("Fight Club","Fight Club is a 1999 film based on the 1996 novel of the same name by Chuck Palahniuk. The film was directed by David Fincher, and stars Brad Pitt, Edward Norton and Helena Bonham Carter. Norton plays the unnamed protagonist, an everyman who is discontented with his white-collar job","https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg","https://www.youtube.com/watch?v=SUXWAEX2jlg")

#Braveheart = media.Movie("Braveheart","Braveheart is a 1995 epic historical medieval war drama film directed by and starring Mel Gibson. Gibson portrays William Wallace, a 13th-century Scottish warrior who led the Scots in the First War of Scottish Independence against King Edward I of England.","https://upload.wikimedia.org/wikipedia/en/thumb/5/55/Braveheart_imp.jpg/220px-Braveheart_imp.jpg","https://www.youtube.com/watch?v=1NJO0jxBtMo")

movies = [The_Godfather,The_Shawshank_Redemption,Pulp_Fiction]

fresh_tomatoes.open_movies_page(movies)