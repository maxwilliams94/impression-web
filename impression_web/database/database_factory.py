"""
Factory of platform specific database objects
"""
from impression_web.database.gcp_database import GCPDatabase


class ImpressionDatabaseFactory:
    """
    Platform specific Database objects
    database() creates instances for the chosen platform
    """
    def __init__(self, platform):
        self.platform = platform
        self.cls_ = ImpressionDatabaseFactory._select(platform)

    @staticmethod
    def _select(platform):
        if platform == 'gcp':
            return GCPDatabase
        else:
            raise NotImplementedError(
                f'Invalid platform: {platform}')

    def database(self, *args, **kwargs):
        return self.cls_(*args, **kwargs)
