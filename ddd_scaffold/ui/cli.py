import typer


class CLI():
    def __init__(self):
        self.app = typer.Typer()

        @self.app.command()
        def hello(message: str = typer.Argument('World')) -> None:
            typer.echo(typer.style(f'Hello, {message}', fg=typer.colors.GREEN))

    def run(self):
        self.app()
