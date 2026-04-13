import matplotlib.pyplot as plt


x = [1,2,3,4,5]
y = [10,15,13,20,17]

# 1. Wykres liniowy

# plt.plot(
#     x,
#     y,
#     color="green",
#     linewidth=3,
#     marker="o",
#     markersize=10,
# ) # wybór wykresu
# plt.title("Wykres liniowy")
# plt.xlabel("Numer dnia")
# plt.ylabel("Wartość sprzedaży")
#
# plt.show() # przywołanie / aktywowanie wykresu


produkty = ["A","B","C","D"]
wyniki = [12,19,7,15]

# plt.bar(produkty, wyniki)
# plt.barh(produkty,wyniki)
# plt.title("Wykres słupkowy")
# plt.xlabel("produkty")
# plt.ylabel("liczba sztuk")
# plt.show()

oceny = [ 2,4,5,2,3,4,5,4,3,2,3,4,5]

# plt.hist(oceny, bins=4)
# plt.title("Histogram ocen")
# plt.xlabel("Ocena")
# plt.ylabel("Liczba wystąpień")
# plt.show()


etykiety = ["Python", "Java","C++", "Javascript"]
wartosci = [40,25,15,20]

# plt.pie(wartosci, labels=etykiety, autopct=lambda p: round(p))
# plt.title("Udział języków programowania")
# plt.show()

a = [1,2,3,4,5]
b = [3,7,4,9,6]

# plt.scatter(a,b)
# plt.title("Wykres punktowy")
# plt.xlabel("Liczba godzin nauki")
# plt.ylabel("Ilość pkt na teście")
# plt.show()

dni = [1,2,3,4,5]
sprzedaz = [10,12,15,14,18]
koszty = [6,7,8,7,9]

# plt.plot(dni, sprzedaz, label="Sprzedaz")
# plt.plot(dni, koszty, label="Koszty")
# plt.title("Sprzedaż i koszty")
# plt.xlabel("Dzień")
# plt.ylabel("Kwota")
# plt.legend()
# plt.ylim(top=30, bottom=-30)
# plt.show()

# dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
# sprzedaz = [120, 150, 180, 160, 170, 210, 190]
# plt.plot(dni, sprzedaz, marker='o')
# plt.title("Sprzedaż sklepu w kolejnych dniach tygodnia")
# plt.xlabel("Dni tygodnia")
# plt.ylabel("Sprzedaż")
# plt.grid(True)
#
# plt.show()


# zad2
# produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
# sprzedaz = [25, 18, 40, 12]
#
# plt.bar(produkty, sprzedaz)
# plt.title("Sprzedaż czterech produktów")
# plt.xlabel("Produkty")
# plt.ylabel("Liczba sprzedanych sztuk")
# plt.show()

#zad3
# wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]
#
# plt.hist(wyniki, bins=5, edgecolor='black')
# plt.title("Rozkład wyników testu studentów")
# plt.xlabel("Wyniki")
# plt.ylabel("Liczba studentów")
# plt.show()