class Environ:
    def set(self, attrib: str, value):
        self.__dict__["attrib"] = value

    def sets(self, new_pairs: dict):
        self.__dict__.update(new_pairs)

if "environ" not in globals():
    environ = Environ()
