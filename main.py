from fastapi import FastAPI
import pandas as pd
Ultimate_df= pd.read_csv('datos-transformados.csv')
ml_matrix_df=pd.read_csv('ml_matrix.csv')
import ast
app=FastAPI(tittle= "Proyecto 1 - Soy Henry")

@app.get("/")
def presentacion():
    return {"PI 01 - Juan Amador Arrieta Barragan"}

@app.get("/contacto")
def contacto():
    return "Email: juansamadors@gmail.com / Github: juan1401123"



@app.get('/peliculas_mes/{mes}',tags=['Peliculas por Mes'])
def peliculas_mes(mes:str):
    meses={'Enero':1,'Febrero':2,'Marzo':3,'Abril':4,'Mayo':5,'Junio':6,'Julio':7,'Agosto':8,'Septiembre':9,'Octubre':10,'Noviembre':11,'Diciembre':12}

    dfm=Ultimate_df[Ultimate_df['release_month']==meses[mes]]
    return 'mes:'+mes+' cantidad:'+str(len(dfm))

@app.get('/peliculas_dia/{dia}',tags=['Peliculas por Dia'])
def peliculas_dia(dia:str):
    dfd=Ultimate_df[Ultimate_df['Día']==dia]
    return 'dia:'+dia+' '+' cantidad:'+ str(len(dfd))

@app.get('/franquicia/{franquicia}',tags=['Ganancia Total por Franquicia'])
def franquicia(franquicia:str):
    dff=Ultimate_df[Ultimate_df['belongs_to_collection_name']==franquicia]
    dff=dff[dff['revenue']>1]
    if len(dff)>1:
     return 'Franquicia:'+franquicia+' Cantidad:'+ str(len(dff))+' Ganancia Total:'+str(sum(dff['revenue']))+' Ganancia Promedio:'+str(sum(dff['revenue'])/len(dff))
    else:
       return 'No hay registros de las ganancias de esta franquicia en la base de datos'


@app.get('/peliculas_pais/{pais}',tags=['Peliculas por Pais'])
def peliculas_pais(pais:str):
    counter=0
    for i in Ultimate_df['production_countries_name'].apply(lambda x:ast.literal_eval(x)):
        if isinstance(i,list):
             for e in i:
                if e==pais:
                    counter+=1
    return 'pais:'+str(pais)+' cantidad:' +str(counter)    


@app.get('/productoras/{productora}',tags=['Ganancia Total por productora'])
def productoras(productora:str):
    counter=0
    sumar=0
    for index,i in enumerate(Ultimate_df['production_companies_name'].apply(lambda x:ast.literal_eval(x))):
     if isinstance(i,list):
        for e in i:
            if e==productora:
               counter+=1
               sumar+=Ultimate_df['revenue'][index]
    return 'productora:'+productora+' ganancia total:'+ str(sumar)+' cantidad:'+ str(counter)


@app.get('/retorno/{pelicula}',tags=['Ganancia y Retorno por Pelicula'])
def retorno(pelicula:str):
   pdf=Ultimate_df[Ultimate_df['title']==pelicula]
   return 'pelicula:'+pelicula+' inversion:'+str(pdf.budget.values[0])+' ganancia:'+str(pdf.revenue.values[0])+' retorno:'+str(pdf['return'].values[0])+' anio:'+str(pdf['release_year'].values[0])

@app.get('/recomendacion/{titulo}',tags=['Recomendacion de Peliculas Similares'])
def recomendacion(titulo:str):
  arr=[]
  for i in ml_matrix_df[titulo].sort_values(ascending=False).head(6).index[1:6].to_list():
     arr.append(ml_matrix_df['title'][i])
  return arr