import typer
# from utils.exporting import export_level1_to_json, export_schedules, save_schedules, export_groups, save_groups, export_attendance, save_attendance
from utils.faking_names import save_fake_names_to_db
from db.poll_models import Result
from db.db import get_db
from sqlalchemy.orm import Session
from utils.load_polls import run_saving_questions, run_saving_options
from utils.ml_wrapper import filter_groups_by_poll

cli = typer.Typer()

@cli.command()
def hello(name: str):
    print(f"Hello {name}")

@cli.command()
def ml():
    db: Session = next(get_db())
    res = db.query(Result).get(7)
    filter_groups_by_poll(res)

@cli.command()
def exporting():
    # print(Categories()())
    # export_level1_to_json()
    # export_schedules()
    # save_schedules()
    # export_groups()
    # save_groups()
    # export_attendance()
    # save_attendance()
    # save_fake_names_to_db()
    # run_saving_questions()
    run_saving_options()

if __name__ == "__main__":
    cli()
