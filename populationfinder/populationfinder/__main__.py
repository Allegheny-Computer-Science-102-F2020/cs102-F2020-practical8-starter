"""Define the command-line interface for the populationfinder program."""

# TODO: import the Path object
from pathlib import Path

# TODO: import the transform module from populationfinder package


# TODO: import typer


def main(
    data_file: Path = typer.Option(...),
    year: str = typer.Option(...),
):
    """Summarize the data values stored in a file."""
    # display details about the file provided on the command line
    data_text = ""
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        typer.echo("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        data_text = data_file.read_text()
        data_line_count = len(data_text.splitlines())
        # display the number of lines in the file and the requested year
        typer.echo("")
        typer.echo(f"The data file contains {data_line_count} data values in it!")
        typer.echo(f"Now we can search for the population at year {year}")
        # TODO: transform the data from a list of textual values to a dictionary of values
        # TODO: lookup the population (i.e., the value) given the specific key (i.e., the year)
        # TODO: display the population at the requested year
        # TODO: although not required for full points on this assignment, think about
        # what might happen if the user requests population data for a year for which
        # we do not currently have an data. Can you handle this situation in the program?
    # --> the file was specified but it does not exist so we cannot continue using program
    elif not data_file.exists():
        typer.echo("The data file does not exist!")


if __name__ == "__main__":
    # indirectly call the main function through the typer.run function
    typer.run(main)
