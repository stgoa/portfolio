
import json
from git import Repo

from portfolio import SETTINGS


with open(SETTINGS.JSON_RESUME_PATH, "r") as file:
    resume = json.load(file)

with open(SETTINGS.JSON_LINKEDIN_PATH, "r") as file:
    linkedin = json.load(file)

with open(SETTINGS.UPDATE_JSON_PATH, "r") as file:
    update= json.load(file)



def update_schema(js:dict, update:dict = None):

    for edu in js["education"]:
        fixed = []
        for course in edu["courses"]:
            fixed.append(course.replace("null - ", "").replace(" - ", ""))
        edu["courses"] = fixed
    
    for certificate in js["certificates"]:
        certificate["date"] = certificate["startDate"]
    

    if update:
        for map in update:
            current_element = js
            keys_path = map["path"].split("-")
            print(f"updating {keys_path}")
            if len(keys_path)>1:
                for key in keys_path[:-1]:
                    if key.isnumeric():
                        key = int(key)
                    current_element = current_element[key]
            final_key = keys_path[-1]
            current_element[final_key] = map["value"]



def update_gist(js:dict):
    with open(SETTINGS.JSON_RESUME_PATH, "w") as file:
        json.dump(js, file, indent = 6)

COMMIT_MESSAGE = 'updated the json resume with the linkedin profile'

def git_push():
    try:
        repo = Repo(SETTINGS.GIT_REPO_PATH)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    




if __name__=="__main__":
    update_schema(linkedin, update=update)
    update_gist(linkedin)
    git_push()