Deux étapes: une première non structurée
La deuxième en utilisant les capacités de notre archi MLFlow

Première étape faite, voir les détails dans les README de chaque partie

Déterminer le livrable pour l'étape précédente (git, tdd, clean code, Création d'un compte developers.redhat.com, 
création d'une sandbox, création d'un compte github)

Livrables à la fin de cette étape : 
M'envoyer par mail cats_dogs_others-annotations.json
M'envoyer par mail train/dist/model/model_plot.png, predictions.json, statistics.json

Maintenant, mise en place de MLFlow.

Une fois que l'on a tout en place, faire la partie avec sauvegarde du dataset et split dans minio:
- Upload de l'integralité du dataset dans minio (à la main, ce sera plus rigolo)
- Mise en place des variables d'environnements pour se connecter depuis codespace (non en fait)

```bash
export AWS_ACCESS_URL=http://tmp-route-aws-gthomas59800-dev.apps.sandbox-m3.1530.p1.openshiftapps.com
export AWS_ACCESS_KEY_ID=minio
export AWS_SECRET_ACCESS_KEY=minio123
```

- Mise en place du script de telechargement du dataset dans la partie extraction
- Sauvegarde du split dans minio dans la partie split
- !!!! Bien expliquer que normalement, il ne faudrait pas refaire un split random à chaque fois !!!!
- Ajouter le chemin dans l'expérience mlflow

Mise en place de l'api

Build et deploy automatique dans github action
Test d'intégration du service
