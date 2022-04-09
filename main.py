import math
import scipy.special as special


class Kula:
    promien = -1
    gestosc = -1

    def pole(self):
        return 4 * math.pi * self.promien ** 2

    def objetosc(self):
        return 1.33 * math.pi * self.promien ** 3

    def masa(self):
        return self.objetosc() * self.gestosc


class Czworoscian:
    bok = -1
    gestosc = -1

    def pole(self):
        return self.bok ** 2 * math.sqrt(3)

    def objetosc(self):
        return (self.bok ** 3 * math.sqrt(2))/12

    def masa(self):
        return self.objetosc()*self.gestosc


class Elipsoida:
    a = -1
    b = -1
    c = -1
    gestosc = -1

    def abc(self):
        tab = []
        a = self.a
        b = self.b
        c = self.c
        if a >= b >= c:
            tab.append(a)
            tab.append(b)
            tab.append(c)
        elif a >= c >= b:
            tab.append(a)
            tab.append(c)
            tab.append(b)
        elif b >= a >= c:
            tab.append(b)
            tab.append(a)
            tab.append(c)
        elif b >= c >= a:
            tab.append(b)
            tab.append(c)
            tab.append(a)
        elif c >= a >= b:
            tab.append(c)
            tab.append(a)
            tab.append(b)
        elif c >= b >= a:
            tab.append(c)
            tab.append(b)
            tab.append(a)
        return tab

    def e(self):
        a = self.abc()[0]
        c = self.abc()[2]
        return math.sqrt(1 - (c ** 2 / a ** 2))

    def phi(self):
        return math.asin(self.e())

    def m(self):
        a = self.abc()[0]
        b = self.abc()[1]
        c = self.abc()[2]
        return (a**2*(b**2-c**2))/(b**2*(a**2-c**2))

    def objetosc(self):
        return 1.33 * math.pi * self.a * self.b * self.c

    def pole(self):
        a = self.abc()[0]
        b = self.abc()[1]
        c = self.abc()[2]
        if a == b == c:
            print('uzyj opcji kula')
            return -1
        if a == b or a == c or b == c:
            return 2 * math.pi * b * (b + a / self.e() * self.phi())
        else:
            return 2 * math.pi*(c**2 + ((b*c**2)/math.sqrt(a**2 - c**2)) *
                                special.ellipkinc(self.phi(), self.m()) +
                                (b*math.sqrt(a**2-c**2)*special.ellipeinc(self.phi(), self.m())))

    def masa(self):
        return self.objetosc() * self.gestosc


def tylkoliczbydodatnie():
    while 1 == 1:
        try:
            x = float(input())
            if x <= 0:
                print("Podaj wartość dodatnią")
            if x > 0:
                return float(x)
        except ValueError:
            print('podana wartość nie może być ciągiem znaków')


class Ostroslup:
    a = -1
    b = -1
    h = -1
    gestosc = -1

    def objetosc(self):
        return self.a * self.b * self.h / 3

    def pole(self):
        return self.a * self.b + math.sqrt((0.5 * self.a) ** 2 + self.h ** 2) * \
               self.b + math.sqrt((0.5 * self.b) ** 2 + self.h ** 2) * self.a

    def masa(self):
        return self.objetosc() * self.gestosc


class Stozek:
    r = -1
    h = -1
    gestosc = -1

    def objetosc(self):
        return math.pi * self.r ** 2 * self.h / 3

    def pole(self):
        return math.pi * self.r ** 2 + math.pi * self.r * math.sqrt(self.r ** 2 + self.h ** 2)

    def masa(self):
        return self.objetosc() * self.gestosc


class Walec:
    r = -1
    h = -1
    gestosc = -1

    def objetosc(self):
        return math.pi * self.r ** 2 * self.h

    def pole(self):
        return math.pi * self.r ** 2 + 2 * math.pi * self.r * self.h

    def masa(self):
        return self.objetosc() * self.gestosc


def start():
    print('Witaj, wybierz figurę:')
    while 1 == 1:
        interfejs()


def interfejs():
    print('Kula-->\"kula\"')
    print('Czworscian foremny-->\"czworoscian\"')
    print('Elipsoida-->\"elipsoida\"')
    print('Ostroslup-->\"ostroslup\"')
    print('Stozek-->\"stozek\"')
    print('wyjdz z programu-->\"koniec\"')
    menu()


def zatwierdz():
    print('wróć do menu głównego --> \"menu\"')
    print('zamknij program --> \"koniec\"')
    wyboropcji = input()
    if wyboropcji == 'menu':
        interfejs()
    elif wyboropcji == 'koniec':
        koniec()
    else:
        print('nieznana opcja ', wyboropcji, ', spróbuj jeszcze raz')
        zatwierdz()


def koniec():
    if 1 == 1:
        print('')
        exit(1)


def menu():
    wyboruzytkownika = input()
    if wyboruzytkownika == 'kula':
        print('kula:')
        wyborparametru()
        menuparametru(wyboruzytkownika)
    elif wyboruzytkownika == 'czworoscian':
        print('czworoscian:')
        wyborparametru()
        menuparametru(wyboruzytkownika)
    elif wyboruzytkownika == 'elipsoida':
        print('elipsoida:')
        wyborparametru()
        menuparametru(wyboruzytkownika)
    elif wyboruzytkownika == 'ostroslup':
        print('ostroslup:')
        wyborparametru()
        menuparametru(wyboruzytkownika)
    elif wyboruzytkownika == 'stozek':
        print('stozek:')
        wyborparametru()
        menuparametru(wyboruzytkownika)
    elif wyboruzytkownika == 'walec':
        print('walec:')
        wyborparametru()
        menuparametru(wyboruzytkownika)
    elif wyboruzytkownika == 'koniec':
        koniec()
    else:
        print('nieznana opcja ', wyboruzytkownika, ', spróbuj jeszcze raz')
        menu()


def wyborparametru():
    print('wybierz parametr, ktory chcesz wyswietlic:')
    print('oblicz pole powierzchnii-->\"pole\"')
    print('oblicz objetosc-->\"objetosc\"')
    print('oblicz mase-->\"masa\"')
    print('wyjdz z programu-->\"koniec\"')


def menuparametru(wyboruzytkownikafigura):
    wyboruzytkownikaparametr = input()
    if wyboruzytkownikaparametr == 'pole':
        switchfigury(wyboruzytkownikafigura, wyboruzytkownikaparametr)
    elif wyboruzytkownikaparametr == 'objetosc':
        switchfigury(wyboruzytkownikafigura, wyboruzytkownikaparametr)
    elif wyboruzytkownikaparametr == 'masa':
        switchfigury(wyboruzytkownikafigura, wyboruzytkownikaparametr)
    elif wyboruzytkownikaparametr == 'koniec':
        koniec()
    else:
        print('nieznana opcja ', wyboruzytkownikaparametr, ', spróbuj jeszcze raz')
        zatwierdz()


def switchfigury(wyboruzytkownikafigura, wyboruzytkownikaparametr):
    if wyboruzytkownikafigura == 'kula':
        if wyboruzytkownikaparametr == 'pole':
            wyswkula(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'objetosc':
            wyswkula(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'masa':
            wyswkula(wyboruzytkownikaparametr)
    if wyboruzytkownikafigura == 'czworoscian':
        if wyboruzytkownikaparametr == 'pole':
            wyswczworoscian(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'objetosc':
            wyswczworoscian(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'masa':
            wyswczworoscian(wyboruzytkownikaparametr)
    if wyboruzytkownikafigura == 'elipsoida':
        if wyboruzytkownikaparametr == 'pole':
            wyswelipsoida(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'objetosc':
            wyswelipsoida(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'masa':
            wyswelipsoida(wyboruzytkownikaparametr)
    if wyboruzytkownikafigura == 'ostroslup':
        if wyboruzytkownikaparametr == 'pole':
            wyswostroslup(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'objetosc':
            wyswostroslup(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'masa':
            wyswostroslup(wyboruzytkownikaparametr)
    if wyboruzytkownikafigura == 'stozek':
        if wyboruzytkownikaparametr == 'pole':
            wyswstozek(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'objetosc':
            wyswstozek(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'masa':
            wyswstozek(wyboruzytkownikaparametr)
    if wyboruzytkownikafigura == 'walec':
        if wyboruzytkownikaparametr == 'pole':
            wyswwalec(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'objetosc':
            wyswwalec(wyboruzytkownikaparametr)
        elif wyboruzytkownikaparametr == 'masa':
            wyswwalec(wyboruzytkownikaparametr)


def wyswkula(wyboruzytkownikaparametr):
    kula = Kula()
    if kula.promien == -1:
        print('podaj promien w metrach')
        setattr(kula, 'promien', tylkoliczbydodatnie())
    if wyboruzytkownikaparametr == 'pole':
        print('pole = ', round(kula.pole(), 2), 'm^2')
    elif wyboruzytkownikaparametr == 'objetosc':
        print('objetosc = ', round(kula.objetosc(), 2), 'm^3')
    elif wyboruzytkownikaparametr == 'masa':
        if kula.gestosc == -1:
            print('podaj gestisc w kg/m^3')
            setattr(kula, 'gestosc', tylkoliczbydodatnie())
        print('masa = ', round(kula.masa(), 2), 'kg')
    zatwierdz()


def wyswstozek(wyboruzytkownikaparametr):
    stozek = Stozek()
    if stozek.r == -1:
        print('podaj promien w metrach')
        setattr(stozek, 'r', tylkoliczbydodatnie())
        print('podaj wysokosc w metrach')
        setattr(stozek, 'h', tylkoliczbydodatnie())
    if wyboruzytkownikaparametr == 'pole':
        print('pole = ', round(stozek.pole(), 2), 'm^2')
    elif wyboruzytkownikaparametr == 'objetosc':
        print('objetosc = ', round(stozek.objetosc(), 2), 'm^3')
    elif wyboruzytkownikaparametr == 'masa':
        if stozek.gestosc == -1:
            print('podaj gestisc w kg/m^3')
            setattr(stozek, 'gestosc', tylkoliczbydodatnie())
        print('masa = ', round(stozek.masa(), 2), 'kg')
    zatwierdz()


def wyswczworoscian(wyboruzytkownikaparametr):
    czworoscian = Czworoscian()
    if czworoscian.bok == -1:
        print('podaj dlugosc boku w metrach')
        setattr(czworoscian, 'bok', tylkoliczbydodatnie())
    if wyboruzytkownikaparametr == 'pole':
        print('pole = ', round(czworoscian.pole(), 2), 'm^2')
    elif wyboruzytkownikaparametr == 'objetosc':
        print('objetosc = ', round(czworoscian.objetosc(), 2), 'm^3')
    elif wyboruzytkownikaparametr == 'masa':
        if czworoscian.gestosc == -1:
            print('podaj gestisc w kg/m^3')
            setattr(czworoscian, 'gestosc', tylkoliczbydodatnie())
        print('masa = ', round(czworoscian.masa(), 2), 'kg')
    zatwierdz()


def wyswwalec(wyboruzytkownikaparametr):
    walec = Walec()
    if walec.r == -1:
        print('podaj promien w metrach')
        setattr(walec, 'r', tylkoliczbydodatnie())
        print('podaj wysokosc w metrach')
        setattr(walec, 'h', tylkoliczbydodatnie())
    if wyboruzytkownikaparametr == 'pole':
        print('pole = ', round(walec.pole(), 2), 'm^2')
    elif wyboruzytkownikaparametr == 'objetosc':
        print('objetosc = ', round(walec.objetosc(), 2), 'm^3')
    elif wyboruzytkownikaparametr == 'masa':
        if walec.gestosc == -1:
            print('podaj gestisc w kg/m^3')
            setattr(walec, 'gestosc', tylkoliczbydodatnie())
        print('masa = ', round(walec.masa(), 2), 'kg')
    zatwierdz()


def wyswostroslup(wyboruzytkownikaparametr):
    ostroslup = Ostroslup()
    if ostroslup.a == -1:
        print('podaj bok a w metrach')
        setattr(ostroslup, 'a', tylkoliczbydodatnie())
        print('podaj bok b w metrach')
        setattr(ostroslup, 'b', tylkoliczbydodatnie())
        print('podaj wysokosc w metrach')
        setattr(ostroslup, 'h', tylkoliczbydodatnie())
    if wyboruzytkownikaparametr == 'pole':
        print('pole = ', round(ostroslup.pole(), 2), 'm^2')
    elif wyboruzytkownikaparametr == 'objetosc':
        print('objetosc = ', round(ostroslup.objetosc(), 2), 'm^3')
    elif wyboruzytkownikaparametr == 'masa':
        if ostroslup.gestosc == -1:
            print('podaj gestisc w kg/m^3')
            setattr(ostroslup, 'gestosc', tylkoliczbydodatnie())
        print('masa = ', round(ostroslup.masa(), 2), 'kg')
    zatwierdz()


def wyswelipsoida(wyboruzytkownikaparametr):
    elipsoida = Elipsoida()
    if elipsoida.a == -1:
        print('podaj promien a w metrach')
        setattr(elipsoida, 'a', tylkoliczbydodatnie())
        print('podaj promien b w metrach')
        setattr(elipsoida, 'b', tylkoliczbydodatnie())
        print('podaj promien c w metrach')
        setattr(elipsoida, 'c', tylkoliczbydodatnie())
    if wyboruzytkownikaparametr == 'pole':
        x = round(elipsoida.pole(), 2)
        if x == -1:
            zatwierdz()
        print('pole = ', x, 'm^2')
    elif wyboruzytkownikaparametr == 'objetosc':
        print('objetosc = ', round(elipsoida.objetosc(), 2), 'm^3')
    elif wyboruzytkownikaparametr == 'masa':
        if elipsoida.gestosc == -1:
            print('podaj gestisc w kg/m^3')
            setattr(elipsoida, 'gestosc', tylkoliczbydodatnie())
        print('masa = ', round(elipsoida.masa(), 2), 'kg')
    zatwierdz()


start()
