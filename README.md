# 🏗️ Civil Engineering Insight Studio

An AI-powered web application that analyzes images of civil engineering structures and generates detailed, professional descriptions using **Google Gemini Pro Vision** and **Streamlit**.

---

## 📁 Project Structure

```
PROJECT/
├── .env                  # Your Google API Key (keep private!)
├── app.py                # Main Streamlit application
└── requirements.txt      # Python dependencies
```

---

## ⚙️ Setup Instructions

### Step 1: Clone / Create the Project Folder
Create a folder named `PROJECT` and place all three files inside it.

### Step 2: Get Your Google API Key
1. Visit: https://ai.google.dev/gemini-api/docs/api-key
2. Sign in to your Google account
3. Click **"Get an API Key"**
4. Copy the generated API key

### Step 3: Configure the `.env` File
Create a `.env` file in your project folder:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

### Step 4: Install Dependencies
Open your terminal / Anaconda Prompt, navigate to the project folder, and run:
```bash
pip install -r requirements.txt
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 🚀 How to Use

1. **Upload an Image** – Upload a JPG, JPEG, or PNG image of a civil engineering structure
2. **Enter a Prompt** (optional) – Add a specific question like *"Identify the materials used"*
3. **Click "🚀 Describe Structure"** – The AI will analyze the image and generate a detailed report

---

## 💡 Use Cases

| Scenario | Description |
|---|---|
| **Material Identification** | Identify concrete, steel, brick, etc. from a construction image |
| **Project Documentation** | Document construction progress with AI-generated descriptions |
| **Structural Analysis** | Analyze bridges, beams, trusses, and other structural elements |

---

## 📦 Dependencies

| Library | Purpose |
|---|---|
| `streamlit` | Interactive web application framework |
| `google-generativeai` | Access to Google Gemini Pro Vision model |
| `python-dotenv` | Load environment variables from `.env` file |
| `Pillow` | Image reading and processing |

---

## 🏗️ Architecture

```
User → UI (Streamlit) → Input → Google Gemini Pro Vision (LLM) → Output → UI
```

---

## ⚠️ Notes
- Never share or commit your `.env` file to GitHub — add it to `.gitignore`
- The app uses `gemini-pro-vision` model which supports both text and image input
- Ensure you have a stable internet connection when running the app
