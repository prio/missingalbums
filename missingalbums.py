import logging
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets.autotag import mb
from beets.ui import decargs


mb.configure()


PLUGIN = 'missingalbums'
log = logging.getLogger('beets')


def _title(artist, title):
    return u"{}: {}".format(artist, title)


def album_title(album):
    return _title(album.albumartist, album.album)


def release_title(artist, release):
    return _title(artist['artist']['name'], release['title'])


class MissingAlbumsPlugin(BeetsPlugin):
    """
    Checks MusicBrainz for any albums you may be missing by an artist

    Decides if its missing using string matching, could be made more
    sophisitcated but it seems to works ok
    """
    def __init__(self):
        super(MissingAlbumsPlugin, self).__init__()
        self._command = Subcommand('missingalbums',
                                   help='returns missing albums',
                                   aliases=['malbum'])

    def commands(self):
        def _miss(lib, opts, args):
            self.config.set_args(opts)
            _seen_titles = []
            albums = lib.albums(decargs(args))
            my_albums = {album_title(album) for album in albums}
            artist_ids = {album.mb_albumartistid
                          for album in albums
                          if (album.mb_albumartistid != ''
                              and album.albumartist.lower() !=
                              "Various Artists".lower())}

            for artist_id in artist_ids:
                artist = mb.musicbrainzngs.get_artist_by_id(
                    artist_id, includes=['releases']
                )
                for release in artist['artist']['release-list']:
                    # Only display if Artist & Title combo is unique
                    #
                    # Does a search through my_albums every loop
                    # which is slower, but means the user gets
                    # results displayed as soon as they are available
                    # (rather than at the end) so it "appears" quicker
                    artist_title = release_title(artist, release)
                    if (artist_title not in my_albums and
                       artist_title not in _seen_titles):
                        _seen_titles.append(artist_title)
                        print u"{} ({})".format(
                            artist_title,
                            release.get('date', 'Unknown').split('-')[0]
                        )

        self._command.func = _miss
        return [self._command]
