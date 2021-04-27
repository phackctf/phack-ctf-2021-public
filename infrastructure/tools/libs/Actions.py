# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo
# Created Date: Dec. 2020
# Description : Generate Github Actions YAML challenges build jobs
# =============================================================================

from jinja2 import Template
from libs.CTFd import Chall
from libs.Utils import CHALL_CATEGORIES

import toml

# Generate CI build&push file
# for Github Actions
def generate(filename: str) -> str:
    challs = []
    
    parsed_toml = toml.loads(open(filename).read())

    for category in CHALL_CATEGORIES:
        for chall in parsed_toml['challs'][category]:
            challs.append( Chall(chall, category) )

    template = Template(open('templates/build.yml.j2').read())

    return template.render(challs = challs)