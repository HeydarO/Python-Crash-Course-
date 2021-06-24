def make_album(artist_name, album_title, song_number = ''):
    """Return an album title and artist"""
    if song_number == '':
        album = {'Artist name': artist_name, 'Album title': album_title}
    else:
        album = {'Artist name': artist_name, 'Album title': album_title, 'Number of songs': song_number}
    return album

while True:
    print("Favorite artist and album (you can stop with entering 'Q' anytime).")
    artist_name = input("Artist: ")
    if artist_name == 'Q':
        break

    album_title = input("Album title: ")
    if album_title == 'Q':
        break

    song_number = input("Number of songs: ")
    if song_number == 'Q':
        break

    album = make_album(artist_name, album_title, song_number)
    print(album)
