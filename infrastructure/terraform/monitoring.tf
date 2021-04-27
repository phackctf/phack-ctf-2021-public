resource "scaleway_instance_ip" "monitoring_public_ip" {}

resource "scaleway_instance_server" "monitoring" {
  type              = "DEV1-S"
  image             = "ubuntu_focal"
  ip_id             = scaleway_instance_ip.monitoring_public_ip.id
  security_group_id = scaleway_instance_security_group.www.id
  tags              = ["admin", "monitoring"]
  name              = "phack-monitoring"
}