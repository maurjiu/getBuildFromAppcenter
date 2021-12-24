import click
import requests
import json

@click.command()
@click.argument('version')
@click.argument('token')
@click.argument('app_name')
@click.argument('owner_name')
@click.argument('save_path')
def main(version, token, app_name, owner_name, save_path):
    url = "https://api.appcenter.ms/v0.1/apps"
    url_releases = url + "/" + owner_name + "/" + app_name + "/releases" 
    print(url_releases)
    headers = {'Accept': 'application/json','X-API-Token': token}
    response = requests.get(url_releases, headers=headers)
    releases = json.loads(response.text)
    for release in releases :
        if release["version"] == version :  
            build_id = str(release["id"])
            url_downloads = url + "/" + owner_name + "/" + app_name + "/releases/" + build_id
            response = requests.get(url_downloads, headers=headers)
            build = json.loads(response.text)
            url_download_buid = build["download_url"]
            build_file = requests.get(url_download_buid)
            version = release["version"]
            file_extension = release["file_extension"]
            short_version = release["short_version"]
            file_name = app_name + "_" + short_version + "." + version + "." + file_extension
            open(save_path + file_name, 'wb').write(build_file.content)
        break

if __name__ == "__main__":
    main()