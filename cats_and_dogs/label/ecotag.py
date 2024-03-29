from dataclasses import dataclass

import aiohttp
import os

from aiohttp import FormData


@dataclass
class ApiInformation:
    api_url: str
    jwt_token: str


@dataclass
class Dataset:
    dataset_name: str
    dataset_type: str
    team_name: str
    directory: str
    classification: str = 'Public'


@dataclass
class Label:
    name: str
    color: str
    id: str


@dataclass
class Project:
    project_name: str
    dataset_name: str
    team_name: str
    numberCrossAnnotation: int = 1
    annotationType: str = "ImageClassifier"
    labels: list[Label] = None


@dataclass
class User:
    id: str


@dataclass
class Group:
    name: str
    userIds: list[str]
    nameIdentifier: str


async def create_dataset(dataset: Dataset, api_information: ApiInformation):
    dataset_name = dataset.dataset_name
    dataset_type = dataset.dataset_type
    team_name = dataset.team_name
    directory = dataset.directory
    classification = dataset.classification

    jwt_token = api_information.jwt_token
    api_url = api_information.api_url

    headers = {'Authorization': f'Bearer {jwt_token}'}

    # Initialize a session.
    async with aiohttp.ClientSession() as session:

        # Fetch the teams and extract the team ID.
        team_id = await get_team_id(api_url, headers, session, team_name)

        # Create the dataset.
        payload = {'name': dataset_name,
                   'type': dataset_type,
                   'groupId': team_id,
                   'classification': classification}

        async with session.post(f'{api_url}/Datasets', headers=headers, json=payload) as response:
            print(f'Create dataset status: {response.status}')
            await response.text()

        dataset_id = await get_dataset_id(api_url, dataset_name, headers, session)

        # Upload image files in the directory.
        print("start uploading files")
        for filename in os.listdir(directory):
            print(f'Uploading file: {filename}')
            if filename.endswith(".jpg") or filename.endswith(".png"):
                data = FormData()
                data.add_field('files',
                               open(os.path.join(directory, filename), 'rb'),
                               filename=filename,
                               content_type='application/octet-stream')

                async with session.post(f'{api_url}/Datasets/{dataset_id}/files', headers=headers, data=data) as response:
                    print(f'upload file status: {response.status} [{filename}]')
                    print(await response.text())

        # Lock the dataset.
        async with session.post(f'{api_url}/Datasets/{dataset_id}/lock', headers=headers) as response:
            print(f'Lock dataset status: {response.status}')
            print(await response.text())


async def get_team_id(api_url, headers, session, team_name):
    team_id = None
    async with session.get(f'{api_url}/Groups', headers=headers) as response:
        print(f'Get teams status: {response.status}')
        teams = await response.json()
        team_id = await get_team_id_from_teams_by_name(team_id, team_name, teams)
        if team_id is None:
            print(f'Team {team_name} not found, we create it for all users')
            payload = {
                "name": team_name
            }
            async with session.post(f'{api_url}/Groups', headers=headers, json=payload) as response_groups:
                print(f'Create group status: {response_groups.status}')
            async with session.get(f'{api_url}/Groups', headers=headers) as last_response_team:
                teams = await last_response_team.json()
                team_id = await get_team_id_from_teams_by_name(team_id, team_name, teams)
            users_ids = await get_users_id(api_url, headers, session)
            payload = {
                "id": team_id,
                "name": team_name,
                "userIds": users_ids
            }
            async with session.put(f'{api_url}/Groups', headers=headers, json=payload) as response_groups:
                print(f'Add users in group status: {response_groups.status}')
        print(f'Team ID: {team_id}')
    return team_id


async def get_team_id_from_teams_by_name(team_id, team_name, teams):
    for team in teams:
        if team['name'] == team_name:
            team_id = team['id']
            break
    return team_id


async def get_users_id(api_url, headers, session) -> list[str]:
    ids = []
    async with session.get(f'{api_url}/Users', headers=headers) as response:
        print(f'Get users status: {response.status}')
        users = await response.json()
        for user in users:
            ids.append(user['id'])
    return ids


async def get_dataset_id(api_url, dataset_name, headers, session):
    # Get Dataset ID.
    dataset_id = None
    async with session.get(f'{api_url}/Datasets', headers=headers) as response:
        datasets = await response.json()
        for dataset in datasets:
            if dataset['name'] == dataset_name:
                dataset_id = dataset['id']
                break
        if dataset_id is None:
            raise Exception(f'Dataset {dataset_name} not found')
        print(f'Dataset ID: {dataset_id}')
    return dataset_id


async def create_project(project: Project, api_information: ApiInformation):
    project_name = project.project_name
    dataset_name = project.dataset_name
    team_name = project.team_name

    jwt_token = api_information.jwt_token
    api_url = api_information.api_url

    headers = {'Authorization': f'Bearer {jwt_token}'}

    async with aiohttp.ClientSession() as session:
        dataset_id = await get_dataset_id(api_url, dataset_name, headers, session)
        team_id = await get_team_id(api_url, headers, session, team_name)

        # Create Image Classification Project.
        payload = {
            "name": project_name,
            "datasetId": dataset_id,
            "groupId": team_id,
            "numberCrossAnnotation": 1,
            "annotationType": "ImageClassifier",
            "labels": []
        }

        for label in project.labels:
            payload['labels'].append(label.__dict__)

        async with session.post(f'{api_url}/Projects', headers=headers, json=payload) as response:
            print(f'Create project status: {response.status}')
            print(await response.text())
