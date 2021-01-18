from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs

so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
jobs = so_jobs + indeed_jobs 
print(jobs)

# https://nomadcoders.co/python-for-beginners/lectures/131
# 0:16 부터 