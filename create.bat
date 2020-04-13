@echo off

set folder_name=%1
set flag=%2

REM Change work directory to the disk where your projects folder is stored
REM Use just cd C:\...projects_folder if your projects folder is on disk C
e:
cd E:\Documents\code\project_initialization_automation\

if "%1"=="" (
	echo "create <project_name>"
	) else (
		if "%2"=="" (
			python remote.py %folder_name% %flag% && exit	
			) else (
				if "%2"=="-l" (
                	python local.py %folder_name% && exit	
            		) else (
            			if "%2" == "-p" (
            				python remote_private.py %folder_name% %flag% && exit	
            				)
            		) 
			)
	)