### Pre-setup:
```
create environment vars :
* projects directory as - "mp"
* Github tocken as      - "gt"
```

### Setup: 
```bash
git clone "https://github.com/therealtgd/project_initializer_automation.git"
cd project_initializer_automation
pip install -r requirements.txt
edit create.bat
copy create.bat to System32 folder
```

### Usage:
```bash
Commands to run the program type

'create <project_name>' - creates a project and adds a public repo on github
'create <project_name> <-p>'   - creates a project and adds a private repo on github
'create <project_name> <-l>'   - creates a project locally
```
