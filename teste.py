from funcoes import letras_certas

# -------------------------------------------------------

chute_teste = "iooooo"
gabarito_teste = "ínsper"

x = letras_certas(chute_teste, gabarito_teste)
assert x == "Í_____"

# ----------------------------------------------------------

chute_teste = "iieiii"
gabarito_teste = "eiooei"

x = letras_certas(chute_teste, gabarito_teste)

assert x == "_Ie__I"

# ----------------------------------------------------------

chute_teste = "insper"
gabarito_teste = "Ínsper"

x = letras_certas(chute_teste, gabarito_teste)
assert x == "ÍNSPER"

# ----------------------------------------------------------
chute_teste = "qqeiei"
gabarito_teste = "eíntei"

x = letras_certas(chute_teste, gabarito_teste)
assert x == "__eiEI"

# ----------------------------------------------------------
x = letras_certas("eeieii", "iiieee")
assert x == "eeIEii"