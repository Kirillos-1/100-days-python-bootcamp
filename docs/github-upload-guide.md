# GitHub Upload Guide

This guide shows the command-line method for uploading this repo to GitHub.

## 1. Open the project folder

```bash
cd path/to/100-days-python-bootcamp
```

## 2. Initialize Git

```bash
git init
git branch -M main
```

## 3. Add files

```bash
git add .
git commit -m "Add days 1-9 of Python bootcamp"
```

## 4. Create a new GitHub repository

Create a repo named:

```text
100-days-python-bootcamp
```

Do not add a README, .gitignore, or license on GitHub if you already have them locally.

## 5. Connect local repo to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/100-days-python-bootcamp.git
```

## 6. Push

```bash
git push -u origin main
```

## Updating later

Whenever you add a new day:

```bash
git add .
git commit -m "Add day 10 project"
git push
```
