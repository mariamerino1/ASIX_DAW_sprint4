# 📋 Projecte CRUD de Tasques amb FastAPI + MongoDB + Frontend senzill

Aquest projecte és un exemple educatiu d'una aplicació web **CRUD** completa per gestionar una llista de tasques.

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

- **FastAPI** (backend)
- **MongoDB** (base de dades)
- **Motor** (driver async per MongoDB)
- **HTML + CSS + JavaScript** (frontend senzill)
- **Apidog** (per testeig d'API)

---

## ▶️ Instruccions d'execució

### 1. Arrencar el backend

Assegura't que MongoDB està actiu a `mongodb://localhost:27017`

```bash
cd backend
uvicorn main:app --reload
```

L'API estarà disponible a: [http://localhost:8000](http://localhost:8000)

### 2. Obrir el frontend

Obre el fitxer `frontend/index.html` en el navegador o utilitza **Live Server** a VS Code.

---

## 🧪 Testejar l'API amb Apidog

1. Obre Apidog i crea un projecte nou.
2. Importa la col·lecció: `tests/apidog_tasques_fastapi_collection.json`
3. Executa els endpoints:
   - `GET /tasques`
   - `POST /tasques` (amb generació automàtica de títol)
   - `PUT /tasques/:id`
   - `DELETE /tasques/:id`
4. El POST desa l'`id` global per poder-lo fer servir en PUT i DELETE.

---

## 🧠 Extensió (idees de millora)

- Afegir un camp `completada` a les tasques.
- Implementar l'opció d'**editar** des del frontend.
- Validació de formulari abans d'enviar.
- Disseny responsive amb CSS modern.

---

## 📂 Recursos

- [Guia test Apidog (PDF)](guia_test_apidog_fastapi.pdf)
- [Guia ús Frontend (PDF)](guia_frontend_api_fastapi.pdf)
- [Guia importació col·lecció Apidog (PDF)](guia_importar_apidog_fastapi.pdf)

---

## 🙌 Autoria

Exercici pensat per a l'aprenentatge de desenvolupament web full-stack en un cicle formatiu.
