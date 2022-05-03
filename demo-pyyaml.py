import json
import yaml
import pathlib
import requests


with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def get_users() -> dict:
    r = requests.get(config["api_url"])
    return r.text


def save_users(users: dict) -> None:
    path = pathlib.Path(config["save_dir"])
    if not path.exists():
        path.mkdir()

    with open(f"{config['save_dir']}/{config['save_file']}", "w") as f:
        json.dump(users, f)


if __name__ == "__main__":
    users = get_users()
    save_users(users=users)