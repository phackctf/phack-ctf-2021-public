# =============================================================================
# THIS FILE HAS BEEN GENERATED USING JINJA TEMPLATING
# DO NOT EDIT MANUALLY
# =============================================================================

# This file has been sanitized before public release (remove team names / members)

resource "scaleway_instance_ip" "team1_instance_ip" {}

resource "scaleway_instance_server" "team1_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team1_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team2_instance_ip" {}

resource "scaleway_instance_server" "team2_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team2_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team3_instance_ip" {}

resource "scaleway_instance_server" "team3_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team3_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team4_instance_ip" {}

resource "scaleway_instance_server" "team4_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team4_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team5_instance_ip" {}

resource "scaleway_instance_server" "team5_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team5_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team6_instance_ip" {}

resource "scaleway_instance_server" "team6_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team6_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team7_instance_ip" {}

resource "scaleway_instance_server" "team7_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team7_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team8_instance_ip" {}

resource "scaleway_instance_server" "team8_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team8_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team9_instance_ip" {}

resource "scaleway_instance_server" "team9_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team9_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team10_instance_ip" {}

resource "scaleway_instance_server" "team10_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team10_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team11_instance_ip" {}

resource "scaleway_instance_server" "team11_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team11_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team12_instance_ip" {}

resource "scaleway_instance_server" "team12_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team12_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team13_instance_ip" {}

resource "scaleway_instance_server" "team13_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team13_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team14_instance_ip" {}

resource "scaleway_instance_server" "team14_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team14_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team15_instance_ip" {}

resource "scaleway_instance_server" "team15_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team15_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team16_instance_ip" {}

resource "scaleway_instance_server" "team16_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team16_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team17_instance_ip" {}

resource "scaleway_instance_server" "team17_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team17_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team18_instance_ip" {}

resource "scaleway_instance_server" "team18_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team18_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team19_instance_ip" {}

resource "scaleway_instance_server" "team19_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team19_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team20_instance_ip" {}

resource "scaleway_instance_server" "team20_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team20_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team21_instance_ip" {}

resource "scaleway_instance_server" "team21_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team21_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team22_instance_ip" {}

resource "scaleway_instance_server" "team22_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team22_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team23_instance_ip" {}

resource "scaleway_instance_server" "team23_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team23_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team24_instance_ip" {}

resource "scaleway_instance_server" "team24_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team24_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team25_instance_ip" {}

resource "scaleway_instance_server" "team25_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team25_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team26_instance_ip" {}

resource "scaleway_instance_server" "team26_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team26_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team27_instance_ip" {}

resource "scaleway_instance_server" "team27_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team27_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team28_instance_ip" {}

resource "scaleway_instance_server" "team28_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team28_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team29_instance_ip" {}

resource "scaleway_instance_server" "team29_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team29_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team30_instance_ip" {}

resource "scaleway_instance_server" "team30_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team30_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team31_instance_ip" {}

resource "scaleway_instance_server" "team31_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team31_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team32_instance_ip" {}

resource "scaleway_instance_server" "team32_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team32_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team33_instance_ip" {}

resource "scaleway_instance_server" "team33_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team33_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team34_instance_ip" {}

resource "scaleway_instance_server" "team34_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team34_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team35_instance_ip" {}

resource "scaleway_instance_server" "team35_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team35_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team36_instance_ip" {}

resource "scaleway_instance_server" "team36_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team36_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team37_instance_ip" {}

resource "scaleway_instance_server" "team37_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team37_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team38_instance_ip" {}

resource "scaleway_instance_server" "team38_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team38_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team39_instance_ip" {}

resource "scaleway_instance_server" "team39_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team39_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team40_instance_ip" {}

resource "scaleway_instance_server" "team40_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team40_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team41_instance_ip" {}

resource "scaleway_instance_server" "team41_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team41_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team42_instance_ip" {}

resource "scaleway_instance_server" "team42_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team42_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team43_instance_ip" {}

resource "scaleway_instance_server" "team43_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team43_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team44_instance_ip" {}

resource "scaleway_instance_server" "team44_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team44_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team45_instance_ip" {}

resource "scaleway_instance_server" "team45_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team45_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team46_instance_ip" {}

resource "scaleway_instance_server" "team46_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team46_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team47_instance_ip" {}

resource "scaleway_instance_server" "team47_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team47_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team48_instance_ip" {}

resource "scaleway_instance_server" "team48_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team48_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team49_instance_ip" {}

resource "scaleway_instance_server" "team49_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team49_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

resource "scaleway_instance_ip" "team50_instance_ip" {}

resource "scaleway_instance_server" "team50_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team50_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}

# -- Admin test machine

resource "scaleway_instance_ip" "team51_instance_ip" {}

resource "scaleway_instance_server" "team51_instance_server" {
  type = "DEV1-S"
  image = "ubuntu_focal"
  ip_id = scaleway_instance_ip.team51_instance_ip.id
  security_group_id = scaleway_instance_security_group.vpn.id
  tags = [ "teams", "team=", "team_members=" ]
  name = ""
}