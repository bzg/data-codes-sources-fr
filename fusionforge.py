from zeep import Client, Settings

url = "http://localhost:8080/index.xml"
client = Client(url, settings=Settings(strict=False))
session = ""

# for group in client.service.searchGroups(session, ""):
#     print(group)

# for group in client.service.getPublicProjectNames(session):
#     print(group)

# for group in client.service.getGroupsByName(session, ["adel"]):
#     print(group)

print("Repository List")
results = client.service.repositoryapi_repositoryList(session, limit=3, offset=0)
for r in results:
    print(r)

print("Repository Info for repos s2low/svn/s2low (SVN)")
results = client.service.repositoryapi_repositoryInfo(session, "s2low/svn/s2low")
for r in results:
    print(r)

results = client.service.repositoryapi_repositoryInfo(
    session, "ansible-ecole/git/ansible-ecole"
)
for r in results:
    print(r)

print("Repository Info for repos milimail/git/milimail (GIT)")
results = client.service.repositoryapi_repositoryInfo(session, "milimail/git/milimail")
for r in results:
    print(r)
