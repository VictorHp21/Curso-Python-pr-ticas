var = input('Digite algo:')

print('O tipo primitivo desse valor é:' , type(var))

print('So tem espaço?', var.isspace())

print('è um número?', var.isnumeric())

print('é alfabetico?', var.isalpha())

print('é alfanumerico?', var.isalnum())

print('Esta em maiuscula?', var.isupper())

print('Esta em minuscula?', var.islower())

print('Esta capitalizada?', var.istitle())