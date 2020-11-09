import pandas as pd

JOBS_DATA_PATH = "data/jobs.csv"


class JobDataFetcher:
    def __init__(self):
        self.dataframe = pd.read_csv(JOBS_DATA_PATH)

    def get_job(self, name):
        name = name.lower()
        return self.dataframe[self.dataframe["Title"].str.contains(name, case=False)]

    def get_product_info(self, name):
        return self.get_product(name)["Job description"].iloc[0]

    def get_application_link(self, name):
        return self.get_product(name)["Where to apply"].iloc[0]

    def get_jobs_by_skill(self, skill):
        skill = skill.lower()
        return self.dataframe[self.dataframe["Technology"].str.contains(skill, case=False)]
