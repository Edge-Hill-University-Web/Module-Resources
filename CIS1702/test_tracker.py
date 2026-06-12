# test_tracker.py

from tracker import (
    add_coursework,
    count_courseworks,
    record_mark,
    calculate_average_mark,
    find_next_deadline,
    save_courseworks,
    load_courseworks,
    generate_progress_report
)


def test_add_coursework():

    courseworks = []

    add_coursework(
        courseworks,
        "Programming 1",
        "CW1",
        "2027-01-15"
    )

    assert len(courseworks) == 1


def test_coursework_structure():

    courseworks = []

    add_coursework(
        courseworks,
        "Programming 1",
        "CW1",
        "2027-01-15"
    )

    coursework = courseworks[0]

    assert coursework["module"] == "Programming 1"
    assert coursework["coursework"] == "CW1"
    assert coursework["deadline"] == "2027-01-15"
    assert coursework["mark"] is None


def test_count_courseworks():

    courseworks = []

    add_coursework(
        courseworks,
        "Programming 1",
        "CW1",
        "2027-01-15"
    )

    add_coursework(
        courseworks,
        "UX Design",
        "Prototype",
        "2027-02-01"
    )

    assert count_courseworks(courseworks) == 2


def test_record_mark():

    courseworks = []

    add_coursework(
        courseworks,
        "Programming 1",
        "CW1",
        "2027-01-15"
    )

    record_mark(
        courseworks,
        "Programming 1",
        "CW1",
        72
    )

    assert courseworks[0]["mark"] == 72


def test_average_mark():

    courseworks = [

        {
            "mark": 60
        },

        {
            "mark": 80
        }

    ]

    assert calculate_average_mark(courseworks) == 70


def test_find_next_deadline():

    courseworks = [

        {
            "module": "Programming",
            "coursework": "CW1",
            "deadline": "2027-02-01",
            "mark": None
        },

        {
            "module": "UX",
            "coursework": "Prototype",
            "deadline": "2027-01-10",
            "mark": None
        }

    ]

    result = find_next_deadline(courseworks)

    assert result["module"] == "UX"


def test_save_data(tmp_path):

    filename = tmp_path / "courseworks.csv"

    courseworks = [

        {
            "module": "Programming",
            "coursework": "CW1",
            "deadline": "2027-01-15",
            "mark": 72
        }

    ]

    save_courseworks(
        courseworks,
        filename
    )

    assert filename.exists()


def test_load_data(tmp_path):

    filename = tmp_path / "courseworks.csv"

    filename.write_text(
        "module,coursework,deadline,mark\n"
        "Programming,CW1,2027-01-15,72\n"
    )

    courseworks = load_courseworks(filename)

    assert len(courseworks) == 1

    assert courseworks[0]["module"] == "Programming"

    assert courseworks[0]["mark"] == 72


def test_progress_report():

    courseworks = [

        {
            "mark": 60
        },

        {
            "mark": 80
        }

    ]

    report = generate_progress_report(courseworks)

    assert report["count"] == 2

    assert report["average"] == 70