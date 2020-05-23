class Product:
    id = 0
    name = ""
    description = ""
    dimension = ""
    default_amount = 0
    image_filename = ""

    def __repr__(self):
        return "<Product object " + "id=" + str(self.id) + " name=" + self.name + " description=" + self.description + " dimension=" + self.dimension + " default_amount=" + str(self.default_amount) + " image_filename=" + str(self.image_filename) + ">"
