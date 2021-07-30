class Citizen:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"


class UnforgivingElephant:
    def __init__(self, name):
        self.name = name
        self._people_to_stomp_on = []

    def get_slapped_by(self, name):
        self._people_to_stomp_on.append(name)
        print('痛い!')

    def revenge(self):
        print('10年後...')
        for person in self._people_to_stomp_on:
            print('%s は %s を踏みつける' % (self.name, person))


if __name__ == '__main__':
    joe = UnforgivingElephant('Joe')
    joe.get_slapped_by('Tarek')
    joe.get_slapped_by('Bill')
    joe.revenge()
