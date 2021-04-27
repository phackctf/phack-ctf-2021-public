.PHONY: install update

all:
	@echo "Usage: make [install | update]"

install:
	fly -t ctfd login -c https://concourse.phack.fr -u admin -p REMOVED
	update

update:
	fly -t ctfd set-pipeline --non-interactive --pipeline terraform-pipeline --config pipeline/terraform-pipeline.yml
	fly -t ctfd set-pipeline --non-interactive --pipeline deploy-challenges --config pipeline/deploy-challenges.yml
	fly -t ctfd set-pipeline --non-interactive --pipeline configure-all --config pipeline/configure-all.yml