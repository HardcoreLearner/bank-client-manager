# Procédure de Rollback

## Objectif
Revenir à une version stable du système après un déploiement problématique.

## Pré-requis
- Accès aux serveurs et outils de gestion des versions
- Version stable de sauvegarde

## Étapes

1. **Identification du problème**
   - Vérifier les erreurs via logs
   - Évaluer l'impact

2. **Préparation**
   - Informer les équipes
   - Sauvegarder l'état actuel (si possible)

3. **Rollback**
   - Utiliser Git pour revenir à une version stable :  
     ```bash
     git checkout <commit_id>
     ```
   - Déployer la version stable via script ou manuellement.

4. **Vérification**
   - Tester le système restauré
   - Analyser les logs

5. **Communication**
   - Informer les parties prenantes du succès
   - Mettre à jour la documentation si nécessaire

## Outils nécessaires
- Git
- Outils de sauvegarde
- Serveur (si déploiement distant)
