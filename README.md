# 📰 News Analytics Pro

## Overview

**News Analytics Pro** is a web-based application that extracts, summarizes, and analyzes any news article from a URL in seconds. Paste a link to any online article and instantly receive a concise AI-generated summary, key metadata (title, authors, publication date), and a sentiment analysis result — all within a clean, responsive interface. Built for readers, researchers, and developers who need quick, structured insights from news content without navigating cluttered pages.

## Key Features

- **Automatic Article Extraction** — Downloads and parses article content from any public URL using `newspaper3k`
- **AI-Powered Summarization** — Generates a concise summary using NLP keyword extraction built into `newspaper3k`
- **Sentiment Analysis** — Classifies article tone as positive, negative, or neutral via `TextBlob` polarity scoring
- **Metadata Display** — Extracts and surfaces article title, authors, and publication date
- **Full Text View** — Expandable panel to read the complete article text in-app
- **Responsive UI** — Animated, mobile-friendly layout built with Streamlit and custom CSS

## Tech Stack

| Category     | Technology                          |
|--------------|-------------------------------------|
| Language     | Python 3.11                         |
| Framework    | Streamlit                           |
| NLP / ML     | newspaper3k, TextBlob, NLTK         |
| HTML Parsing | lxml, lxml-html-clean               |
| Dev Environment | GitHub Codespaces / VS Code Dev Containers |

## Installation

### Prerequisites

- Python 3.9+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/vanix056/News-Summarizer.git
cd News-Summarizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download required NLTK data
bash setup.sh
```

## Usage

```bash
streamlit run app.py
```

The application will start on `http://localhost:8501` by default.

1. Open the app in your browser
2. Paste a news article URL into the input field
3. Click **Analyze Article**
4. View the summary, metadata, and sentiment result in the dashboard

> **Streamlit Cloud:** The app downloads NLTK data automatically on first run when deployed to Streamlit Cloud.

## Project Structure

```
News-Summarizer/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── setup.sh                # NLTK data setup script
└── .devcontainer/
    └── devcontainer.json   # GitHub Codespaces / Dev Container configuration
```

## Configuration

No environment variables are required for local use. The app runs out of the box after installing dependencies.

| Parameter | Location | Description |
|-----------|----------|-------------|
| NLTK data path | `app.py` (line 7–9) | Set to `/home/appuser/nltk_data` for Streamlit Cloud; modify for custom environments |
| Streamlit port | CLI | Defaults to `8501`; override with `--server.port` |
| CORS / XSRF | `.devcontainer/devcontainer.json` | Disabled for local Codespaces preview |

## UI Features

- **Animated header** with fade-in transitions
- **Two-column layout** — article content on the left, metadata panel on the right
- **Metric cards** with hover lift effects for title, authors, date, and sentiment
- **Expandable full-text panel** to reduce visual clutter
- **Social links footer** for author contact (LinkedIn, GitHub)
- **Responsive design** — social button labels collapse on mobile viewports

## Deployment

### Streamlit Community Cloud (Recommended)

1. Push the repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect the repository
3. Set the main file path to `app.py`
4. Deploy — NLTK data is downloaded automatically on startup

### GitHub Codespaces

Open the repository in Codespaces. The dev container will:
- Install all Python dependencies from `requirements.txt`
- Install `streamlit`
- Automatically launch the app on port `8501` with a preview window

```bash
# Manual launch inside Codespaces
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: description"`
4. Push to your fork and open a pull request

Please keep pull requests focused and include a clear description of the change.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Abdullah Waqar**

- GitHub: [@vanix056](https://github.com/vanix056)
- LinkedIn: [abdullahwaqar](https://www.linkedin.com/in/abdullahwaqar/)
