from fastapi import FastAPI, HTTPException, status, Path, Query, Header, Depends
from fastapi.responses import JSONResponse
from models import Pais, paises
from typing import List, Optional, Any, Dict
from time import sleep





app = FastAPI(
    title='Documentação',
    version='0.0.1',
    description='Api sobre Países'
    )   


@app.get('/paises', description='retorna os paises')
async def get_paises():
    return paises


@app.get('/paises/{pais_id}', description='retorna um pais pelo id')
async def get_pais(pais_id: int):
    try:
        pais = paises[pais_id - 1]
        print(pais)
        return pais
    
    except KeyError:
        raise HTTPException(status_code=404, detail='Pais não encontrado')
    
    
@app.post('/paises', status_code=201)
async def post_pais(pais: Pais):
    next_id: int = len(paises) + 1
    pais.id = next_id
    paises.append(pais)
    return pais

@app.put('/paises/{pais_id}')
async def put_pais(pais_id: int, pais: Pais):
    if paises[pais_id - 1] in paises:
        paises[pais_id - 1] = pais
        pais.id = pais_id
        return pais

    else:
        raise HTTPException(status_code=404, detail='País não encontrado')
    

@app.delete('/paises/{pais_id}')
async def get_pais(pais_id: int):
    if paises[pais_id - 1] in paises:
        paises[pais_id - 1] = {"id": pais_id, "status": "PAÍS DELETADO"}
        return paises
    else:
        raise HTTPException(status_code=404, detail='País não encontrado')

    




if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)