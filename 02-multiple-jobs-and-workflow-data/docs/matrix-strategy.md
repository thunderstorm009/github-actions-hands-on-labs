# Matrix strategy

A matrix expands one job definition into several executions, one for each configured value or combination. In the lab, Python 3.11, 3.12, and 3.13 each receive an independent runner and run the same assertion.

- **matrix** defines variable values.
- The expression context named matrix reads the value for this execution.
- **fail-fast: false** lets remaining variants finish after one fails.
- **max-parallel** caps simultaneous matrix jobs; actual start time depends on runner availability.

Use a matrix when the same build/test procedure must be checked against several runtimes, platforms, or configurations. Avoid needless combinations that multiply time and cost. See [GitHub matrix jobs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs).
