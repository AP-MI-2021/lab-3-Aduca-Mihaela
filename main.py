def print_menu():
    print("1. Citire lista")
    print("2. Afiseaza cea mai lunga subsecventa care are toate numerele neprime.")
    print("3. Afiseaza cea mai lunga subsecventa care are media numerelor mai mia decat o valoare citita.")
    print("4. Iesire")


def citire_lista():
    l = []
    givenstring = input(" Dati numerele din lista, separate prin virgula")
    numersasstring = givenstring.split(", ")
    for x in numersasstring:
        l.append(int(x))
    return l


def is_not_prime(x):
    """
    Determina daca un numar nu este prim.
    :return:returneaza True daca numarul nu este prim, sau False in caz contrar.
    """
    if x < 2:
        return True
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return True
    return False


def test_is_not_prime():
    assert is_not_prime(5) is False
    assert is_not_prime(-1) is True
    assert is_not_prime(4) is True
    assert is_not_prime(7) is False


def is_all_not_prime(l):
    """
    Verifica daca o lista aare elementele neprime.
    :param l: lista de numere intregi
    :return: True daca toate elementele sunt neprime, False in caz contrar.
    """
    for i in l:
        if is_not_prime(i):
            return True
    return False


def test_is_all_not_prime():
    assert is_all_not_prime([3, 5, 7]) is False
    assert is_all_not_prime([]) is False
    assert is_all_not_prime([2, 8, 4]) is True


def get_longest_all_not_prime(l):
    """
    Determina cea mai lunga subsecventa de numere care are toate numerele neprime.
    :param l: O lista de numere intregi
    :return: Returneaza cea mai lunga subsecventa de numere neprime dintr-o lista.
    """

    secv_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if is_not_prime(l[i: j + 1]) and len(l[i: j + 1]) > len(secv_max):
                secv_max = l[i: j + 1]
    return secv_max


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([1, 2, 3, 4, 6, 8]) == [4, 6, 8]
    assert get_longest_all_not_prime([2, 7, 9, 4, 6, 12, 8, 1]) == [4, 6, 12, 8]


def numbers_average(l):
    """
    Determina media aritmetica a  numerelor dintr-o lista.
    :param l: o lista de numere
    :return: Media aritmetica a numerelor din lista data.
    """
    sum_nr = 0
    count_nr = 0
    for i in l:
        sum_nr = sum_nr + i
        count_nr = count_nr + 1
    if count_nr == 0:
        return 0
    return sum_nr / count_nr


def test_numbers_average():
    assert numbers_average([2, 7, 9]) == 6
    assert numbers_average([4, 5]) == 4.5
    assert numbers_average([2, 4, 6, 8]) == 5


def get_longest_average_below(l, average):
    """
    Determina cea mai lunga subsecventa care are media numerelor mai mica decat o valoare citita.
    :param l: lista de numere intregi
    :param average: numar intreg
    :return:cea mai lunga subsecventa care are media numerelor mai mica decat average. 
    """
    secv_max = []

    for i in range(len(l)):
        for j in range(i, len(l)):
            if numbers_average(l[i: j + 1]) < average and len(l[i: j + 1]) > len(secv_max):
                secv_max = l[i: j + 1]
    return secv_max


def test_get_longest_average_below():
    assert get_longest_average_below([2, 4, 6, 8, 7, 20, 3, 5, 7], 10) == [2, 4, 6, 8, 7]
    assert get_longest_average_below([2, 3, 5, 7, 8, 9, 10, 5473, 2, 4, 5, 457], 18) == [2, 3, 5, 7, 8, 9, 10]


def main():
    test_is_not_prime()
    test_is_all_not_prime()
    test_get_longest_all_not_prime()
    test_numbers_average()
    test_get_longest_average_below()

    l = []
    while True:
        print_menu()
        optiune = input("dati optiunea: ")
        if optiune == "1":
            citire_lista()
        elif optiune == "2":
            print(get_longest_all_not_prime(l))
        elif optiune == "3":
            average = input("Introduceti valoarea: ")
            print(get_longest_average_below(l, average))
        elif optiune == "4":
            break
        else:
            print("Optiune gresita! Selectati alta optiune.")


if __name__ == '__main__':
    main()

