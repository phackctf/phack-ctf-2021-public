resource "scaleway_instance_ip" "challenges_standalone_public_ip" {}

resource "scaleway_instance_server" "challenges_standalone_server" {
  type              = "DEV1-M"
  image             = "ubuntu_focal"
  ip_id             = scaleway_instance_ip.challenges_standalone_public_ip.id
  security_group_id = scaleway_instance_security_group.challenges.id
  tags              = ["challenges"]
  name              = "phack-challenges-standalone"
}