Comment installer mlflow-kto ?

Exécuter les commandes suivantes :

```bash
git clone https://github.com/guillaume-thomas/kto-mlflow
cd kto-mlflow/k8s
oc apply -f minio.yml
oc apply -f mysql.yml
oc apply -f mlflow.yml
oc apply -f dailyclean.yml
oc label deployment dailyclean-api axa.com/dailyclean=false
oc label statefulset mysql axa.com/dailyclean=true
cd ../..
rm -rf kto-mlflow
```

Attention, pensez à bien éteindre vos workloads quand vous ne vous en servez plus avec Dailyclean

Attention, la sandbox éteint automatiquement les workloads
Nous utiliserons dailyclean pour allumer et éteindre notre environnement automatiquement depuis une github action

Désinstaller mlflow-kto : 
```bash
git clone https://github.com/guillaume-thomas/kto-mlflow
cd kto-mlflow/k8s
oc delete -f minio.yml
oc delete -f mysql.yml
oc delete -f mlflow.yml
oc delete -f dailyclean.yml
cd ../..
rm -rf kto-mlflow
```
