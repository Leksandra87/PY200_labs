class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.is_valid(name)
        self._name = name
        self.is_valid(author)
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @staticmethod
    def is_valid(text: str) -> None:
        if not isinstance(text, str):
            raise TypeError

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    """ Класс бумажные книги """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError
        if pages < 0:
            raise ValueError
        self._pages = pages


class AudioBook(Book):
    """ Класс аудио книги """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        if not isinstance(duration, (int, float)):
            raise TypeError
        if duration < 0:
            raise ValueError
        self._duration = duration


if __name__ == "__main__":
    bo1 = Book('Text_1', 'Author_1')
    bo2 = PaperBook('Text_2', 'Author_2', 120)
    bo3 = AudioBook('Text_3', 'Author_3', 32.5)
    print(bo1, bo2, bo3, sep='\n')
    bo2.name = "New"
    print(bo1)
