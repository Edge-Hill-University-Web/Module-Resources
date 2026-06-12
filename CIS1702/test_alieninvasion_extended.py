import subprocess
import sys
import pytest

def run_script(inputs):
    """
    Runs alieninvasion-extended.py, passing inputs separated by newlines, 
    and returns (stdout, stderr, returncode).
    Times out after 2 seconds to prevent infinite loops.
    """
    try:
        res = subprocess.run(
            [sys.executable, "alieninvasion-extended.py"],
            input=inputs,
            text=True,
            capture_output=True,
            timeout=2
        )
        return res.stdout, res.stderr, res.returncode
    except subprocess.TimeoutExpired as e:
        stdout = e.stdout.decode('utf-8') if e.stdout else ""
        stderr = e.stderr.decode('utf-8') if e.stderr else ""
        pytest.fail(
            f"The script timed out after 2 seconds.\n"
            f"This usually means it is stuck in an infinite loop or waiting for input.\n"
            f"Captured stdout:\n{stdout}\n"
            f"Captured stderr:\n{stderr}"
        )

def get_clean_lines(stdout):
    """
    Removes the prompt string 'Formation height (2-20): ' from the output
    so that we can test the printed output lines independently of TTY prompt echoing.
    """
    cleaned = stdout.replace("Formation height (2-20): ", "")
    cleaned = cleaned.replace("Formation height (2-20):", "")
    return cleaned.splitlines()

# --- Base Tests (Ensuring the core functionality is intact) ---

def test_prompt_for_height():
    """
    Test 1: The program must prompt the user for the formation height 
    using the exact prompt text: 'Formation height (2-20): '
    """
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    assert "Formation height (2-20):" in stdout, (
        "Could not find the prompt 'Formation height (2-20):' in the script's output."
    )

def test_validation_low():
    """
    Test 2: If the formation height input is less than 2, the program 
    must display the warning 'Formation height must be between 2 and 20.' 
    and prompt the user again.
    """
    stdout, stderr, code = run_script("1\n3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    assert "Formation height must be between 2 and 20." in stdout, (
        "Could not find the validation error message for input < 2."
    )
    assert stdout.count("Formation height (2-20):") >= 2, (
        "The script should prompt again after an invalid input of 1."
    )

def test_validation_high():
    """
    Test 3: If the formation height input is greater than 20, the program 
    must display the warning 'Formation height must be between 2 and 20.' 
    and prompt the user again.
    """
    stdout, stderr, code = run_script("21\n3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    assert "Formation height must be between 2 and 20." in stdout, (
        "Could not find the validation error message for input > 20."
    )
    assert stdout.count("Formation height (2-20):") >= 2, (
        "The script should prompt again after an invalid input of 21."
    )

def test_saucer_rendering():
    """
    Test 4: The command saucer '<^>' must be printed and aligned using 
    leading spaces equal to twice the formation height.
    """
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    lines = get_clean_lines(stdout)
    
    saucer_line = None
    for line in lines:
        if "<^>" in line:
            saucer_line = line
            break
            
    assert saucer_line is not None, "Could not find the command saucer '<^>' in the output."
    expected = " " * (3 * 2) + "<^>"
    assert saucer_line == expected, (
        f"Saucer line mismatch.\n"
        f"Expected: '{expected}'\n"
        f"Got:      '{saucer_line}'"
    )

def test_blank_line_after_saucer():
    """
    Test 5: There must be an empty line printed directly after the 
    command saucer line.
    """
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    lines = get_clean_lines(stdout)
    
    saucer_idx = -1
    for idx, line in enumerate(lines):
        if "<^>" in line:
            saucer_idx = idx
            break
            
    assert saucer_idx != -1, "Could not find the command saucer in the output."
    assert saucer_idx + 1 < len(lines), "There should be lines printed after the command saucer."
    
    next_line = lines[saucer_idx + 1]
    assert next_line.strip() == "", (
        f"The line immediately following the saucer must be blank. Got: '{next_line}'"
    )

def test_alien_row_indentation():
    """
    Test 6: The first row of aliens must be indented correctly.
    """
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    lines = get_clean_lines(stdout)
    
    saucer_idx = -1
    for idx, line in enumerate(lines):
        if "<^>" in line:
            saucer_idx = idx
            break
            
    alien_row_idx = saucer_idx + 2
    assert alien_row_idx < len(lines), "Did not find any alien rows printed after the blank line."
    
    first_alien_row = lines[alien_row_idx]
    expected_indentation = " " * ((3 - 1) * 2)
    assert first_alien_row.startswith(expected_indentation), (
        f"Row 1 should start with exactly 4 leading spaces. Got: '{first_alien_row}'"
    )

def test_alien_rows_content():
    """
    Test 7: Each alien row must print the correct number of aliens ('👾 '),
    with each alien followed by a space.
    """
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    lines = get_clean_lines(stdout)
    
    saucer_idx = -1
    for idx, line in enumerate(lines):
        if "<^>" in line:
            saucer_idx = idx
            break
            
    alien_row_idx = saucer_idx + 2
    assert alien_row_idx + 2 < len(lines), "Expected at least 3 alien rows in the output."
    
    assert lines[alien_row_idx] == "    👾 ", f"Row 1 incorrect. Got: '{lines[alien_row_idx]}'"
    assert lines[alien_row_idx + 1] == "  👾 👾 ", f"Row 2 incorrect. Got: '{lines[alien_row_idx + 1]}'"
    assert lines[alien_row_idx + 2] == "👾 👾 👾 ", f"Row 3 incorrect. Got: '{lines[alien_row_idx + 2]}'"


# --- Extended Feature Tests (For alieninvasion-extended.py challenge) ---

def test_blank_line_after_fleet():
    """
    Test 8 (Extended): There must be an empty line printed directly after the 
    last row of the alien fleet, before the total count is printed.
    """
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    lines = get_clean_lines(stdout)
    
    total_idx = -1
    for idx, line in enumerate(lines):
        if "Total aliens unleashed:" in line:
            total_idx = idx
            break
            
    assert total_idx != -1, "Could not find 'Total aliens unleashed:' in the output."
    assert total_idx - 1 >= 0, "The total count line cannot be the first line."
    assert lines[total_idx - 1].strip() == "", (
        f"The line immediately preceding the total count must be blank. Got: '{lines[total_idx - 1]}'"
    )

def test_total_aliens_unleashed():
    """
    Test 9 (Extended): The program must calculate and print the total number of aliens 
    unleashed in the format: 'Total aliens unleashed: <count>'
    For height 3, the count is 6. For height 5, the count is 15.
    """
    # Check height 3
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    assert "Total aliens unleashed: 6" in stdout, "Did not find correct total count (6) for height 3."

    # Check height 5
    stdout, stderr, code = run_script("5\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    assert "Total aliens unleashed: 15" in stdout, "Did not find correct total count (15) for height 5."

def test_full_output_extended_height_3():
    """
    Test 10 (Extended): Check the full, exact layout of the extended fleet printout 
    for a formation height of 3.
    """
    stdout, stderr, code = run_script("3\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    lines = get_clean_lines(stdout)
    
    saucer_idx = -1
    for idx, line in enumerate(lines):
        if "<^>" in line:
            saucer_idx = idx
            break
            
    assert saucer_idx != -1, "Could not find the command saucer."
    
    program_output = lines[saucer_idx:]
    expected_output = [
        "      <^>",
        "",
        "    👾 ",
        "  👾 👾 ",
        "👾 👾 👾 ",
        "",
        "Total aliens unleashed: 6"
    ]
    assert program_output == expected_output, (
        f"Extended output structure mismatch for height 3.\n"
        f"Expected:\n{expected_output}\n"
        f"Got:\n{program_output}"
    )

def test_full_output_extended_height_5():
    """
    Test 11 (Extended): Check the full, exact layout of the extended fleet printout 
    for a formation height of 5.
    """
    stdout, stderr, code = run_script("5\n")
    assert code == 0, f"Script failed with exit code {code}. Error: {stderr}"
    lines = get_clean_lines(stdout)
    
    saucer_idx = -1
    for idx, line in enumerate(lines):
        if "<^>" in line:
            saucer_idx = idx
            break
            
    assert saucer_idx != -1, "Could not find the command saucer."
    
    program_output = lines[saucer_idx:]
    expected_output = [
        "          <^>",
        "",
        "        👾 ",
        "      👾 👾 ",
        "    👾 👾 👾 ",
        "  👾 👾 👾 👾 ",
        "👾 👾 👾 👾 👾 ",
        "",
        "Total aliens unleashed: 15"
    ]
    assert program_output == expected_output, (
        f"Extended output structure mismatch for height 5.\n"
        f"Expected:\n{expected_output}\n"
        f"Got:\n{program_output}"
    )
