# Testing

## Functional Tests

Write tests in files whose name ends with `_test.py` which ensures that they
are picked up by `py.test` command. These test files will contain functions
with function name matching `testXxx` pattern. Put these test files inside the
test directory of same package as the one being tested. This ensures that
unexported functions can also be unit tested.

Refer to documentation of pytest's [testing](https://docs.pytest.org/en/latest/)
framework for detailed information.

**Running tests:**

Run the following command from the test/ directory:

```
$ py.test
```
