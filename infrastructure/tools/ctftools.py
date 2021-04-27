#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @Pdrooo
# Created Date: Dec. 2020
# Description : CTF cli to make management easier
# =============================================================================

import libs.CTFd as api
import libs.Actions as Actions
import libs.Terraform as Terraform
import libs.DiscordTool as DiscordTool
import libs.DiscordVPN as DiscordVPN
import libs.DiscordMessage as DiscordMessage

import click

@click.group()
# @click.option('--verbose', is_flag = True, help = 'Yield verbose logs')
def main():
    pass

@main.command()
@click.option('--sort', is_flag = True, help = 'Sort results')
def stats(sort):
    """Show some CTF stats."""

    stats = api.fetchStats(sort = sort)
    click.echo(stats.pprint())

@main.command()
def terraform():
    """Generate teams terreform script."""
    
    click.echo(Terraform.generate())

@main.command()
@click.argument('filename')
def actions(filename):
    """Generate github actions challenges script."""

    click.echo(Actions.generate(filename = filename))

@main.command()
# @click.option('--dry-run', is_flag = True, help = 'Show changes before apply')
def discord():
    """Configure discord team channels and roles."""

    DiscordTool.configure()

@main.command()
def vpn():
    """Send VPN configs to discord team channels."""

    DiscordVPN.configure()

@main.command()
def message():
    """Send private message to discord team channels."""

    DiscordMessage.configure()

if __name__ == '__main__':
    main()