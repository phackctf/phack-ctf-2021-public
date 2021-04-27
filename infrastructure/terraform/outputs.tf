### The Ansible inventory file

resource "local_file" "AnsibleInventory" {
  content = templatefile("template/inventory.tmpl",
    {
      monitoring-ip                   = scaleway_instance_ip.monitoring_public_ip.address
      monitoring-private-ip           = scaleway_instance_server.monitoring.private_ip
      challenges-standalone-public-ip = scaleway_instance_server.challenges_standalone_server.public_ip

      # Because loops are for losers

      teams-1-public-ip         = scaleway_instance_server.team1_instance_server.public_ip
      teams-1-name              = scaleway_instance_server.team1_instance_server.tags[1]
      teams-1-members           = scaleway_instance_server.team1_instance_server.tags[2]

      teams-2-public-ip         = scaleway_instance_server.team2_instance_server.public_ip
      teams-2-name              = scaleway_instance_server.team2_instance_server.tags[1]
      teams-2-members           = scaleway_instance_server.team2_instance_server.tags[2]

      teams-3-public-ip         = scaleway_instance_server.team3_instance_server.public_ip
      teams-3-name              = scaleway_instance_server.team3_instance_server.tags[1]
      teams-3-members           = scaleway_instance_server.team3_instance_server.tags[2]

      teams-4-public-ip         = scaleway_instance_server.team4_instance_server.public_ip
      teams-4-name              = scaleway_instance_server.team4_instance_server.tags[1]
      teams-4-members           = scaleway_instance_server.team4_instance_server.tags[2]

      teams-5-public-ip         = scaleway_instance_server.team5_instance_server.public_ip
      teams-5-name              = scaleway_instance_server.team5_instance_server.tags[1]
      teams-5-members           = scaleway_instance_server.team5_instance_server.tags[2]

      teams-6-public-ip         = scaleway_instance_server.team6_instance_server.public_ip
      teams-6-name              = scaleway_instance_server.team6_instance_server.tags[1]
      teams-6-members           = scaleway_instance_server.team6_instance_server.tags[2]

      teams-7-public-ip         = scaleway_instance_server.team7_instance_server.public_ip
      teams-7-name              = scaleway_instance_server.team7_instance_server.tags[1]
      teams-7-members           = scaleway_instance_server.team7_instance_server.tags[2]

      teams-8-public-ip         = scaleway_instance_server.team8_instance_server.public_ip
      teams-8-name              = scaleway_instance_server.team8_instance_server.tags[1]
      teams-8-members           = scaleway_instance_server.team8_instance_server.tags[2]

      teams-9-public-ip         = scaleway_instance_server.team9_instance_server.public_ip
      teams-9-name              = scaleway_instance_server.team9_instance_server.tags[1]
      teams-9-members           = scaleway_instance_server.team9_instance_server.tags[2]

      teams-10-public-ip         = scaleway_instance_server.team10_instance_server.public_ip
      teams-10-name              = scaleway_instance_server.team10_instance_server.tags[1]
      teams-10-members           = scaleway_instance_server.team10_instance_server.tags[2]

      teams-11-public-ip         = scaleway_instance_server.team11_instance_server.public_ip
      teams-11-name              = scaleway_instance_server.team11_instance_server.tags[1]
      teams-11-members           = scaleway_instance_server.team11_instance_server.tags[2]

      teams-12-public-ip         = scaleway_instance_server.team12_instance_server.public_ip
      teams-12-name              = scaleway_instance_server.team12_instance_server.tags[1]
      teams-12-members           = scaleway_instance_server.team12_instance_server.tags[2]

      teams-13-public-ip         = scaleway_instance_server.team13_instance_server.public_ip
      teams-13-name              = scaleway_instance_server.team13_instance_server.tags[1]
      teams-13-members           = scaleway_instance_server.team13_instance_server.tags[2]

      teams-14-public-ip         = scaleway_instance_server.team14_instance_server.public_ip
      teams-14-name              = scaleway_instance_server.team14_instance_server.tags[1]
      teams-14-members           = scaleway_instance_server.team14_instance_server.tags[2]

      teams-15-public-ip         = scaleway_instance_server.team15_instance_server.public_ip
      teams-15-name              = scaleway_instance_server.team15_instance_server.tags[1]
      teams-15-members           = scaleway_instance_server.team15_instance_server.tags[2]

      teams-16-public-ip         = scaleway_instance_server.team16_instance_server.public_ip
      teams-16-name              = scaleway_instance_server.team16_instance_server.tags[1]
      teams-16-members           = scaleway_instance_server.team16_instance_server.tags[2]

      teams-17-public-ip         = scaleway_instance_server.team17_instance_server.public_ip
      teams-17-name              = scaleway_instance_server.team17_instance_server.tags[1]
      teams-17-members           = scaleway_instance_server.team17_instance_server.tags[2]

      teams-18-public-ip         = scaleway_instance_server.team18_instance_server.public_ip
      teams-18-name              = scaleway_instance_server.team18_instance_server.tags[1]
      teams-18-members           = scaleway_instance_server.team18_instance_server.tags[2]

      teams-19-public-ip         = scaleway_instance_server.team19_instance_server.public_ip
      teams-19-name              = scaleway_instance_server.team19_instance_server.tags[1]
      teams-19-members           = scaleway_instance_server.team19_instance_server.tags[2]

      teams-20-public-ip         = scaleway_instance_server.team20_instance_server.public_ip
      teams-20-name              = scaleway_instance_server.team20_instance_server.tags[1]
      teams-20-members           = scaleway_instance_server.team20_instance_server.tags[2]

      teams-21-public-ip         = scaleway_instance_server.team21_instance_server.public_ip
      teams-21-name              = scaleway_instance_server.team21_instance_server.tags[1]
      teams-21-members           = scaleway_instance_server.team21_instance_server.tags[2]

      teams-22-public-ip         = scaleway_instance_server.team22_instance_server.public_ip
      teams-22-name              = scaleway_instance_server.team22_instance_server.tags[1]
      teams-22-members           = scaleway_instance_server.team22_instance_server.tags[2]

      teams-23-public-ip         = scaleway_instance_server.team23_instance_server.public_ip
      teams-23-name              = scaleway_instance_server.team23_instance_server.tags[1]
      teams-23-members           = scaleway_instance_server.team23_instance_server.tags[2]

      teams-24-public-ip         = scaleway_instance_server.team24_instance_server.public_ip
      teams-24-name              = scaleway_instance_server.team24_instance_server.tags[1]
      teams-24-members           = scaleway_instance_server.team24_instance_server.tags[2]

      teams-25-public-ip         = scaleway_instance_server.team25_instance_server.public_ip
      teams-25-name              = scaleway_instance_server.team25_instance_server.tags[1]
      teams-25-members           = scaleway_instance_server.team25_instance_server.tags[2]

      teams-26-public-ip         = scaleway_instance_server.team26_instance_server.public_ip
      teams-26-name              = scaleway_instance_server.team26_instance_server.tags[1]
      teams-26-members           = scaleway_instance_server.team26_instance_server.tags[2]

      teams-27-public-ip         = scaleway_instance_server.team27_instance_server.public_ip
      teams-27-name              = scaleway_instance_server.team27_instance_server.tags[1]
      teams-27-members           = scaleway_instance_server.team27_instance_server.tags[2]

      teams-28-public-ip         = scaleway_instance_server.team28_instance_server.public_ip
      teams-28-name              = scaleway_instance_server.team28_instance_server.tags[1]
      teams-28-members           = scaleway_instance_server.team28_instance_server.tags[2]

      teams-29-public-ip         = scaleway_instance_server.team29_instance_server.public_ip
      teams-29-name              = scaleway_instance_server.team29_instance_server.tags[1]
      teams-29-members           = scaleway_instance_server.team29_instance_server.tags[2]

      teams-30-public-ip         = scaleway_instance_server.team30_instance_server.public_ip
      teams-30-name              = scaleway_instance_server.team30_instance_server.tags[1]
      teams-30-members           = scaleway_instance_server.team30_instance_server.tags[2]

      teams-31-public-ip         = scaleway_instance_server.team31_instance_server.public_ip
      teams-31-name              = scaleway_instance_server.team31_instance_server.tags[1]
      teams-31-members           = scaleway_instance_server.team31_instance_server.tags[2]

      teams-32-public-ip         = scaleway_instance_server.team32_instance_server.public_ip
      teams-32-name              = scaleway_instance_server.team32_instance_server.tags[1]
      teams-32-members           = scaleway_instance_server.team32_instance_server.tags[2]

      teams-33-public-ip         = scaleway_instance_server.team33_instance_server.public_ip
      teams-33-name              = scaleway_instance_server.team33_instance_server.tags[1]
      teams-33-members           = scaleway_instance_server.team33_instance_server.tags[2]

      teams-34-public-ip         = scaleway_instance_server.team34_instance_server.public_ip
      teams-34-name              = scaleway_instance_server.team34_instance_server.tags[1]
      teams-34-members           = scaleway_instance_server.team34_instance_server.tags[2]

      teams-35-public-ip         = scaleway_instance_server.team35_instance_server.public_ip
      teams-35-name              = scaleway_instance_server.team35_instance_server.tags[1]
      teams-35-members           = scaleway_instance_server.team35_instance_server.tags[2]

      teams-36-public-ip         = scaleway_instance_server.team36_instance_server.public_ip
      teams-36-name              = scaleway_instance_server.team36_instance_server.tags[1]
      teams-36-members           = scaleway_instance_server.team36_instance_server.tags[2]

      teams-37-public-ip         = scaleway_instance_server.team37_instance_server.public_ip
      teams-37-name              = scaleway_instance_server.team37_instance_server.tags[1]
      teams-37-members           = scaleway_instance_server.team37_instance_server.tags[2]

      teams-38-public-ip         = scaleway_instance_server.team38_instance_server.public_ip
      teams-38-name              = scaleway_instance_server.team38_instance_server.tags[1]
      teams-38-members           = scaleway_instance_server.team38_instance_server.tags[2]

      teams-39-public-ip         = scaleway_instance_server.team39_instance_server.public_ip
      teams-39-name              = scaleway_instance_server.team39_instance_server.tags[1]
      teams-39-members           = scaleway_instance_server.team39_instance_server.tags[2]

      teams-40-public-ip         = scaleway_instance_server.team40_instance_server.public_ip
      teams-40-name              = scaleway_instance_server.team40_instance_server.tags[1]
      teams-40-members           = scaleway_instance_server.team40_instance_server.tags[2]

      teams-41-public-ip         = scaleway_instance_server.team41_instance_server.public_ip
      teams-41-name              = scaleway_instance_server.team41_instance_server.tags[1]
      teams-41-members           = scaleway_instance_server.team41_instance_server.tags[2]

      teams-42-public-ip         = scaleway_instance_server.team42_instance_server.public_ip
      teams-42-name              = scaleway_instance_server.team42_instance_server.tags[1]
      teams-42-members           = scaleway_instance_server.team42_instance_server.tags[2]

      teams-43-public-ip         = scaleway_instance_server.team43_instance_server.public_ip
      teams-43-name              = scaleway_instance_server.team43_instance_server.tags[1]
      teams-43-members           = scaleway_instance_server.team43_instance_server.tags[2]

      teams-44-public-ip         = scaleway_instance_server.team44_instance_server.public_ip
      teams-44-name              = scaleway_instance_server.team44_instance_server.tags[1]
      teams-44-members           = scaleway_instance_server.team44_instance_server.tags[2]

      teams-45-public-ip         = scaleway_instance_server.team45_instance_server.public_ip
      teams-45-name              = scaleway_instance_server.team45_instance_server.tags[1]
      teams-45-members           = scaleway_instance_server.team45_instance_server.tags[2]

      teams-46-public-ip         = scaleway_instance_server.team46_instance_server.public_ip
      teams-46-name              = scaleway_instance_server.team46_instance_server.tags[1]
      teams-46-members           = scaleway_instance_server.team46_instance_server.tags[2]

      teams-47-public-ip         = scaleway_instance_server.team47_instance_server.public_ip
      teams-47-name              = scaleway_instance_server.team47_instance_server.tags[1]
      teams-47-members           = scaleway_instance_server.team47_instance_server.tags[2]

      teams-48-public-ip         = scaleway_instance_server.team48_instance_server.public_ip
      teams-48-name              = scaleway_instance_server.team48_instance_server.tags[1]
      teams-48-members           = scaleway_instance_server.team48_instance_server.tags[2]

      teams-49-public-ip         = scaleway_instance_server.team49_instance_server.public_ip
      teams-49-name              = scaleway_instance_server.team49_instance_server.tags[1]
      teams-49-members           = scaleway_instance_server.team49_instance_server.tags[2]

      teams-50-public-ip         = scaleway_instance_server.team50_instance_server.public_ip
      teams-50-name              = scaleway_instance_server.team50_instance_server.tags[1]
      teams-50-members           = scaleway_instance_server.team50_instance_server.tags[2]

      teams-51-public-ip         = scaleway_instance_server.team51_instance_server.public_ip
      teams-51-name              = scaleway_instance_server.team51_instance_server.tags[1]
      teams-51-members           = scaleway_instance_server.team51_instance_server.tags[2]

    }
  )

  filename = "../ansible/inventories/scaleway"
}