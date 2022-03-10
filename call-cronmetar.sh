#!/bin/bash
#: A bash script to call the cron_metar.py script on an hourly basis.
#: Used with crontab, if this is to be changed to an anacron then a
#: re-write as root is needed with adding the first line in the code
#: set -e
#: and the last line to be
#: exit 0
#: also change shebang to #!/bin/sh

source "$HOME"/github/metar-scraper/.venv/bin/activate