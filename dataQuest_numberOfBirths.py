#funcion que lee el archivo y lo organiza en lista anidada para el analisis retorna la lista anidada
# recibe el archivo y si tiene o no encabezado (bool)
def read_csv(filename,header_row = False): 
    file = open(filename).read()  
    rows = file.split('\n')
    if header_row == True:
        rows = rows[1:]   
    birth_list = []
    for el in rows:
        splitList = el.split(',')
        int_fields = []
        for each in splitList:
            int_fields.append(int(each))
        birth_list.append(int_fields)
    return(birth_list)

final_list = read_csv('US_births_2000-2014_SSA.csv',True)
# print(final_list[0:10])

# funcion que cuenta el numero de nacimientos que hay por año/mes/dia de la semana y los devuelve en un diccionario
# recibe una lista y un indice(int)
def birthCounter(lista,index):
    libro = {}
    for each in lista:
        fecha = each[index]
        nacimiento = each[4]
        if fecha in libro:
            libro[fecha] = libro[fecha] + nacimiento
        else:
            libro[fecha] = nacimiento
    return(libro)

#funcion que imprime los valores maximo y minimo, recibe un diccionario
def min_max_calc(dict):
    minimo = min(dict.keys(), key=(lambda k: dict[k])) 
    maximo = max(dict.keys(), key=(lambda k: dict[k]))
    print('Min Value: {} {}'.format(minimo,dict[minimo]))
    print('Max Value: {} {}'.format(maximo,dict[maximo]))

#funcion que devuelve lista de valores unicos, recibe una lista y un indice(int)
def uniqueLists(lista,index):
    unique_list = []
    for el in lista:
        if el[index] not in unique_list:
            unique_list.append(el[index])
    return unique_list

#funcion que retorna lista con valores de nacimiento atraves de los años en una fecha especifica, recibe una lista, indice de fecha(int) y un indice especifico(int)
def changeCalc(lista,date_index,specific_index):
    unique_years = uniqueLists(lista,0) # crea una lista de años sin repetirse
    lista_cambio = []
    for el in unique_years:
        births = 0
        for each in lista:
            if el == each[0]:
                if each[date_index] == specific_index:
                    year = each[0]
                    fecha = each[date_index]
                    births += each[4]
        aux_list = [year,fecha,births]
        lista_cambio.append(aux_list)
    return lista_cambio


cambio_dow = changeCalc(final_list,2,29)
print(cambio_dow)
# unique_years = uniqueLists(final_list,0)
# print(unique_years)
    
# births_year = birthCounter(final_list,0)
# min_max_calc(births_year)
# print(births_year)

# births_month = birthCounter(final_list,1)
# min_max_calc(births_month)

# births_day = birthCounter(final_list,2)
# min_max_calc(births_day)

# births_dayOfWeek = birthCounter(final_list,3)
# min_max_calc(births_dayOfWeek)

# [[year,dow,births],[1994,1,20k],[1995,1,20k]]