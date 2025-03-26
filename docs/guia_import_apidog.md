# 📂 Guia per importar la col·lecció Apidog

## 1. Obre Apidog

- Si no tens Apidog instal·lat: https://apidog.com
- Obre l'aplicació

## 2. Crea un projecte nou
- Clica `New Project`
- Dona-li nom: *Tasques FastAPI*

## 3. Importa la col·lecció
- Ves a `Import > Import Collection`
- Selecciona: `tests/apidog_tasques_fastapi_collection.json`

## 4. Executa les peticions
- `GET /tasques`
- `POST /tasques` (amb títol aleatori)
- `PUT /tasques/{{tasca_id}}`
- `DELETE /tasques/{{tasca_id}}`

## 5. Scripts automatitzats
- El `POST` desa l'`id` com a variable global (`tasca_id`)
- El `PUT` i `DELETE` la reutilitzen
