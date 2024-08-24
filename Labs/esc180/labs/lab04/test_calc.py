import calculator

if __name__ == "__main__":
    calculator.initialize()
    calculator.add(42)
    if calculator.display_current_value() == 42:
        print("Test 1 passed")
    else:
        print("Test 1 failed")