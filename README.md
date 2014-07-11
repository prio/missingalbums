# Missing Albums Plugin for Beets

I was searching for something like this and came across: https://groups.google.com/forum/#!topic/beets-users/bdIl1r-PAP0. The people involved didn't manage to get it working but this code borrows names etc. from that sample code.

To install create a plugins folder and clone this repo into it. The add the plugins folder to your PYTHONPATH and add `missingalbums` as a plugin to your config.yaml.

```
  mkdir ~/.config/beets/plugins
  cd ~/.config/beets/plugins
  touch __init__.py
  git clone git@github.com:prio/missingalbums.git beetsplug
  export PYTHONPATH=$PYTHONPATH:~/.config/beets/plugins
  beet missingalbums
```
