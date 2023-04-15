from flask import Flask, request, render_template
import yaml
import subprocess

app = Flask(__name__)

@app.route('/update_meltano_config', methods=['POST'])
def update_meltano_config():
    # get form data
    extractor = request.form['extractor']
    loader = request.form['loader']
    access_token = request.form['access_token']
    start_date = request.form['start_date']
    repository = request.form['repository']
    path = request.form['path']

    # modify meltano.yml file
    with open('meltano.yml', 'r') as f:
        config = yaml.safe_load(f)

    # update extractor config
    for plugin in config.get('plugins', {}).get('extractors', []):
        if plugin['name'] == extractor:
            plugin['config']['repository'] = repository
            plugin['config']['start_date'] = start_date
            plugin['config']['access_token'] = access_token

    # update loader config
    for plugin in config.get('plugins', {}).get('loaders', []):
        if plugin['name'] == loader:
            plugin['config']['destination_path'] = path

    with open('meltano.yml', 'w') as f:
        yaml.dump(config, f)

    # run meltano elt command
    elt_command = ['meltano', 'elt', extractor, loader]
    subprocess.run(elt_command)

    return 'Your Data is Loaded into the Directory !'


@app.route('/')
def index():
    return render_template('ui.html')

if __name__ == '__main__':
    app.run(debug=True)
