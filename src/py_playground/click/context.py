import click

@click.group()
@click.option('--flag', default='flag default value')
@click.pass_context
def cli(ctx, flag):
    ctx.obj['FLAG'] = flag


@cli.command()
@click.pass_context
def hi_context(ctx):
    click.echo("Now flag value: " + ctx.obj['FLAG'])


if __name__ == '__main__':
    cli(obj={})