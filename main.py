from send_email import send_email, send_no_new_jobs_found_email
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
    jobs_file = "/home/martin/phd-scraper/jobs.csv"
    old_jobs_df = pd.read_csv(jobs_file)
    scraped_jobs_df = scraper.scrape()
    new_jobs = check_for_new_jobs(old_jobs_df, scraped_jobs_df)
    if len(new_jobs) > 0:
        send_email(new_jobs)
        # Store the scraped jobs in a csv file
        scraped_jobs_df.to_csv(jobs_file)
        print(f"{len(new_jobs)} new jobs found")
        print(f"Stored scraped jobs in '{jobs_file}'")
    else:
        send_no_new_jobs_found_email()
        print("No new jobs found")
    
    
    