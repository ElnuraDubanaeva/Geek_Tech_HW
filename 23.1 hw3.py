class Computer:
    def __init__(self, __cpu, __memory):
        self.__cpu = __cpu
        self.__memory = __memory

    def __str__(self):
        return f'Device: Computer cpu:{self.__cpu} memory:{self.__memory}'

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, __sim_cards_list):
        self.__sim_cards_list = __sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        return f'There is a call to the number {call_to_number} from sim card {sim_card_number} {self.__sim_cards_list[sim_card_number]}'

    def __str__(self):
        return f'Device : Phone sim_cards: {self.__sim_cards_list}'
    @staticmethod
    def use_gps(location):
        return f'локация отмечена до {location}'


class SmartPhone(Computer, Phone):
    def __init__(self, __cpu, __memory, __sim_cards_list):
        Computer.__init__(self, __cpu, __memory)
        Phone.__init__(self, __sim_cards_list)

    def __str__(self):
        return f'Device: Smart Phone sim_cards: {self.sim_cards_list} memory {self.memory} cpu {self.cpu}'


def show_result():
    computer1 = Computer(123, 234)
    phone1 = Phone('beeline, o, megacom')
    smart_phone1 = SmartPhone(23, 46, ['beeline', 'o'])
    smart_phone2 = SmartPhone(56, 67, ['beeline', 'o', 'megacom'])
    devices = [computer1, phone1, smart_phone1, smart_phone2]
    print(smart_phone2.call(1, '+996708869616'))
    print(smart_phone1.use_gps('tSUM'))
    print(smart_phone1 < smart_phone2)
    for device in devices:
        print(device)

show_result()
