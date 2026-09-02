import unittest

from analyzer import EmployeeAnalyzer


class EmployeeAnalyzerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.analyzer = EmployeeAnalyzer()
        self.data = self.analyzer.load_data()

    def test_csv_loading_and_employee_count(self) -> None:
        self.assertEqual(len(self.data), 11)
        self.assertEqual(list(self.data.columns), ["id", "name", "department", "age", "salary"])

    def test_statistics(self) -> None:
        self.assertAlmostEqual(self.analyzer.statistics()["average_salary"], 71_500)

    def test_filtering(self) -> None:
        result = self.analyzer.filter_data(department="IT", salary_gt=75_000)
        self.assertEqual(result["name"].tolist(), ["Aisha Khan"])

    def test_sorting(self) -> None:
        result = self.analyzer.sort_data("salary", ascending=False)
        self.assertEqual(result.iloc[0]["name"], "Mei Chen")

    def test_grouping(self) -> None:
        result = self.analyzer.department_analysis()
        self.assertEqual(result.loc[result["department"] == "Finance", "employee_count"].iloc[0], 3)

    def test_data_quality(self) -> None:
        quality = self.analyzer.data_quality()
        self.assertEqual(quality["missing_values"]["salary"], 1)
        self.assertEqual(quality["duplicate_count"], 1)


if __name__ == "__main__":
    unittest.main()