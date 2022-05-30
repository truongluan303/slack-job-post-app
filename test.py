from job_boards_scrapers import LinkedIn

li = LinkedIn()
job = li.get_job_info("https://www.linkedin.com/jobs/view/3092250691/")

print(job)
