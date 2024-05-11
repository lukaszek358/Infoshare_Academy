# METODA TO TAKA FUNKCJA, KTÓRA JEST ZDEFINIOWANA WEWNĄTRZ KLASY
# PRZYJMUJE ZAZWYCZAJ CO NAJMNIEJ JEDEN ARGUMENT ZWANY 'self'
# POD ARGUMENTEM 'self' MAMY DOSTĘP DO AKTUALNEJ INSTANCJI OBIEKTU NA KTÓRYM ZOSTAŁA WYWOŁANA TA METODA
# KONSTRUKTOR (POPRZEDNIE ZAJĘCIA) RÓWNIEŻ JEST METODĄ, ALE SPECJALNEGO RODZAJU

class Student():
    def __init__(self, name):
        # Pole/ stan naszego biektu
        self.name = name
    def print_something(self):
        print('To ja - metoda studenta!')
    def print_self(self):
        print(f'Czym jest self? {self}')
        print(f'Jest tutaj dostęp do name: {self.name}')
    def do_all_work(self):
        print('Teraz to się napracuję...')
        self.piece_of_work()
        self.piece_of_work()
        self.piece_of_work()
        print('Robota zakończona.')
    def piece_of_work(self):
        print('Robota, robota, robota ...')
#-----------------------------------------------------------------------------------------------------------------------
def run_example():
    student = Student(name= 'Mikołaj')

    # Wywołanie metody
    student.print_something()

    # Pierwszy przekazany niejawnie argument - zawiera referencje na aktualny obiekt
    student.print_self()

    # Metoda może wywoływać inną metodę
    student.do_all_work()

if __name__ == '__main__':
    run_example()