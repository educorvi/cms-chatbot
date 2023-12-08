from setuptools import setup, find_packages

requirements = ['jsonschema==4.19.2', 'argparse==1.4.0', 'pyyaml==6.0.1', 'langchain==0.0.348', 'typesense==0.17.0',
                'elasticsearch==8.11.0', 'websockets==12.0', 'peewee==3.17.0', 'deepl==1.16.1', 'openai==1.3.7',
                'pip==23.2.1', 'attrs==23.1.0', 'idna==3.4', 'multidict==6.0.4', 'anyio==3.7.1', 'sniffio==1.3.0',
                'requests==2.31.0', 'numpy==1.26.2', 'setuptools==65.5.0', 'yarl==1.9.2', 'aiohttp==3.8.6',
                'aiosignal==1.3.1', 'frozenlist==1.4.0', 'certifi==2023.7.22', 'greenlet==3.0.1', 'pydantic==2.5.0',
                'urllib3==2.1.0', 'tenacity==8.2.3', 'langsmith==0.0.64', 'packaging==23.2', 'SQLAlchemy==2.0.23',
                'jsonpatch==1.33', 'referencing==0.30.2', 'jsonpointer==2.4', 'marshmallow==3.20.1']
setup(
    name='cms-chatbot',
    version='1.0.0',
    url='https://github.com/educorvi/cms-chatbot',
    license='BSL-1.1',
    author='Julian Pollinger',
    author_email='julian.pollinger@educorvi.de',
    description='Backend for the CMS Chatbot',
    install_requires=requirements,
    packages=find_packages(),
    package_dir={'': '.'},
    # data_files=[
    #     ("/etc/cms-chatbot", ["conf.template.yaml"]),
    #     ("/lib/systemd/system", ["cms-chatbot.service"]),
    #     ('/var/lib/cms-chatbot', []),
    # ],
    entry_points={
        'console_scripts': [
            'cms-chatbot = src.backend:start_backend',
        ],
    },
    package_data={p: ["*"] for p in find_packages()},
)
