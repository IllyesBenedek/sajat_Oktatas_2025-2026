SELECT job_title, COUNT(*)AS alkalmazottak_száma FROM employees
GROUP BY job_title;