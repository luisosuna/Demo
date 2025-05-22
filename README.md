Stack Overflow QA Chatbot — Fine-Tuned GPT-3.5 Turbo

A domain-specific AI chatbot powered by a fine-tuned `gpt-3.5-turbo` model, trained on high-quality Q&A data scraped from Stack Overflow. Built with Python, Scrapy, OpenAI’s fine-tuning tools, and a fully automated data pipeline for transforming real-world developer knowledge into an intelligent assistant for QA and dev workflows.

---

## 🔧 Features

- 🧠 Fine-tuned GPT-3.5 on real Stack Overflow Q&A content
- 🕸 Scraped using Scrapy + BeautifulSoup
- 🧹 Data cleaned and converted to OpenAI’s fine-tuning format
- 💬 Lightweight command-line chatbot powered by OpenAI API
- ⚙️ Easily extensible to internal docs or other domains

---

## 📊 Project Workflow

```mermaid
graph TD;
    A[Scrape Stack Overflow (Scrapy)] --> B[Save Raw Q&A in JSON]
    B --> C[Clean & Transform (BeautifulSoup, html.unescape)]
    C --> D[Prepare JSONL for OpenAI ("messages": [...])]
    D --> E[Fine-Tune GPT-3.5 Turbo Model]
    E --> F[Chatbot CLI or API Execution]
