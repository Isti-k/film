import Faljbeolvas

lista=Faljbeolvas.faljbeolvasas()
legrov=Faljbeolvas.legrovidebb_film(lista)
print(f"A legrövidebb film:{lista[legrov].cím}")
legalabb=Faljbeolvas.legalabb110p(lista)
print(f"Legalább {legalabb}db 110p-es film van.")
film=Faljbeolvas.filmbeker(lista)
print(film)
Faljbeolvas.falj_kiir(lista,film)






