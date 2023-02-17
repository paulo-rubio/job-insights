from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    list_salary = []
    for dicionario in data:
        if dicionario["max_salary"] and dicionario["max_salary"].isnumeric():
            list_salary.append(int(dicionario["max_salary"]))
    return max(list_salary)
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    data = read(path)
    list_salary = []
    for dicionario in data:
        if dicionario["min_salary"] and dicionario["min_salary"].isnumeric():
            list_salary.append(int(dicionario["min_salary"]))
    return min(list_salary)
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("precisa ter max e min")
    if not isinstance(job["min_salary"], int) or not isinstance(job["max_salary"], int):
        raise ValueError("os valores precisam ser int")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("max salary precisa ser menor q minsalary")
    if not isinstance(salary, int):
        raise ValueError("O valor de 'salary' precisa ser um número inteiro")
    return job["min_salary"] < salary < job["max_salary"]

    """Checks i"f a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    # salary_list = []
    # for job in jobs:
    #     try:
    #       if 
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
