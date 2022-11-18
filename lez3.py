#8/10 -> manca caso
def sum_csv(file_name):
    values = [] # variabile per memorizzare i dati da sommare
    
    file=open(file_name, 'r')

    vuoto = True
    
    for line in file:
        elements = line.split(',')
        
        if elements[0]!='Date': 
            value = elements[1]
    
            value=float(value)
            values.append(value)
            vuoto = False
            
    if vuoto == False:
        return sum(values)
    else:
        return None
    
    file.close()

print(sum_csv('shampoo_sales.csv')) 
print(sum_csv('empty_file.csv'))
#print(sum_csv('text_test.csv'))