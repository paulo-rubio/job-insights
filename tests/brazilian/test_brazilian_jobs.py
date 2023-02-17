from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_job = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert 'titulo' not in brazilian_job[0]
    assert 'salário' not in brazilian_job[0]
    assert 'tipo' not in brazilian_job[0]
    assert 'title' in brazilian_job[0]
    assert 'salary' in brazilian_job[0]
    assert 'type' in brazilian_job[0]
