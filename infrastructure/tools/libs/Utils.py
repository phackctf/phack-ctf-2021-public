CTFD_ACCESS_TOKEN  = 'REMOVED'
CTFD_BASE_URL      = 'https://ctf.phack.fr/api/v1'

# DISCORD_ID    = REMOVED     # Production server
DISCORD_ID      = REMOVED     # POC Server
DISCORD_TOKEN   = 'REMOVED'

VPN_CONFIG_DIR  = '../ansible/static/openvpn'

CHALL_CATEGORIES = [
    'Web-Server',
    'Network',
    'Programmation',
    'Systeme',
    'Osint',
    'Forensic'
]

class BColors:
    OKAY = '\033[92m'
    WARN = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    EOL  = '\n'