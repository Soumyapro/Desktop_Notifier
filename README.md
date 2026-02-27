# Desktop Notifier

A Python application that fetches the latest top news headlines from [NewsAPI](https://newsapi.org/) and displays them as desktop notifications.

---

## How It Works

1. `news.py` fetches the top headlines for a given country using the NewsAPI and saves the response to a local `news.json` file.
2. `desktop.py` reads the `news.json` file and displays the first article's title and description as a native desktop notification.

---

## Getting Started

### Prerequisites

- Python 3.x
- A free API key from [https://newsapi.org/](https://newsapi.org/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Soumyapro/Desktop_Notifier.git
   cd Desktop_Notifier
   ```

2. **Install dependencies**
   ```bash
   pip install requests plyer python-dotenv
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```env
   API_KEY=newsapi_key_here
   COUNTRY_NAME=country_name_here
   ```
   Replace `newsapi_key_here` with actual NewsAPI key and `country_name_here` with preferred country code (e.g., `gb`, `in`, `au`).

---

## Usage

**Step 1:** Fetch the latest news
```bash
python news.py
```
This will generate a `news.json` file in the project directory.

**Step 2:** Display the desktop notification
```bash
python desktop.py
```
A notification will pop up on desktop showing the latest headline.

---

## Project Structure

```
Desktop_Notifier/
│
├── news.py          # Fetches news from NewsAPI and saves to news.json
├── desktop.py       # Reads news.json and sends a desktop notification
├── news.json        # Auto-generated file containing fetched news data
├── .env             # Environment variables (not committed to git)
└── README.md
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `requests` | Makes HTTP requests to NewsAPI |
| `plyer` | Sends cross-platform desktop notifications |
