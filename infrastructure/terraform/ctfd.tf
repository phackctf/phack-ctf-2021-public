resource "scaleway_instance_ip" "ctfd_public_ip" {}

resource "scaleway_instance_server" "ctfd_server" {
  type              = "DEV1-M"
  image             = "ubuntu_focal"
  ip_id             = scaleway_instance_ip.ctfd_public_ip.id
  security_group_id = scaleway_instance_security_group.www.id
  tags              = ["ctfd"]
  name              = "phack-ctfd"
}

resource "scaleway_object_bucket" "ctfd_backup_bucket" {
  name = "phack-ctfd-backup"
  acl  = "private"
}