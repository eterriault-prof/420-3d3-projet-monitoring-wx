# Projet 1 — Tableau de bord de monitoring système (version wxPython)

Application de surveillance des ressources système (CPU, RAM, disque) avec interface graphique wxPython.

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python app.py
```

## Travail à faire avant le cours

1. Forkez ce dépôt dans votre compte GitHub
2. Créez une branche `refactoring`
3. **Lisez attentivement le code** — vous aurez un quiz de compréhension en début de cours
4. Posez-vous les questions suivantes :
   - Que fait la méthode `rafraichir()` exactement ?
   - Que se passerait-il si on voulait ajouter une alerte quand le CPU dépasse 80% ?
   - Que se passerait-il si on voulait afficher les métriques dans une deuxième fenêtre ?
   - Y a-t-il des portions de code qui se ressemblent beaucoup ?
   - Quelle différence remarquez-vous entre `wx.CallLater()` et `after()` de tkinter ?
