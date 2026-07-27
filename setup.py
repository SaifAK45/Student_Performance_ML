from setuptools import find_packages,setup

HYPEN_E_DOT = '-e .'  
def get_requiremnt(file_path):
    ''' This function is used to return the list of requirement'''

    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace('\n','') for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement



setup(
    name ='Student-Performance-ML',
    version = '0.0.1',
    author = 'SAIF ALI KHAN',
    author_email='saifalikhan8050@gmail.com',
    packages= find_packages(),
    install_requires = get_requiremnt('requirement.txt'),
)