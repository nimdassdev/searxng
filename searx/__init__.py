'''
searx is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

searx is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with searx. If not, see < http://www.gnu.org/licenses/ >.

(C) 2013- by Adam Tauber, <asciimoo@gmail.com>
'''

from os import environ
from os.path import realpath, dirname, join, abspath
from searx.https_rewrite import load_https_rules
try:
    from yaml import load
except:
    from sys import exit, stderr
    stderr.write('[E] install pyyaml\n')
    exit(2)

searx_dir = abspath(dirname(__file__))
engine_dir = dirname(realpath(__file__))

# if possible set path to settings using the enviroment variable SEARX_SETTINGS_PATH
if 'SEARX_SETTINGS_PATH' in environ:
    settings_path = environ['SEARX_SETTINGS_PATH']
# otherwise using default path
else:
    settings_path = join(searx_dir, 'settings.yml')

if 'SEARX_HTTPS_REWRITE_PATH' in environ:
    https_rewrite_path = environ['SEARX_HTTPS_REWRITE_PATH']
else:
    https_rewrite_path = join(searx_dir, 'https_rules')

# load settings
with open(settings_path) as settings_yaml:
    settings = load(settings_yaml)

# load https rules only if https rewrite is enabled
if settings.get('server', {}).get('https_rewrite'):
    # loade https rules
    load_https_rules(https_rewrite_path)
