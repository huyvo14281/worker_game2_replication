import click

from config.application import Application


@click.group()
def __main():
    pass


@click.command('worker')
def worker():
    """Start the worker."""
    application = Application()
    application.start()


__main.add_command(worker)
if __name__ == '__main__':
    __main()
