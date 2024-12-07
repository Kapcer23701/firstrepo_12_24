from faker import Faker

#inicjalizacja generatora faker
fake = Faker()

def generuj_dane_testowe(liczba_uzytkownikow):
    dane = []

    for i in range(liczba_uzytkownikow):
        uzytkownik = {
            "imie": fake.first_name(),
            "email": fake.email(),
            "wiek": fake.year(),
        }
        dane.append(uzytkownik)

    return dane

#generacja 10 użytkownikow
print(generuj_dane_testowe(10))