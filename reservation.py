class Reservation:
    id = 0
    table_id = ""
    date = []
    _from = []
    _to = []

    def __repr__(self):
        return "<Reservation object " + "id=" + str(self.id) + " date=" + self.get_date() + " _from=" + self.get_from() + " _to=" + self.get_to() + ">"

    def get_date(self):
        return str(self.date[0]) + "." + str(self.date[1]) + "." +str(self.date[2])

    def get_year(self):
        return self.date[0]

    def get_month(self):
        return self.date[1]

    def get_day(self):
        return self.date[2]

    def same_date(self, date):
        if date[0] == self.get_year() and date[1] == self.get_month() and date[2] == self.get_day():
            return True
        return False

    def get_from(self):
        return str(self._from[0]) + ":" + str(self._from[1])

    def get_from_hour(self):
        return int(self._from[0])

    def get_from_minute(self):
        return int(self._from[1])

    def get_to_hour(self):
        return int(self._to[0])

    def get_to_minute(self):
        return int(self._to[1])

    def get_to(self):
        return str(self._to[0]) + ":" + str(self._to[1]);