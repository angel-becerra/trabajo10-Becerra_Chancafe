import libreria

assert (libreria.validar_byte("hola") == False)
assert (libreria.validar_byte("1") == False)
assert (libreria.validar_byte("1111111") == False)
assert (libreria.validar_byte("ABCDEFGH") == False)
assert (libreria.validar_byte("1111111F") == False)
assert (libreria.validar_byte("11111112") == False)
assert (libreria.validar_byte("22222222") == False)
assert (libreria.validar_byte("30000000") == False)
assert (libreria.validar_byte("00005000") == False)
assert (libreria.validar_byte("00000000") == True)
assert (libreria.validar_byte("11111111") == True)
assert (libreria.validar_byte("00001111") == True)
assert (libreria.validar_byte("11110000") == True)
print("validar_byte ok")

assert (libreria.mascara("0","0") == "0")
assert (libreria.mascara("1","0") == "0")
assert (libreria.mascara("0","1") == "0")
assert (libreria.mascara("1","1") == "1")
print("mascara ok")

assert (libreria.enmascarar("00000000","00000000") == "00000000")
assert (libreria.enmascarar("11111111","11111111") == "11111111")
assert (libreria.enmascarar("11110000","11110000") == "11110000")
print("enmascarar OK")



import libreria

assert (libreria.validar_ip("adf") == False)
assert (libreria.validar_ip("182 192 192 491") == False)
assert (libreria.validar_ip("182.491") == False)
assert (libreria.validar_ip("182.491.") == False)
assert (libreria.validar_ip("A.B.C.D") == False)
assert (libreria.validar_ip("10.9.8.D") == False)
assert (libreria.validar_ip("10.9.A.1") == False)
assert (libreria.validar_ip("10.B.0.1") == False)
assert (libreria.validar_ip("1A.1.0.1") == False)
assert (libreria.validar_ip("900.500.600.300") == False)
assert (libreria.validar_ip("9.5.6.300") == False)
assert (libreria.validar_ip("256.256.256.256") == False)
assert (libreria.validar_ip("25.256.2.25") == False)
assert (libreria.validar_ip("259.2.2.25") == False)
assert (libreria.validar_ip("127.0.0.1") == True)
assert (libreria.validar_ip("255.255.255.255") == True)
assert (libreria.validar_ip("0.0.0.0") == True)
assert (libreria.validar_ip("16.0.23.14") == True)
print("validar_ip ok")
