# 🌐 Guia ús del Frontend

## 1. Inicia el backend:
```bash
uvicorn backend.main:app --reload
```

## 2. Obre el frontend:
Obre `frontend/index.html` amb el navegador o amb **Live Server** (VS Code).

## 3. Com funciona:
- `GET /tasques` es fa en carregar
- El formulari envia un `POST`
- El botó d'eliminar fa `DELETE`
- Cada acció refresca la llista automàticament

## 4. Arxius clau:
- `index.html` – estructura
- `style.css` – estils
- `script.js` – interaccions amb l’API
