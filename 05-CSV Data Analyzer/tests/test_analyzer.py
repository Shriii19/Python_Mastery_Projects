from analyzer import EmployeeAnalyzer


def test_load_data_returns_employee_dataset() -> None:
    analyzer = EmployeeAnalyzer()

    data = analyzer.load_data()

    assert len(data) == 8
    assert list(data.columns) == ["id", "name", "department", "age", "salary"]