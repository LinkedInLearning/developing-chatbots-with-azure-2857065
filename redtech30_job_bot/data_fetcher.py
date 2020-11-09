import pandas as pd

JOBS_DATA_PATH = "data/jobs.csv"


class JobDataFetcher:
    def __init__(self):
        self.dataframe = pd.read_csv(JOBS_DATA_PATH)

    def get_job(self, technology=None, years=None, location=None):
        technology = ", ".join(technology) if technology else ""
        location = ", ".join(location) if location else ""
        years = int(years[0])
        return self.dataframe[(self.dataframe["Technology"].str.contains(technology, case=False)) & 
                              (self.dataframe["Years of experience"] <= years) &
                              (self.dataframe["Location"].str.contains(location, case=False))  ]
