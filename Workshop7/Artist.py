class Artist:
    def __init__(self, name = "unknown", birth_year = -1, death_year = -1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        output = f"Artist: {self.name} "
        if self.birth_year > 0 and self.death_year > 0:
            output += f"({self.birth_year} to {self.death_year})"
        elif self.birth_year > 0:
            output += f"({self.birth_year} to present)"
        else:
            output += "(unknown)"
        print(output)
      
class Artwork:
    def __init__(self, title = "unknown", year_created = -1, artist = Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        print(f"Name: {self.artist.name}")
        output = f"Title: {self.title}, "
        if self.year_created > 0:
            output += f"{self.year_created}"
        else:
            output += "unknown"
        print(output)



if __name__ == "__main__":
    user_artist_name = "Picasso"
    user_birth_year = 1956
    user_death_year = 1999
    user_title = "Flowers"
    user_year_created = 1970

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()







