1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

step-by-step
1. Buat direktori baru dengan nama toup-up 
2. Buat virtual environment pada direktori tersebut dengan perintah python -m venv env di command prompt
3. Aktifkan virtual environment dengan env\Scripts\activate
4. Di dalam direktori yang sama, buat berkas requirements.txt dan menambahkan beberapa dependencies
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
5. Melakukan instalasi dependencies dengan perintah 
pip install -r requirements.txt
6. Buat proyek Django bernama toup_up dengan perintah django-admin startproject toup_up .
7. Tambahkan "localhost" dan "127.0.0.1" pada ALLOWED_HOST di settings.py sehingga menjadi ALLOWED_HOSTS = ["localhost", "127.0.0.1"] 
8. Menjalankan python manage.py runserver dan membuka http://localhost:8000 di website untuk memastikan aplikasi Django berhasil jalan
9. Menghentikan server dengan Ctrl+C dan menonaktifkan virtual environment dengan perintah deactivate
10. Buat repositori Github baru bernama toup-up dengan visibilitas public
11. inisiasi direktori lokal toup-up sebagai repositori Git dengan perintah git init 
12. Menambah berkas .gitignore yang berisi
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml
.DS_Store

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod]
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery
celerybeat-schedule.*

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history
13. Melakukan add, commit dan push dari direktori repositori lokal
14. 