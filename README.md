## Helm Deploy

* Add repo using. `helm repo add aws-ip-range-chart https://charts.j1shnu.ml/`
* Use `helm search repo` to list the charts.
* Install using `helm install aws-ip-range-api aws-ip-range-chart/aws-ip-ranges-chart`
* `kubectl get all -A | grep aws` to check.
