import os
import argparse
import json
import sys

from jsonschema import validate
import yaml


def get_args():
    """
    Parse the command line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    parser = argparse.ArgumentParser(prog='cms-chatbot', description='Backend for the cms chatbot')
    parser.add_argument('-c', '--config', help='path to the config file', default="/etc/cms-chatbot/conf.yaml")
    args = parser.parse_args()
    return args


def get_config():
    """
    Get the config from the config file.

    Returns:
        dict: The config.
    """
    args = get_args()
    conf_location = args.config
    if os.getenv("CMS_CHATBOT_CONFIG") is not None:
        conf_location = os.getenv("CMS_CHATBOT_CONFIG")
    if not os.path.isfile(conf_location):
        print("Config file", conf_location, "does not exist", file=sys.stderr)
        exit(-1)
    schema = json.load(open(os.getcwd() + "/conf.schema.json", "r"))
    conf = yaml.safe_load(open(conf_location, "r"))
    validate(instance=conf, schema=schema)
    return conf
