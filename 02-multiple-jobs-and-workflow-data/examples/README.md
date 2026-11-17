# Lab example files

Copy the examples directory to the root of your own practice repository.

- prepare/input.txt is the small deterministic input validated by two jobs.
- scripts/generate-report.sh writes output/lab-report.txt. GitHub Actions executes it with Bash on the Ubuntu runner.
- The report includes branch and commit context in Actions. Locally those environment values may be absent; the script prints safe fallback text.

To inspect locally from the lab directory, run:

~~~sh
bash examples/scripts/generate-report.sh
cat output/lab-report.txt
~~~

The workflow uploads only this generated text report and sets artifact retention to seven days. Never add credentials or private content to example inputs.
