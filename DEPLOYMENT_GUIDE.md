# 🚀 GitHub Pages Deployment Guide

Your Captain IL website is ready to deploy! Follow these simple steps:

## Step 1: Create a GitHub Repository

1. Go to **https://github.com/new**
2. Repository name: `CAP_IL` (or `captain-il-mission-hope`)
3. Description: `Captain IL Mission HOPE - Fundraising Website`
4. Keep it **Public** (required for free GitHub Pages)
5. **DO NOT** initialize with README, .gitignore, or license
6. Click **"Create repository"**

## Step 2: Push Your Code to GitHub

After creating the repository, GitHub will show you commands. Use these instead:

```bash
git remote add origin https://github.com/YOUR_USERNAME/CAP_IL.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### Quick Copy-Paste (update YOUR_USERNAME):

```bash
git remote add origin https://github.com/YOUR_USERNAME/CAP_IL.git
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** (top menu)
3. Click **"Pages"** (left sidebar)
4. Under "Source", select: **Branch: main** and **/ (root)**
5. Click **"Save"**

## Step 4: Get Your Live URL! 🎉

After 1-2 minutes, your site will be live at:

**https://YOUR_USERNAME.github.io/CAP_IL/**

GitHub will show you the URL in the Pages settings.

---

## Already Have the Repo? Quick Commands:

If you already created the repo, just run these from the CAP_IL folder:

```bash
# Add your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/CAP_IL.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Then enable GitHub Pages in Settings → Pages.

---

## Troubleshooting

**Site not showing?**
- Wait 2-3 minutes after enabling Pages
- Make sure the repository is Public
- Check Settings → Pages for the live URL

**Need to update the site?**
- Make changes to your files
- Run: `git add .`
- Run: `git commit -m "Update website"`
- Run: `git push`
- Changes go live in 1-2 minutes!

---

## 🎯 Next Steps After Deployment

1. Share the URL: `https://YOUR_USERNAME.github.io/CAP_IL/`
2. Consider getting a custom domain (optional)
3. Add analytics (Google Analytics)
4. Set up donation payment gateway

---

**Need Help?** The commands are all ready in your terminal - just update YOUR_USERNAME and run them!


