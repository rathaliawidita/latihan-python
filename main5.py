
class Orang(object):

    def __init__(self):
        pass

class Anak:

    def __init__(self):
        pass


#class
class Mahasiswa(Orang, Anak):

    # self -> method ini adalah member dari sebuah class
    def __init__(self):
        self.nama = ''
        self.kelas = ''

    def mengerjakan_tugas(self):
        print('kerjakan tugas')


nama = 'Rathalia'
# object
mhs = Mahasiswa()

mhs.nama = 'Rathalia'
mhs.kelas = '4C'