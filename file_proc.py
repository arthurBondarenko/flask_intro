FILE_NAME = "data.txt"


def pievinot(rindina):
    f = open(FILE_NAME, "a")
    f.write(rindina + "\n")
    f.close()


def lasit():
    with open(FILE_NAME, "r") as f:
        rindina = f.readlines()

    return rindina
