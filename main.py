def print_menu():
    print("1. Citire lista")
    print("2. Afiseaza cea mai lunga subsecventa care are toate numerele neprime.")
    print("3. Afiseaza cea mai lunga subsecventa care are toate numerele prime.")
    print("4. Afiseaza cea mai lunga subsecventa care are numerele ordonate crescator.")
    print("5. Iesire")


def citire_lista():
    l = []
    n = int(input("Dati numarul de elem din lista: "))
    for i in range(n):
        l.append(int(input("l[" + str(i) + "]= ")))
    return l

def is_prime(x):
    """
    Determina daca un numar este prim.
    :param x: nr intreg
    :return: True daca numarul este prim sau False in caz contrar.
    """
    if x < 2:
        return False
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                return False
    return True

def test_is_prime():
    assert is_prime(13) is True
    assert is_prime(1) is False
    assert is_prime(2) is True


def is_all_not_prime (l):
    """
    Determina daca toate numerele dintr-o lista nu sunt prime
    :param l: o lista de numere intregi
    :return: True daca toate numerele dintr-o lista nu sunt prime sau False, in caz contar.
    """
    for i in l:
        if is_prime(i):
            return False
    return True


def test_is_all_not_prime():
    assert is_all_not_prime([]) is True
    assert is_all_not_prime([1, 2, 3]) is False
    assert is_all_not_prime([1, 4, 8, 9]) is True


def get_longest_all_not_prime(lista):
    '''
    Determina cea mai lunga subsecventa de numere care are toate numerele neprime.
    :param lista: o lista de numere intregi
    :return: Afiseaza cea mai lunga subsecventa de numere neprime dintr-o lista.
    '''
    secv_max = []
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if is_all_not_prime(lista[i:j+1]) and len(lista[i:j+1]) > len(secv_max):
                secv_max = lista[i:j+1]
    return secv_max


def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([]) == []
    assert get_longest_all_not_prime([2, 3, 5, 7]) == []
    assert get_longest_all_not_prime([1, 2, 3, 4, 6, 12, 14, 5, 7, 2, 8, 10, 26]) == [4, 6, 12, 14]

def is_all_prime(lista):
    '''
    Determina daca toate numerele dintr-o lista nu sunt prime
    :param lista: o lista de numere intregi
    :return:True daca toate numerele dintr-o lista sunt prime sau False, in caz contar.
    '''
    for i in lista:
        if not is_prime(i):
            return False
    return True


def get_longest_all_primes(lista):
    '''
    Determina cea mai lunga subsecventa de numere care are toate numerele prime.
    :param lista: o lista de numere intregi.
    :return: Afiseaza cea mai lunga subsecventa de numere prime dintr-o lista.
    '''
    secv_max=[]
    for i in range(len(lista)):
        for j in range(i,len(lista)):
            if is_all_prime(lista[i:j+1]) and len(lista[i:j+1]) > len(secv_max):
                secv_max = lista[i:j+1]
    return secv_max


def test_get_longest_all_primes():
    assert get_longest_all_primes([3, 5, 7, 8]) == [3, 5, 7]
    assert get_longest_all_primes([12, 4, 8, 9]) == []
    assert get_longest_all_primes([3, 7, 15, 2, 3, 5]) == [2, 3, 5]
    assert get_longest_all_primes([3, 7, 13, 17, 23]) == [3, 7, 13, 17, 23]

def ordine_crescatoare(l):
    '''
    Verifica daca 2 numere sunt ordonate crescator.
    :param l:lista de nr intregi
    :return: True, daca elementele sunt ordonate crescator sau False in caz contrar
    '''
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

def test_ordine_crescatoare():
    assert ordine_crescatoare([2,5,7,9]) is True
    assert ordine_crescatoare([9,2,7,5]) is False
    assert ordine_crescatoare([3,6,7,8]) is True

def get_longest_sorted_asc(l):
    """
    Determina cea mai lunga subsecventa care are numerele ordonate crescator.
    :param l: lista de numere intregi.
    :return: cea mai lunga subsecventa care are numerele ordonate crescator.
    """

    sec_max = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if ordine_crescatoare(l[i:j + 1]) is True and (len(l[i:j + 1]) > len(sec_max)):
                sec_max = l[i:j + 1]
    return sec_max


def test_get_longest_sorted_asc():
    assert get_longest_sorted_asc([1, 5, 6, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert get_longest_sorted_asc([1, 2, 3, 1, 0, 5, 6, 7]) == [0, 5, 6, 7]


def main():
    test_is_prime()
    test_is_all_not_prime()
    test_get_longest_all_not_prime()
    test_get_longest_all_primes()
    test_ordine_crescatoare()
    test_get_longest_sorted_asc()

    l = []
    while True:
        print_menu()
        optiune = input("dati optiunea: ")
        if optiune == "1":
            l = citire_lista()
        elif optiune == "2":
            print(get_longest_all_not_prime(l))
        elif optiune == "3":
            print(get_longest_all_primes(l))
        elif optiune == "4":
            print(get_longest_sorted_asc(l))
        elif optiune == "5":
            break
        else:
            print("Optiune gresita! Reincercati!")

if __name__ == '__main__':
    main()
