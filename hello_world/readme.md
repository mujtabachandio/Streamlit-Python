# Streamlit Hello World

This guide will help you set up and run a simple "Hello World" app using Streamlit. We will cover installation with both `uv` and `pip`, and how to run your app.

---

## 🚀 Installation

### Using `uv`
`uv` is a fast package manager that can be used as an alternative to `pip`.

```sh
# Install uv if not already installed
pip install uv

# Create a virtual environment
uv venv .venv

# Activate the virtual environment
# On Windows (cmd/powershell)
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Streamlit
uv pip install streamlit
```

### Using `pip`
If you prefer using `pip`, follow these steps:

```sh
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows (cmd/powershell)
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install Streamlit
pip install streamlit
```

---

## 🎉 Running Your First Streamlit App

Create a new Python file (e.g., `app.py`) and add the following code:

copy the code from file or write it

Now, run your app using:

```sh
streamlit run app.py
```

This will start a local development server, and the app will open in your web browser.

---

## 🎯 Additional Commands

- To stop the server, press `CTRL + C`
- To exit the virtual environment:
  - On Windows: `deactivate`
  - On macOS/Linux: `deactivate`

Happy coding! 🚀