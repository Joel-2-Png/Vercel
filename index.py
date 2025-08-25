from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def formulaire():
    return """
    <html>
        <body>
            <h2>Formulaire d'inscription</h2>
            <form action="/submit" method="post">
                <input type="text" name="nom" placeholder="Nom" required><br><br>
                <input type="text" name="prenom" placeholder="Prénom" required><br><br>
                <input type="email" name="email" placeholder="Email" required><br><br>
                <input type="password" name="password" placeholder="Mot de passe" required><br><br>
                <button type="submit">S'inscrire</button>
            </form>
        </body>
    </html>
    """

@app.post("/submit", response_class=HTMLResponse)
def submit(nom: str = Form(...), prenom: str = Form(...), email: str = Form(...), password: str = Form(...)):
    return f"""
    <html>
        <body>
            <h2>Inscription réussie ✅</h2>
            <p><b>Nom :</b> {nom}</p>
            <p><b>Prénom :</b> {prenom}</p>
            <p><b>Email :</b> {email}</p>
        </body>
    </html>
    """
