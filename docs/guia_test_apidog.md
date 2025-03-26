# 🧪 Guia test Apidog (FastAPI)

## 1. Inicia el servidor FastAPI
```bash
uvicorn backend.main:app --reload
```
API disponible a: `http://localhost:8000`

## 2. Obre Apidog i crea un projecte nou
- Dona-li un nom (ex: `Tasques FastAPI`)
- Configura la **Base URL**: `http://localhost:8000`

## 3. Afegeix endpoints

### `GET /tasques`
- Mètode: `GET`
- Comprova que torna una array de tasques

### `POST /tasques`
- Mètode: `POST`
- Cos (JSON):
```json
{
  "title": "Exemple",
  "description": "Tasca d'exemple"
}
```

### `PUT /tasques/{id}`
- Mètode: `PUT`
- Cos (JSON):
```json
{
  "title": "Actualitzat",
  "description": "Descripció nova"
}
```

### `DELETE /tasques/{id}`
- Mètode: `DELETE`

## 4. Scripts útils

### Test Script per GET:
```js
pm.test("Codi 200", () => {
  pm.response.to.have.status(200);
});
pm.test("És una array", () => {
  pm.expect(Array.isArray(pm.response.json())).to.be.true;
});
```

### Guardar ID després de POST:
```js
const jsonData = pm.response.json();
pm.globals.set("tasca_id", jsonData.id);
```
