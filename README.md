# Générateur de requêtes SQL - SIAP

Ce projet contient trois pages HTML qui permettent de générer automatiquement des requêtes SQL à partir de fichiers Excel contenant des données de passage.

## Objectif

- Générer des requêtes SQL selon trois procédures :
  - Fusion de communes
  - Scission de communes
  - Changement de code INSEE

## Structure

- `src/` : contient les fichiers HTML principaux.
- `data/` : contient les fichiers Excel d'exemple (non versionnés dans GitHub).
- `test/` : résultats attendus pour vérification.

## Utilisation

1. Ouvrir la page HTML correspondant à la procédure.
2. Importer le fichier Excel.
3. Copier les requêtes SQL générées.

## Dépendances

- [XLSX.js](https://github.com/SheetJS/sheetjs) pour la lecture des fichiers Excel côté navigateur.
