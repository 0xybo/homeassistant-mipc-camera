@ECHO OFF

@REM Check that the current directory is the project's root directory.
FOR %%A IN ("%cd%") DO (
    SET "directory=%%~nxA"
)
IF %directory% == script (
    CD ..
)

ECHO =================================================================================================
ECHO =                              Hassfest (only manifest plugin)                                  =
ECHO =================================================================================================
ECHO Installing dependencies ...      /
ECHO --------------------------------/
ECHO.

py -m pip install -r script/requirements.txt

ECHO.
ECHO -----------\
ECHO Done !      \
ECHO =================================================================================================
ECHO Running Hassfest ...     /
ECHO ------------------------/
ECHO.

py -m script.hassfest --action validate --integration-path %cd%\custom_components/mipc_camera --plugins manifest

ECHO -----------\
ECHO Done !      \
ECHO =================================================================================================
ECHO.
ECHO Bye !

@REM Back to initial folder
IF %directory% == script (
    CD script
)

@REM Check whether this script is executed in a cmd window that closes at the end.
@REM In this case, pause the script at the end.
ECHO %cmdcmdline% | FINDSTR /l " /c " > NUL
IF %errorLevel% EQU 0 PAUSE