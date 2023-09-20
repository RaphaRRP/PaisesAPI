from typing import Optional
from pydantic import BaseModel

class Pais(BaseModel):
    id: Optional[int] = None
    nome: str
    territorio: int
    populacao: int
    capital: str
    idioma: str
    moeda: str
    continente: str


paises = [
    Pais(id=1, nome="Brasil", territorio=8515767, populacao=212559417, capital="Brasília", idioma="Português", moeda="Real", continente="América do Sul"),
    Pais(id=2, nome="Estados Unidos", territorio=9372610, populacao=331002651, capital="Washington, D.C.", idioma="Inglês", moeda="Dólar", continente="América do Norte"),
    Pais(id=3, nome="Índia", territorio=3287263, populacao=1380004385, capital="Nova Deli", idioma="Hindi e Inglês", moeda="Rúpia Indiana", continente="Ásia"),
    Pais(id=4, nome="Canadá", territorio=9984670, populacao=37742154, capital="Ottawa", idioma="Inglês e Francês", moeda="Dólar Canadense", continente="América do Norte"),
    Pais(id=5, nome="Austrália", territorio=7692024, populacao=257883197, capital="Camberra", idioma="Inglês", moeda="Dólar Australiano", continente="Oceania"),
    Pais(id=6, nome="Rússia", territorio=17125200, populacao=145912025, capital="Moscou", idioma="Russo", moeda="Rublo", continente="Europa e Ásia"),
    Pais(id=7, nome="China", territorio=9596960, populacao=1444216107, capital="Pequim", idioma="Mandarim", moeda="Renminbi (Yuan)", continente="Ásia"),
    Pais(id=8, nome="Japão", territorio=377975, populacao=126476461, capital="Tóquio", idioma="Japonês", moeda="Iene", continente="Ásia"),
    Pais(id=9, nome="Argentina", territorio=2780400, populacao=45195777, capital="Buenos Aires", idioma="Espanhol", moeda="Peso Argentino", continente="América do Sul"),
    Pais(id=10, nome="Reino Unido", territorio=242495, populacao=67886011, capital="Londres", idioma="Inglês", moeda="Libra Esterlina", continente="Europa"),
    Pais(id=11, nome="França", territorio=551695, populacao=65273511, capital="Paris", idioma="Francês", moeda="Euro", continente="Europa"),
    Pais(id=12, nome="Alemanha", territorio=357022, populacao=83783942, capital="Berlim", idioma="Alemão", moeda="Euro", continente="Europa"),
    Pais(id=13, nome="Espanha", territorio=505990, populacao=46754778, capital="Madri", idioma="Espanhol", moeda="Euro", continente="Europa"),
    Pais(id=14, nome="Itália", territorio=301340, populacao=60461826, capital="Roma", idioma="Italiano", moeda="Euro", continente="Europa"),
    Pais(id=15, nome="México", territorio=1964375, populacao=126190788, capital="Cidade do México", idioma="Espanhol", moeda="Peso Mexicano", continente="América do Norte"),
    Pais(id=16, nome="Colômbia", territorio=1141748, populacao=50882891, capital="Bogotá", idioma="Espanhol", moeda="Peso Colombiano", continente="América do Sul")]

