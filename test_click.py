import click

@click.group()
def cli():
    pass

@cli.command(name='update-password')
@click.option('--new-password', prompt=True, hide_input=True, confirmation_prompt=True)
def update_password(new_password):
    click.echo(f"Password updated to: {new_password}")

if __name__ == '__main__':
    cli()
