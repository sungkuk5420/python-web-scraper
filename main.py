from indeed import extract_indeed_pages, extract_indeed_jobs

from save import save_to_file
# jobs = []
# save_to_file(jobs)
max_indeed_pages = extract_indeed_pages()
jobs = extract_indeed_jobs(max_indeed_pages)

save_to_file(jobs)
