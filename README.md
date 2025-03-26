# 📋 Projecte CRUD de Tasques amb FastAPI + MongoDB + Frontend senzill

Aquest projecte és un exemple educatiu d'una aplicació web **CRUD** completa per gestionar una llista de tasques.
Per utilitzar-lo, tenir el docker de monodb server funcionant.
I crear un entorn virtual de python per instal.lar i recordar activar-lo cada cop que poseu en marxa uvicorn.

## 🧱 Estructura del projecte

```
crud_tasques/
├── backend/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── crud.py
│   └── database.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── tests/
│   └── apidog_tasques_fastapi_collection.json
├── requirements.txt
```

## 🚀 Tecnologies utilitzades

- **MongoDB server** (SGBD)
- **FastAPI** (backend)
- **Motor** (driver async per MongoDB)
- **HTML + CSS + JavaScript** (frontend senzill)
- **Apidog** (per testeig d'API)

## ▶️ Instruccions d'execució

### 1. Arrencar el backend
```bash
cd backend
uvicorn main:app --reload
```
L'API estarà disponible a: [http://localhost:8000](http://localhost:8000)

### 2. Obrir el frontend
Obre el fitxer `frontend/index.html` en el navegador o utilitza **Live Server** a VS Code.

## 🧪 Testejar l'API amb Apidog

1. Obre Apidog i crea un projecte nou.
2. Importa la col·lecció: `tests/apidog_tasques_fastapi_collection.json`
3. Executa els endpoints:
   - `GET /tasques`
   - `POST /tasques`
   - `PUT /tasques/:id`
   - `DELETE /tasques/:id`

## 🧠 Extensió (idees de millora)

- Afegir un camp `completada` a les tasques.
- Implementar l'opció d'**editar** des del frontend.
- Validació de formulari abans d'enviar.
- Disseny responsive amb CSS modern.

## 📂 Recursos

- [Explicació codi FastApi](docs/explicacio_fastapi.md)
- [Guia test Apidog](docs/guia_test_apidog.md)
- [Guia ús Frontend](docs/guia_frontend.md)
- [Guia importació Apidog](docs/guia_import_apidog.md)

## 🙌 Autoria

Exercici pensat per a l'aprenentatge de desenvolupament web full-stack en un cicle formatiu.
