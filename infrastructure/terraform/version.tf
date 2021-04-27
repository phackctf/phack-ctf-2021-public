terraform {
  backend "s3" {
    bucket                      = ""
    key                         = "env:/prod/state.tfstate"
    region                      = "fr-par"
    endpoint                    = "https://s3.fr-par.scw.cloud"
    access_key                  = ""
    secret_key                  = ""
    skip_credentials_validation = true
    skip_region_validation      = true
  }

  required_providers {
    scaleway = {
      source = "scaleway/scaleway"
    }
  }
  required_version = ">= 0.13"
}

provider "scaleway" {
  zone            = "fr-par-1"
  region          = "fr-par"
  access_key      = ""
  secret_key      = ""
  organization_id = ""
}
