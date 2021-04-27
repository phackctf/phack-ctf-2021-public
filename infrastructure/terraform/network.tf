resource "scaleway_instance_security_group" "www" {
  name                    = "phack_web_security_group"
  inbound_default_policy  = "drop"
  outbound_default_policy = "accept"

  inbound_rule {
    action = "accept"
    port   = "22"
  }

  inbound_rule {
    action = "accept"
    port   = "80"
  }

  inbound_rule {
    action = "accept"
    port   = "443"
  }

  inbound_rule {
    action = "accept"
    port   = "8086"
  }
}

resource "scaleway_instance_security_group" "challenges" {
  name                    = "phack_challenges_security_group"
  inbound_default_policy  = "drop"
  outbound_default_policy = "accept"

  inbound_rule {
    action = "accept"
    port   = "80"
  }

  inbound_rule {
    action = "accept"
    port   = "5601"
  }

  inbound_rule {
    action  = "accept"
    port    = "22"
  }
}

resource "scaleway_instance_security_group" "vpn" {
  name                    = "phack_teams_vpn_security_group"
  inbound_default_policy  = "drop"
  outbound_default_policy = "accept"

  inbound_rule {
    action   = "accept"
    port     = "1194"
    protocol = "UDP"
  }

  inbound_rule {
    action  = "accept"
    port    = "22"
  }
}