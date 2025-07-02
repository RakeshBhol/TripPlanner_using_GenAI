```# ***Commands I used: Adding everything to git***```
```
# ***uv --version***
# ***pip install uv***
# ***uv --version***
# ***uv init GENAI_Trip_Planner*** ##Create initial setup using this command
# ***cd GENAI_Trip_Planner***
```
```
deactivate if you have conda cmd installed
# conda deactivate
```
```
# cd GENAI_Trip_Planner
# uv python list
# uv python install cpython-3.11.13-windows-x86_64-none
# uv python list
# uv venv env --python cpython-3.11.13-windows-x86_64-none

# env\Scripts\activate

# uv pip list
# pip --version

# uv pip install langchain
# uv pip list

# git config --list
# doskey/history
```
```
***GIT COMMANDs***
# git add .
# git commit -m "Adding initial folder structure"
# git diff --staged

# git branch development

# git checkout development
# git remote add https://github.com/RakeshBhol/TripPlanner_using_GenAI.git

# git push -u origin development
# git remote show origin
# git push -u origin master

# ### How to know which repo configured in your current cmd ###
# git config --show-origin remote.origin.url
# git config --show-origin user.name
# ## List all configurations ##
git config --list

**push branch changes from development to master**
# git push origin development:master
```
```
# ***uv pip install -r requirements.txt*** 
```
```
***! Commands to start server ***
streamlit run streamlit_app.py  # For running frontend server
uvicorn main:app --reload --port 8000   # For running api server
```