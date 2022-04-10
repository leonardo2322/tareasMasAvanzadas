from numpy import index_exp
import pandas as pd


data = [5,2,25]
friends = ['Noa','Noe','Leonardo']
ide = ["ar0","ar2","ar3"]
dict_data = {
    'Nombres':friends,
    'Edad':data
}
data  = pd.read_json('/home/hidden/Documentos/poblacion.json')
    

data_sets = pd.DataFrame(dict_data,index=ide)
a = []
for i in range(0,6,2):
    a.append(i)

data_sets['dias'] = a # de esta manera se agg un nueva columna


print(data_sets)
print(data.head())

