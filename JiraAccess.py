# This code sample uses the 'requests' library:
# http://docs.python-requests.org
# import requests
# from requests.auth import HTTPBasicAuth
# import json
#
# url = "https://extrawest.atlassian.net/rest/api/3/users/search"
#
# auth = HTTPBasicAuth("email@example.com", "<api_token>")
#
# headers = {
#    "Accept": "application/json"
# }
#
# response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    auth=auth
# )
#
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


from jira.client import JIRA

jira_server = "https://jira.extrawest.com/"
jira_user = "oleksii.yentis"
jira_password = ""

jira_server = {'server': jira_server}
jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_password))

group = jira.group_members("jira-users")
for users in group:
    print(users)

