provider "helm" {
  kubernetes {
    config_path = var.k8s_config_path
  }
}

resource "helm_release" "aws-ip-ranges" {

  name = "aws-ip-ranges"

  repository = "https://charts.j1shnu.ml/"
  chart      = "aws-ip-ranges-chart"
  namespace  = "default"

  set {
    name  = "fullnameOverride"
    value = "aws-ip-range-api-${var.environment}"
  }

  set {
    name  = "service.nodePort"
    value = var.node_port
  }
}

