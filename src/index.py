from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print(mehua)
    print(olutta)


def liian_monta_lauseketta():
    a = 1
    b = 2
    c = 3
    d = 4
    raja_arvo = 20
    if raja_arvo > 1:
        print("on")
    return a + b + c + d


class LiikaaAttribuutteja:
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.eka = 1
        self.toka = 2
        self.kolmas = 3
        self.neljas = 4
        self.viides = 5
        self.kuudes = 6


if __name__ == "__main__":
    main()