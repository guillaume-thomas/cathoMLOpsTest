Utilisation de Kubeflow pour train des model avec Kubernetes

L'exemple de Guigui utilise keras et tensorflow

https://www.kubeflow.org/docs/components/training/tftraining/

Installer kubeflow est passablement compliqué : 

https://www.kubeflow.org/docs/started/installing-kubeflow/

Mais Kubeflow pipeline est peut être suffisant, si j'utilise mlflow à côté : 

https://www.kubeflow.org/docs/components/pipelines/v1/overview/quickstart/
https://github.com/kubeflow/examples/blob/master/pipelines/simple-notebook-pipeline/Simple%20Notebook%20Pipeline.ipynb
https://developer.ibm.com/tutorials/awb-compose-run-ml-pipelines-using-kubeflow-pipelines/
https://developer.ibm.com/tutorials/awb-deploy-standalone-kubeflow-pipelines-on-a-kind-cluster/
https://github.com/kubeflow/pipelines

Installer kubeflow openshift pipeline
https://developer.ibm.com/tutorials/run-kubeflow-pipelines-with-certified-red-hat-openshift-pipelines/

ou plutôt

https://github.com/kubeflow/kfp-tekton/blob/master/guides/kfp_tekton_install.md#standalone-kubeflow-pipelines-with-openshift-pipelines-backend-deployment

mais on n'a pas les droits grrrr
