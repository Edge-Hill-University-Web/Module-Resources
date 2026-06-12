from superhero import generate_hero_name, assign_power, generate_catchphrase

def test_generate_hero_name_blue_falcon():
    """
    Test 1: Check that generate_hero_name combines 'blue' and 'falcon'
    into the name 'The blue falcon'.
    """
    result = generate_hero_name("blue", "falcon")
    assert result == "The blue falcon", f"Expected 'The blue falcon', but got '{result}'"

def test_generate_hero_name_red_spider():
    """
    Test 2: Check that generate_hero_name combines 'red' and 'spider'
    into the name 'The red spider'.
    """
    result = generate_hero_name("red", "spider")
    assert result == "The red spider", f"Expected 'The red spider', but got '{result}'"

def test_assign_power_fire():
    """
    Test 3: Check that if the element is 'fire', the returned power is
    'Pyrokinesis (Shoots fire from hands)'.
    """
    result = assign_power("fire")
    assert result == "Pyrokinesis (Shoots fire from hands)", f"Expected 'Pyrokinesis...', but got '{result}'"

def test_assign_power_water():
    """
    Test 4: Check that if the element is 'water', the returned power is
    'Hydrokinesis (Controls water currents)'.
    """
    result = assign_power("water")
    assert result == "Hydrokinesis (Controls water currents)", f"Expected 'Hydrokinesis...', but got '{result}'"

def test_assign_power_wind():
    """
    Test 5: Check that if the element is 'wind', the returned power is
    'Aerokinesis (Creates powerful gusts of wind)'.
    """
    result = assign_power("wind")
    assert result == "Aerokinesis (Creates powerful gusts of wind)", f"Expected 'Aerokinesis...', but got '{result}'"

def test_assign_power_default():
    """
    Test 6: Check that if any other element is passed, the returned power is
    'Super Strength'.
    """
    result = assign_power("earth")
    assert result == "Super Strength", f"Expected 'Super Strength', but got '{result}'"

def test_generate_catchphrase_justice():
    """
    Test 7: Check that generate_catchphrase creates the catchphrase:
    'I am The blue falcon and I fight for justice!'
    """
    result = generate_catchphrase("The blue falcon", "justice")
    assert result == "I am The blue falcon and I fight for justice!", f"Expected 'I am The blue falcon...', but got '{result}'"

def test_generate_catchphrase_pizza():
    """
    Test 8: Check that generate_catchphrase creates the catchphrase:
    'I am The red spider and I fight for pizza!'
    """
    result = generate_catchphrase("The red spider", "pizza")
    assert result == "I am The red spider and I fight for pizza!", f"Expected 'I am The red spider...', but got '{result}'"

if __name__ == "__main__":
    tests = [
        test_generate_hero_name_blue_falcon,
        test_generate_hero_name_red_spider,
        test_assign_power_fire,
        test_assign_power_water,
        test_assign_power_wind,
        test_assign_power_default,
        test_generate_catchphrase_justice,
        test_generate_catchphrase_pizza
    ]
    failed = 0
    
    print("=== RUNNING SUPERHERO TDD TESTS ===")
    for test in tests:
        # Extract the short docstring description for printing
        description = test.__doc__.strip().splitlines()[0]
        print(f"Running {test.__name__} ({description})...")
        try:
            test()
            print("✓ Passed!")
        except AssertionError as e:
            print(f"❌ Test Failed!\n{e}\n")
            failed += 1
        except Exception as e:
            print(f"💥 Unexpected system error during test: {e}\n")
            failed += 1
            
    print("================================")
    if failed == 0:
        print("🎉 ALL TESTS PASSED! Your superhero builder works perfectly.")
    else:
        print(f"⚠️ {failed} of {len(tests)} test(s) failed. Time to write some code to fix them!")
