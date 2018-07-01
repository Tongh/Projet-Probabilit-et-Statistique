def invert_str_to_float(data):
    if data == "":
        return None
    else:
        return float(data)


class Verre:

    def __init__(self, data_ligne):
        self.command = data_ligne[0]
        self.oeil = data_ligne[1]
        self.type = data_ligne[2]
        self.matiere = data_ligne[3]
        self.diametre = invert_str_to_float(data_ligne[4])
        self.base = invert_str_to_float(data_ligne[5])
        self.sphere = invert_str_to_float(data_ligne[6])
        self.sphere_mesure = invert_str_to_float(data_ligne[7])
        self.cylindre = invert_str_to_float(data_ligne[8])
        self.cylindre_mesure = invert_str_to_float(data_ligne[9])
        self.axe = invert_str_to_float(data_ligne[10])
        self.axe_mesure = invert_str_to_float(data_ligne[11])
        self.addition = invert_str_to_float(data_ligne[12])
        self.addition_mesure = invert_str_to_float(data_ligne[13])
        self.epais_centre = invert_str_to_float(data_ligne[14])
        self.epais_centre_mesure = invert_str_to_float(data_ligne[15])
        self.sphere_delta = None
        self.cylindre_delta = None
        self.axe_delta = None
        self.addition_delta = None
        self.epais_centre_delta = None
        self.init_all()

    def init_all(self):
        self.calculer_delta()

    def get(self, para):
        if para == "type":
            return self.type
        elif para == "matiere":
            return self.matiere

    def calculer_delta(self):
        if self.sphere and self.sphere_mesure:
            self.sphere_delta = self.sphere - self.sphere_mesure
        else:
            self.sphere_delta = None
        if self.cylindre and self.cylindre_mesure:
            self.cylindre_delta = self.cylindre - self.cylindre_mesure
        else:
            self.cylindre_delta = None
        if self.axe and self.axe_mesure:
            self.axe_delta = self.axe - self.axe_mesure
        else:
            self.axe_delta = None
        if self.addition and self.addition_mesure:
            self.addition_delta = self.addition - self.addition_mesure
        else:
            self.addition_delta = None
        if self.epais_centre and self.epais_centre_mesure:
            self.epais_centre_delta = self.epais_centre - self.epais_centre_mesure
        else:
            self.epais_centre_delta = None
