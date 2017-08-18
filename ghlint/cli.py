import click
from . import config


@click.command()
def main():
    settings = config.settings()
    click.echo("hello cli {}".format(settings))
    return


if __name__ == '__main__':
    main()
