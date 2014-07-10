# Missing Albums Plugin for Beets

To install create a plugins folder and clone this repo into it. The add the plugins folder to your PYTHONPATH and add `missingalbums` as a plugin to your config.yaml.

  mkdir ~/.config/beets/plugins
  cd ~/.config/beets/plugins
  touch __init__.py
  git clone git@github.com:prio/missingalbums.git beetsplug
  export PYTHONPATH=$PYTHONPATH:~/.config/beets/plugins
  beet missingalbums

