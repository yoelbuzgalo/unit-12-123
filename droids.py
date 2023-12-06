PROTO = "Protocol"
ASTRO = "Astro"

PARTS = {
    PROTO: {'p_head', 'p_chasis', 'p_left_arm', 'p_right_arm', ' p_left_leg', 'p_right_leg'},
    ASTRO: {'a_dome', 'a_body', 'a_left_leg', 'a_center_leg', 'a_right_leg'}
    }

class Droid:
    __slots__ = ['__serial_number','__type', '__parts']
    def __init__(self, serial_number, type):
        self.__serial_number = serial_number
        self.__type = type
        self.__parts = set()


    def needs_part(self, a_part):
        if a_part not in self.__parts:
            return True
        
    def install(self, a_part):
        if self.needs_part(a_part):
            self.__parts.add(a_part)
        else:
            raise ValueError("Part already exists")
        
    def is_complete(self):
        for part in PARTS[self.__type]:
            if self.needs_part(part):
                return False
        return True
    
    def __repr__(self):
        return "Serial Number:" + str(self.__serial_number) \
        + "\n Parts:" + str(self.__parts)
    
def main():
    droid = Droid(1, PROTO)
    droid.install('p_head')
    print(droid)

if __name__ == "__main__":
    main()