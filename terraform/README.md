## Terraform Deploy

* Create \a tfvars file using `template.tfvars`.
* Can set below variables.\
`k8s_config_path` for kubernetes config file path.\
`environment` for deployment environment. Example:- stag/dev/prod.\
`node_port` for NodePort to expose the service.
* Run using `terraform apply -var-file=<file.tfvars>`.
