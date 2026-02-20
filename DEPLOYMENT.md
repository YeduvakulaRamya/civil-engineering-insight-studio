# 🚀 Streamlit Cloud Deployment Guide

## Quick Setup to Deploy on Streamlit Cloud

### Prerequisites
- GitHub account
- Google Gemini API key
- This project code

---

## Step 1️⃣: Push to GitHub

```bash
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Civil Engineering Insight Studio - Ready for deployment"

# Create repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/civil-engineering-studio.git
git branch -M main
git push -u origin main
```

---

## Step 2️⃣: Deploy on Streamlit Cloud

1. Go to **[streamlit.io/cloud](https://streamlit.io/cloud)**
2. Click **"New app"** button
3. **Select repository:**
   - GitHub account: [Select yours]
   - Repository: `civil-engineering-studio`
   - Branch: `main`
   - Main file path: `app.py`
4. Click **"Deploy"**
5. Wait 2-3 minutes for deployment ✅

---

## Step 3️⃣: Add Your API Key (IMPORTANT!)

Your app will error without the API key. Do this now:

1. After deployment completes, click **⚙️ Settings** (top right)
2. Click **"Secrets"** tab
3. Paste your API key in TOML format:
   ```
   GOOGLE_API_KEY = "AIzaSy..."
   ```
4. Click **"Save"**
5. Wait ~1 minute for changes to propagate ✅

---

## Step 4️⃣: Set Python Version (Optional)

For Python 3.13:

1. Go to **⚙️ Settings** → **Advanced settings**
2. Change **Python version** to `3.13.0`
3. Save

---

## ✅ Your App is Live!

Your app is now available at:
```
https://[YOUR-GITHUB-USERNAME]-civil-engineering-studio.streamlit.app
```

Share this URL with others!

---

## 🔧 Troubleshooting

### "Couldn't find GOOGLE_API_KEY"
- ✅ Verify you added it to Secrets (not .env)
- ✅ Wait 1-2 minutes for propagation
- ✅ Hard refresh browser (Ctrl+Shift+R)

### App is very slow
- ✅ Free tier has limited resources
- ✅ Upgrade Streamlit account for faster response

### "Import error"
- ✅ Verify requirements.txt is in repo root
- ✅ All dependencies have correct spelling

---

## 🔐 Security Notes

✅ **Good Practices:**
- API key in Streamlit Secrets only (never .env on GitHub)
- .gitignore prevents accidental commits
- Never share your live app URL with untrusted sources

❌ **Don't:**
- Commit `.env` or `secrets.toml`
- Share API keys
- Run on public networks without HTTPS

---

## 📊 Monitoring

Check your API usage:
- Google Cloud Console: [console.cloud.google.com](https://console.cloud.google.com)
- Verify quotas and costs
- Set up billing alerts

---

## 🆘 Need Help?

- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- [Google Gemini Docs](https://ai.google.dev/docs)
- [Streamlit Community](https://discuss.streamlit.io)

---

**Your app is ready to go! 🎉**
