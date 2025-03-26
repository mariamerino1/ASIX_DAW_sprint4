# 🧠 Explicació del codi FastAPI

Aquest document explica els components del projecte backend desenvolupat amb **FastAPI** i **MongoDB**.

---

## 📁 Fitxer: `main.py`

Aquest és el punt d'entrada de l'aplicació FastAPI.

### Funcions principals:
- Crear la instància `app`
- Afegir middleware CORS
- Importar i registrar les rutes

```python
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
```

---

## 📁 Fitxer: `routes.py`

Conté les rutes de l’API per gestionar les tasques (GET, POST, PUT, DELETE).

### Exemple:
```python
@router.get("/tasques")
async def llegir_tasques():
    return await get_all_tasques()
```

### Altres rutes:
- `POST /tasques`: crea una nova tasca
- `PUT /tasques/{id}`: actualitza una tasca
- `DELETE /tasques/{id}`: elimina una tasca

---

## 📁 Fitxer: `models.py`

Defineix el model de dades usant Pydantic.

```python
class Tasca(BaseModel):
    title: str
    description: str
```

Aquest model serveix per validar les dades rebudes i enviades.

---

## 📁 Fitxer: `crud.py`

Conté la lògica per interactuar amb la base de dades MongoDB.

### Funcions destacades:
- `get_all_tasques()`: retorna totes les tasques
- `create_tasca(tasca)`: afegeix una nova tasca
- `update_tasca(id, tasca)`: modifica una tasca existent
- `delete_tasca(id)`: elimina una tasca

### Exemple:
```python
async def create_tasca(tasca: Tasca):
    result = await collection.insert_one(tasca.dict())
    return await collection.find_one({"_id": result.inserted_id})
```

---

## 📁 Fitxer: `database.py`

Crea la connexió amb MongoDB utilitzant `motor` (driver async).

```python
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["tasques_db"]
```

---

## ✅ Resum

| Fitxer          | Funció principal                                     |
|-----------------|------------------------------------------------------|
| `main.py`       | Inicia l'app i registra les rutes                    |
| `routes.py`     | Defineix les rutes de l'API                          |
| `models.py`     | Model de dades amb validació                         |
| `crud.py`       | Operacions CRUD amb MongoDB                          |
| `database.py`   | Connexió amb la base de dades                        |

Aquest esquema permet separar responsabilitats i mantenir un codi net i modular.
