from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__make_album() ###

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for row_idx in range(len(self.photos)):
            if len(self.photos[row_idx]) < 4:
                self.photos[row_idx].append(label) ###
                return f'{label} photo added successfully on page {row_idx + 1} slot {len(self.photos[row_idx])}'
        return "No more free slots"

    def __make_album(self):
        result = []
        for _ in range(self.pages):
            result.append([]) ###
        return result

    def display(self):
        result = '-' * 11 + '\n'
        for row in self.photos:
            result += ' '.join(['[]' for _ in row]) + '\n' ###
            result += '-' * 11 + '\n'

        return result.strip()


# album = PhotoAlbum.from_photos_count(33)
# print(album.pages)
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
