from instagram.client import InstagramAPI


# Instantiate the Api
class ParmPics(object):
    def __init__(self):
        keys = Keys()
        self._api = InstagramAPI(client_id=keys.get_instagram_client_id(),
                                 client_secret=keys.get_instagram_client_secret())

    def get_recent_parms(self, count=1):
        # Ask for the raw data about the most recent '#chickenparm' post
        media_list = self._api.tag_recent_media(count=count, tag_name="chickenparm")[0]

        def get_url_from_media(media):
            return media.images['standard_resolution'].url

        parm_urls = [get_url_from_media(media) for media in media_list]
        return parm_urls


class Keys(object):
    # these keys are throwaway; let the world see
    @staticmethod
    def get_instagram_client_id():
        return '9fd163440d84417bb5fcb1ee7912a9f3'

    @staticmethod
    def get_instagram_client_secret():
        return '03842f80bb3e47b6972886cd2f38a2e8'