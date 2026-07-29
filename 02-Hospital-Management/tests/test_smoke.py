from hospital import Hospital


def test_hospital_initializes():
    hospital = Hospital()

    assert isinstance(hospital.patients, list)
    assert isinstance(hospital.doctors, list)
    assert isinstance(hospital.appointments, list)
