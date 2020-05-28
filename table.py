class Table:
    id = 0
    name = ""
    description = ""
    image_filename = ""
    available_from = []
    available_to = []
    reservations = []

    def __repr__(self):
        return "<Table object " + "id=" + str(self.id) + " name=" + self.name + " description=" + self.description + " image_filename=" + str(self.image_filename) + " available_from=" + self.get_available_from() + " available_to=" + self.get_available_to() + " reservations=" + str(self.reservations) + ">"

    def get_available_from(self):
        return str(self.available_from[0]) + ":" + str(self.available_from[1]);

    def get_available_to(self):
        return str(self.available_to[0]) + ":" + str(self.available_to[1]);