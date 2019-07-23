import os

class CD():

    @staticmethod
    def back_path():
        a = os.getcwd()
        b = str(a).split('/')
        c = len(b) - 1
        d = len(b[c])
        e = len(a) - d
        f = a[:e - 1]
        os.chdir(f)

    @staticmethod
    def set_path(path):
        try:
            os.chdir(path)
            return True
        except:
            return False