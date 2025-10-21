# Tristan Touazi — CV

Ce dépôt contient la source LaTeX de mon CV (une page) et la configuration VS Code pour compiler automatiquement le PDF puis le convertir en PNG.

## 🧰 Prérequis

Installer les outils suivants sur votre machine (WSL/Ubuntu conseillé) :
- LaTeX (XeLaTeX) : `sudo apt-get install -y texlive-xetex texlive-latex-recommended texlive-latex-extra`
- Poppler (pour la conversion PDF → PNG) : `sudo apt-get install -y poppler-utils`
- Python 3 et la bibliothèque `pdf2image` : `python3 -m pip install pdf2image`
- VS Code + extension « LaTeX Workshop » (recommandé)

## 🚀 Utilisation (VS Code)

Le dossier contient une configuration LaTeX Workshop prête à l’emploi (`.vscode/settings.json`).
- Ouvrir le dossier dans VS Code.
- Installer l’extension « LaTeX Workshop ».
- Modifier `cv.tex`, puis enregistrer (Ctrl+S).
- La recette « xelatex + png » se lance automatiquement : `CV_Tristan_Touazi_2025.pdf` et `CV_Tristan_Touazi_2025.png` sont régénérés.

## 🖥️ Utilisation (ligne de commande)

Sans VS Code, vous pouvez compiler et convertir manuellement :

```bash
xelatex -interaction=nonstopmode -file-line-error -jobname=CV_Tristan_Touazi_2025 cv.tex
python3 pdf_to_png.py
```

Le script `pdf_to_png.py` lit le PDF généré et crée le PNG correspondant à 300 DPI.

## ✏️ Personnalisation rapide

Les informations personnelles sont définies en haut de `cv.tex` :
- Nom/titre : `\setname{Tristan}{Touazi}`, `\setposition{...}`
- Adresse / mobile : `\setaddress{...}`, `\setmobile{...}`
- Email / LinkedIn / GitHub : `\setmail{...}`, `\setlinkedinaccount{...}`, `\setgithubaccount{...}`
- Couleur du thème : `\setthemecolor{MidnightBlue}`

Les sections principales sont ensuite : « Profil », « Compétences », « Expérience », « Formation ».

## 📁 Structure

- `cv.tex` : contenu du CV (LaTeX)
- `muratcan_cv.cls` : classe/style du CV
- `.vscode/settings.json` : recette de compilation auto (XeLaTeX + conversion PNG)
- `pdf_to_png.py` : conversion PDF → PNG
- `CV_Tristan_Touazi_2025.pdf` / `CV_Tristan_Touazi_2025.png` : fichiers générés

## ❗Dépannage

- XeLaTeX introuvable : installez `texlive-xetex` (voir Prérequis).
- Erreur `pdf2image` ou Poppler : installez `poppler-utils` et `python3 -m pip install pdf2image`.
- Pas de build auto : vérifiez l’extension « LaTeX Workshop », ou lancez les commandes en ligne de commande.

## 📤 Publication

Le dépôt est prêt pour Git ; configurez votre remote puis poussez :

```bash
git remote set-url origin https://github.com/TristanTouazi/TistanTouazi-cv.git
git push -u origin main
```

Vous pouvez aussi changer le nom du fichier final via `.vscode/settings.json` (clé `-jobname`).
