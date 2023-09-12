class Auto:
    marca = ""
    modelo = 2004
    placa = ""

taxi = Auto()
print(taxi.modelo)

police = Auto()
print(police.modelo)

class Jugadores_A:
    j1 = "messi"
    j2 = "Ronaldo"

class Jugadores_B:
    j3 = "Marcelo"
    j1 = "Falcao"
print(Jugadores_B.j1)

class nombre:
    pass

victor = nombre()
mauricio = nombre()

#objeto.atributo = valor

victor.edad = 30
victor.sexo = "M"
victor.pais = "Perú"

mauricio.edad = 22
mauricio.sexo = "M"
mauricio.pais = "Chile"

print(mauricio.edad)
print(victor.edad)
print(mauricio.pais)
print(victor.pais)