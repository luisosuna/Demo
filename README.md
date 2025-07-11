# Stack Overflow QA Visual Chatbot — Fine-Tuned GPT-3.5 Turbo

A domain-specific AI chatbot powered by a fine-tuned `gpt-3.5-turbo` model, trained on high-quality Q&A data scraped from Stack Overflow. Built with Python, Scrapy, OpenAI's fine-tuning tools, and a modern **visual web interface** for an enhanced user experience.

---

## 🔧 Features

- 🧠 Fine-tuned GPT-3.5 on real Stack Overflow Q&A content
- 🕸 Scraped using Scrapy + BeautifulSoup
- 🧹 Data cleaned and converted to OpenAI's fine-tuning format
- 🌐 **Modern visual web interface** with chat bubbles and real-time messaging
- 💬 ~~Lightweight command-line chatbot~~ **Enhanced visual chatbot** powered by OpenAI API
- ⚙️ Easily extensible to internal docs or other domains
- 📱 Responsive design that works on desktop and mobile
- 🎨 Professional UI with typing indicators and message timestamps

---

## 🚀 Quick Start

### Option 1: Use the startup script (Recommended)
```bash
./start_chatbot.sh
```

### Option 2: Manual setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set up your API key
cp Chatbot/.env.example Chatbot/.env
# Edit .env and add your OpenAI API key

# Start the visual chatbot
cd Chatbot && python app.py
```

Then open http://localhost:5000 in your browser to access the visual chatbot interface.

---

## 🖥️ Visual Interface

The chatbot now features a modern web interface with:

- **Clean, professional design** with a gradient background
- **Chat bubbles** for user and bot messages
- **Real-time messaging** with typing indicators
- **Responsive layout** that works on all devices
- **Message timestamps** for conversation tracking
- **Error handling** with user-friendly messages

![Visual Chatbot Interface](https://github.com/user-attachments/assets/4262f454-5954-4ec3-b3fb-861fe4b3557a)

![Chat Conversation](https://github.com/user-attachments/assets/60d908c8-b11e-4b9d-a42d-3a23b19b85d9)

---

## 📊 Project Workflow

```mermaid
graph TD;
    A[Scrape Stack Overflow (Scrapy)] --> B[Save Raw Q&A in JSON]
    B --> C[Clean & Transform (BeautifulSoup, html.unescape)]
    C --> D[Prepare JSONL for OpenAI ("messages": [...])]
    D --> E[Fine-Tune GPT-3.5 Turbo Model]
    E --> F[Visual Web Chatbot Interface]
```

## 📁 Project Structure

```
Demo/
├── Chatbot/
│   ├── app.py                 # Flask web server for visual chatbot
│   ├── chatbotmodel.py        # Original CLI chatbot (still available)
│   ├── training.py            # Model fine-tuning script
│   ├── fileconversion.py      # Data preprocessing
│   ├── templates/
│   │   └── index.html         # Visual chatbot HTML interface
│   ├── static/
│   │   ├── css/style.css      # Modern UI styling
│   │   └── js/app.js          # Interactive JavaScript
│   ├── .env.example           # Environment variables template
│   └── *.jsonl               # Training data files
├── requirements.txt           # Python dependencies
└── start_chatbot.sh          # Easy startup script
```

## 🛠️ Technical Implementation

### Backend (Flask)
- **Flask web server** serving the visual interface
- **RESTful API** endpoints for chat messages
- **OpenAI integration** preserving original fine-tuned model
- **Error handling** and graceful API key management

### Frontend (HTML/CSS/JS)
- **Responsive design** with modern CSS styling
- **Real-time messaging** with JavaScript fetch API
- **Chat bubbles** with proper message threading
- **Typing indicators** and timestamps
- **Mobile-friendly** responsive layout

## 🔄 Migration from CLI to Visual

The transformation preserves all the original functionality while adding a modern web interface:

- ✅ **Original CLI chatbot** still available (`chatbotmodel.py`)
- ✅ **Same fine-tuned model** and API integration
- ✅ **Enhanced user experience** with visual interface
- ✅ **Backward compatibility** maintained
- ✅ **Minimal code changes** for maximum impact

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with the visual interface
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).