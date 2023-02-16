from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        result = csv.DictReader(file)
        jobs = list()
        for job in result:
            jobs.append(job)
        print(jobs[:2])

    return jobs


def get_unique_job_types(path: str) -> List[str]:
    leitura = read(path)
    jobsTypes = list()

    for dict in leitura:
        if dict["job_type"] not in jobsTypes:
            jobsTypes.append(dict["job_type"])
    return jobsTypes

    """Checks all different job types and returns a list of them

    Must call `read`
''
    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type
        for job in result:
            jobsTypes.append(job["job_type"])
        return jobsTypes
    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
