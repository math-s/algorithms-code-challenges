def test_if_array_is_sorted(array: list):
    for i in range(len(array)):
        try:
            assert array[i] <= array[i+1]
        except IndexError:
            continue
        except AssertionError:
            print("{}>{}", array[i], array[i+1])
