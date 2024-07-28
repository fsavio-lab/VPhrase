
from api.v1.models import Movie
import pandas as pd
from django.conf import settings
import os.path
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help="file path")

    def handle(self,*args, **options):
        if "path" not in options.keys():
            raise Exception("Please provide a path to the file")
        ingest_movies(options["path"])


def ingest_movies(file_path: str) -> None:
    """
    Ingest Movies CSV file to Movie Model in Database

    param file_path(str): File Path String
    returns: None
    """
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError
        
        movie_data = pd.read_csv(file_path, index_col=False)
        movie_data.index = range(1, len(movie_data["MOVIES"]) + 1, 1)

        # Remove all rows with Movie Name Missing
        movie_data.dropna(subset=["MOVIES"], inplace=True)

        # Drop Unnecessary Columns
        movie_data = movie_data.drop(["ONE-LINE", "STARS", "RunTime"], axis=1)

        # Allocate appropriate datatype to columns
        movie_data["VOTES"] = (
            movie_data["VOTES"]
            .fillna("0")
            .astype(str)
            .apply(lambda x: x.replace(",", ""))
        )
        movie_data["VOTES"] = movie_data["VOTES"].astype(int)
        movie_data["RATING"] = movie_data["RATING"].astype(float).fillna(0.0)
        movie_data["Gross"] = (
            movie_data["Gross"]
            .fillna("$0.00M")
            .astype(str)
            .apply(lambda x : x.replace("$", "").replace("M", ""))
            .astype(float)
            .apply(lambda x : round(x * 100000))
        )

        # Aggregate Data based on necessary columns to remove duplicates
        movie_data = movie_data.groupby("MOVIES").aggregate(
            axis="index",
            func={
                "MOVIES": "first",
                "YEAR": "first",
                "RATING": "mean",
                "VOTES": "mean",
                "Gross": "first",
            },
        )

        # with open(file_path, "r") as movie_file:
        #     reader = csv.DictReader(movie_file)
        # return movie_data.to_dict("records")
        for index, row in enumerate(movie_data.to_dict("records")):
            _ingest_movie_record(index, row)
    except Exception as e:
        # TODO: Logger
        # I would have Logger in place
        # Cant do it due to Time Constraint
        raise e


def _ingest_movie_record(index: int, row: dict) -> None:
    """
    Preprocess and Create Movie Data Record to Database

    param row(dict): CSV Data row
    returns: None
    """
    try:
        movie_obj: Movie = Movie(
            id=index,
            name=row["MOVIES"],
            year=row["YEAR"],
            rating=row["RATING"],
            votes=row["VOTES"],
            grossing_value=row["Gross"]
        )
        movie_obj.save()

    except Exception as e:
        # TODO: Logger
        # I would have Logger in place
        # Cant do it due to Time Constraint
        raise e
