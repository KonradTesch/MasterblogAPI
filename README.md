# Flask Blog API

Eine einfache REST API für Blog-Posts mit Flask Backend und HTML/JavaScript Frontend.

## 📋 Features

- **CRUD Operationen**: Erstellen, Lesen, Aktualisieren und Löschen von Blog-Posts
- **Suchfunktion**: Suche nach Posts basierend auf Titel und/oder Inhalt
- **Sortierung**: Posts nach Titel oder Inhalt sortieren (aufsteigend/absteigend)
- **Web Frontend**: Benutzerfreundliche HTML-Oberfläche
- **CORS Support**: Cross-Origin Resource Sharing aktiviert
- **Error Handling**: Umfassendes Fehlerbehandlungssystem

## 🚀 Installation & Setup

### Voraussetzungen

- Python 3.7+
- pip

### Installation

**Abhängigkeiten installieren**
   ```bash
   pip install flask flask-cors
   ```

### Anwendung starten

1. **Backend starten** (Terminal 1):
   ```bash
   python backend_app.py
   ```
   Das Backend läuft auf: `http://127.0.0.1:5002`

2. **Frontend starten** (Terminal 2):
   ```bash
   python frontend_app.py
   ```
   Das Frontend läuft auf: `http://127.0.0.1:5001`

3. **Anwendung öffnen**
   
   Öffnen Sie Ihren Browser und navigieren Sie zu: `http://127.0.0.1:5001`

## 📖 API Dokumentation

### Base URL
```
http://127.0.0.1:5002/api
```

### Endpoints

#### 🔍 Alle Posts abrufen
```http
GET /posts
```

**Query Parameter:**
- `sort` (optional): `title` oder `content`
- `direction` (optional): `asc` oder `desc` (Standard: `asc`)

**Beispiel:**
```bash
curl "http://127.0.0.1:5002/api/posts?sort=title&direction=desc"
```

#### ➕ Neuen Post erstellen
```http
POST /posts
```

**Request Body:**
```json
{
  "title": "Mein neuer Post",
  "content": "Das ist der Inhalt meines Posts."
}
```

#### 🗑️ Post löschen
```http
DELETE /posts/{id}
```

#### ✏️ Post aktualisieren
```http
PUT /posts/{id}

```

**Request Body:**
```json
{
  "title(optional)": "Aktualisierter Titel",
  "content(optional)": "Aktualisierter Inhalt"
}
```

#### 🔍 Posts suchen
```http
GET /posts/search
```

**Query Parameter:**
- `title` (optional): Suchtext für Titel
- `content` (optional): Suchtext für Inhalt

**Beispiel:**
```bash
curl "http://127.0.0.1:5002/api/posts/search?title=first&content=post"
```

### HTTP Status Codes

| Code | Bedeutung |
|------|-----------|
| 200  | OK - Anfrage erfolgreich |
| 201  | Created - Ressource erstellt |
| 400  | Bad Request - Ungültige Anfrage |
| 404  | Not Found - Ressource nicht gefunden |
| 405  | Method Not Allowed - HTTP-Methode nicht erlaubt |
| 415  | Unsupported Media Type - Falscher Content-Type |

## 💻 Frontend Nutzung

1. **API Base URL einstellen**: Standardmäßig auf `http://127.0.0.1:5002/api` gesetzt
2. **Posts laden**: Klicken Sie auf "Load Posts" um alle Posts anzuzeigen
3. **Post hinzufügen**: Titel und Inhalt eingeben, dann "Add Post" klicken
4. **Post löschen**: "Delete" Button beim entsprechenden Post klicken

## 🧪 Testing

Testen Sie die API mit curl oder einem API-Client wie Postman:

```bash
# Alle Posts abrufen
curl http://127.0.0.1:5002/api/posts

# Neuen Post erstellen
curl -X POST http://127.0.0.1:5002/api/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Post", "content": "Test Content"}'

# Post suchen
curl "http://127.0.0.1:5002/api/posts/search?title=Test"
```
---

**Created by** Konrad Tesch
