variable "k8s_config_path" {
  description = "Specify the path of kubernetes config file path"
  type        = string
  default     = "~/.kube/config"
}

variable "environment" {
  description = "Specify deployment environment. Example:- stag/dev/prod"
  type        = string
  default     = "demo"
}

variable "node_port" {
  description = "Specify the NodePort for the service"
  type        = number
  default     = 31001
}
