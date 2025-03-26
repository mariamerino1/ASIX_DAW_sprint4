const apiUrl = "http://localhost:8000/tasques";

async function carregarTasques() {
  const res = await fetch(apiUrl);
  const tasques = await res.json();
  const llista = document.getElementById("tasca-list");
  llista.innerHTML = "";
  tasques.forEach(t => {
    const li = document.createElement("li");
    li.textContent = `${t.title}: ${t.description}`;
    const btn = document.createElement("button");
    btn.textContent = "❌";
    btn.onclick = () => eliminarTasca(t.id);
    li.appendChild(btn);
    llista.appendChild(li);
  });
}

async function afegirTasca(e) {
  e.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  await fetch(apiUrl, {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ title, description })
  });
  e.target.reset();
  carregarTasques();
}

async function eliminarTasca(id) {
  await fetch(`${apiUrl}/${id}`, { method: "DELETE" });
  carregarTasques();
}

document.getElementById("tasca-form").addEventListener("submit", afegirTasca);
carregarTasques();