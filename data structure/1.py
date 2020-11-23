class Students:

    level = 'bachelor'

    def __init__(self, name):
        self.name = name
        self.lectures = []
    def add_lecture(self, new_lecture):
        self.lectures.append(new_lecture)

d = Students('Walter White')
d.add_lecture('Lineare Algebra')
print(d.lectures)

e = Students('Bill Black')
e.add_lecture('Numerical Analysis')
print(e.lectures)

class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = keywords
        self.__template = template

    def filter(self, msg):
        wo = msg.split()

        output = ''
        for word in wo:
            if word in self.__keywords:
                wor = (len(word)//len(self.__template))*self.__template
                wor += self.__template[:(len(word)%len(self.__template))]
                output += wor + ' '
            else:
                if word == wo[-1]:
                    output += word
                else:
                    output += word + ' '

        return output


f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
offensive_msg = "abc defghi mastard jklmno"
clean_msg = f.filter(offensive_msg)
print(clean_msg)



'''class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__title = title
        self.__year = year

    def get_authors(self):
        return self.__authors

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def __str__(self):
        author_list = [f'"{i}"' for i in self.__author]

        return f'Publication({author_list}, "{self.__title}", {self.__year})'


    def __repr__(self):
        return 'Publication({}, {}, {})'.format(self.__authors, self.__title, self.__year)

    def __eq__(self, other):
        return (self.__authors,self.__title,self.__year)==(other.authors, other.title, other.year)

    def __hash__(self):'''




output = []


class Fridge:
    def store(self, item):
        self.item = item

    def __len__(self):
        return len(self)
    def __iter__(self):
        return self
    def __next__(self):
        self.output = output
        if self.item not in self.output:
            output.append(self.item)
        return output.sort()
    def take(self, item):
        output.remove(item)
    def find(self, name):
        self.name = name
        for idx, self.name in enumerate(sorted(output)):
            return output[idx]
    def take_before(self, date):
        self.date = date
        for i in sorted(output):
            if i < date:
                sorted(output).remove(i)
        return sorted(output)


if __name__ == '__main__':
    l = ["a", "b", "c"]
    for i in l:
        l.remove(i)

    f = Fridge()
    print(f)
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    i = f.take((191127, "Butter"))
    print("Removed {}, {} items left".format(i, len(f)))

