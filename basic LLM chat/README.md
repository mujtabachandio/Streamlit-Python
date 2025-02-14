# Streamlit LLM Chat App

This is a simple chat application built using **Streamlit** and **Hugging Face's API**. It allows users to interact with a language model (LLM) using the **BlenderBot 400M** model hosted on Hugging Face.

---

## 🚀 Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required libraries:
```sh
pip install streamlit requests
```

### 2️⃣ Set Up Hugging Face API Key
Replace `'your-api-key'` in the `API_URL` section of the code with your actual Hugging Face API key.

### 3️⃣ Run the Application
```sh
streamlit run app.py
```

This will start the Streamlit server, and the app will open in your browser.

---

## 🎯 Features
- Simple chat interface
- Stores chat history within the session
- Uses Hugging Face's **BlenderBot 400M** for responses

---

## 🔧 Customization
You can modify the model being used by changing the API endpoint:
```python
API_URL = "https://api-inference.huggingface.co/models/{your-model-name}"
```
Replace `{your-model-name}` with another model from Hugging Face.

---

## 🛑 Stopping the App
To stop the Streamlit server, use:
```sh
CTRL + C
```

---

Enjoy chatting with AI! 🚀

