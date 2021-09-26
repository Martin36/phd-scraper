from send_email import send_email
from structs import Job
import pandas as pd
from scrape import Scraper


def check_for_new_jobs(old_jobs_df, scraped_jobs_df):
    new_jobs = []
    for i, row in scraped_jobs_df.iterrows():
        name = row["name"]
        found = old_jobs_df.loc[old_jobs_df["name"].isin([name])]
        if not len(found):
            job = Job()
            job["name"] = name
            job["location"] = row["location"]
            job["department"] = row["department"]
            job["deadline"] = row["deadline"]
            job["link"] = row["link"]
            new_jobs.append(job)
    return new_jobs

if __name__ == "__main__":
    scraper = Scraper()
    # TODO: add check for if the jobs.csv file does not exist
    old_jobs_df = pd.read_csv("jobs.csv")
    scraped_jobs_df = scraper.scrape()
    new_jobs = check_for_new_jobs(old_jobs_df, scraped_jobs_df)
    if len(new_jobs) > 0:
        send_email(new_jobs)
        # Store the scraped jobs in a csv file
        out_file = "jobs.csv"
        scraped_jobs_df.to_csv(out_file)
        print(f"{len(new_jobs)} new jobs found")
        print(f"Stored scraped jobs in '{out_file}'")
    else:
        print("No new jobs found")
    
    
    