# -- Docker registry

resource "scaleway_registry_namespace_beta" "phack_registry" {
  name = "phack_challenges"
}