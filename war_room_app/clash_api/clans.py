import requests

headers = {'Accept': 'application/json', 'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjAyMGU1ZmRjLWNkYzAtNDlhNS1hM2M2LTU1MDRiMjdmOWNhMyIsImlhdCI6MTQ1NTg1OTA0Mywic3ViIjoiZGV2ZWxvcGVyLzY3ZDk2YzhhLTJiYmUtZjk1YS1lYTUyLWNmMGMzZjI5MGU2ZSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjc2LjIuNjYuMTYzIiwiMTI3LjAuMC4xIl0sInR5cGUiOiJjbGllbnQifV19.242qOS4h9Ga2JAYYDe_qZbVB29d0rEHu3AZzP3ctIWf-FyAcT3yAb8UGNk4-G3rACAS42IWfTzsre5P5aRIIzg'}


def get_clan_by_name(clan_name):
    payload = {'name': clan_name}
    r = requests.get(_url("/clans"), params=payload, headers=headers)
    return r.json()


def get_clan_by_tag(clan_tag):
    r = requests.get(_url("/clans/{}").format(clan_tag), headers=headers)
    return r.json()

def _url(path):
    return 'https://api.clashofclans.com/v1' + path
