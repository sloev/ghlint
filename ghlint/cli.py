import click


@click.command()
def main():
    click.echo("hello cli")
    return


if __name__ == '__main__':
    main()
