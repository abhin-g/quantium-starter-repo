@echo off

rem Activate the virtual environment (replace 'venv' with the name of your virtual environment)
call myenv\Scripts\activate

rem Execute the test suite (replace 'test_suite_command' with the actual command to run your tests)
set test_suite_command=pytest -sv test_app.py  
%test_suite_command%

rem Get the exit code of the test suite execution
set exit_code=%errorlevel%

rem Deactivate the virtual environment
deactivate

rem Return the exit code
exit /b %exit_code%
