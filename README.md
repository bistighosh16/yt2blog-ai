# 🎬 YT2Blog AI 💜

> Transform any YouTube video (or any text!) into a beautiful blog post, Twitter thread, and LinkedIn post — in seconds! ✨

<div align="center">

### 🚀 [**Try the Live Demo →**](https://yt2blog-ai.streamlit.app/) 💜

[![Live Demo](https://img.shields.io/badge/🚀_LIVE_DEMO-Try_It_Now-9B59B6?style=for-the-badge&labelColor=E056FD)](https://yt2blog-ai.streamlit.app/)
[![Made with Streamlit](https://img.shields.io/badge/Made_with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Powered by Groq](https://img.shields.io/badge/Powered_by-Groq-F55036?style=for-the-badge)](https://groq.com)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-9B59B6?style=for-the-badge)](LICENSE)

</div>
---

## ✨ What is YT2Blog AI?

**YT2Blog AI** is your content multiplier 🚀 — paste any YouTube URL and instantly get:

- 📝 A **beautifully formatted blog post** (Markdown)
- 🎯 **SEO metadata** (title, description, tags)
- 🐦 A **viral Twitter thread**
- 💼 A **professional LinkedIn post**

Built for content creators, marketers, students, and anyone who wants to repurpose video content into multiple formats — **for FREE**! 💜

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🎬 **YouTube Integration** | Works with any YouTube URL format (regular, shorts, embed) |
| 📝 **Paste Transcript** | Works on cloud! Paste any text or transcript directly |
| 🧠 **AI-Powered** | Uses Llama 3.3 70B via Groq for blazing-fast generation |
| 🎨 **Multiple Tones** | Professional, Casual, Technical, or Storytelling |
| 📏 **Custom Length** | Short (~500), Medium (~1000), or Detailed (~1500+ words) |
| 🎯 **SEO Optimization** | Auto-generates SEO title, meta description & tags |
| 🐦 **Twitter Threads** | Convert blog into viral Twitter/X thread |
| 💼 **LinkedIn Posts** | Professional LinkedIn-ready content |
| 🎨 **Theme Switcher** | 3 stunning themes: Cosmic Purple, Aurora, Midnight |
| 🎉 **Confetti Celebration** | Because you deserve to celebrate! 💜 |
| ⬇️ **Download All** | Export as Markdown or TXT |

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit + Custom CSS (Glassmorphism)
- **LLM:** Groq API (Llama 3.3 70B Versatile)
- **Transcripts:** youtube-transcript-api
- **Framework:** LangChain Core
- **Language:** Python 3.11

---

## 🏃 Quick Start

### Prerequisites
- Python 3.11+
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/bistighosh16/yt2blog-ai.git
cd yt2blog-ai

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq API key
echo GROQ_API_KEY=your_key_here > .env

# 5. Run the app
streamlit run app.py
