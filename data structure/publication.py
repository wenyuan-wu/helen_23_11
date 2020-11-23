class Publication(object):
    def __init__(self, author: list, title: str, year: int):
        self.__title = title
        self.__author = author
        self.__year = year
        pass

    def __repr__(self):
        # TODO:
        return f'{self.__title}, {self.__author}, {self.__year}'


    def __str__(self):
        author_list = [f'"{i}"' for i in self.__author]

        return f'Publication({author_list}, "{self.__title}", {self.__year})'

    def __eq__(self, other):
        return str(self).__eq__(str(other))

    def __hash__(self):
        pass

    def get_title(self):
        # TODO:
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        pass

    def __gt__(self, other):
        author_list.sort()

    def __lt__(self, other):
        pass


    def __ge__(self, other):
        pass


    def __le__(self, other):
        pass



def main():
    test = Publication(['Python', 'Java'], 'Wenyuan', 2020)
    print(test.get_title())
    print(test)
    print(repr(test))
    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(s)
    print(str(p))
    print(p == s)

if __name__ == '__main__':
    main()
