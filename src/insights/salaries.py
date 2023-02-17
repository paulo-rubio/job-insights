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
    try:
        salario = int(salary)
        minJob = int(job["min_salary"])
        maxJob = int(job["max_salary"])
    except(ValueError, TypeError):
        raise ValueError("")
    except(KeyError):
        raise ValueError("chaves não existentes")
    if minJob > maxJob:
        raise ValueError("max salary precisa ser menor q minsalary")
    return minJob <= salario <= maxJob

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
    salary_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_list.append(job)
        except ValueError:
            pass
    return salary_list

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
