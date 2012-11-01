from django.conf import settings as django_settings


class LazySettings(object):
    
    @property
    def REQUIRE_BASE_URL(self):
        return getattr(django_settings, "REQUIRE_BASE_URL", "js")
    
    @property
    def REQUIRE_BUILD_PROFILE(self):
        return getattr(django_settings, "REQUIRE_BUILD_PROFILE", None)
    
    @property
    def REQUIRE_JS(self):
        return getattr(django_settings, "REQUIRE_JS", "require.js")
    
    @property
    def REQUIRE_STANDALONE_MODULES(self):
        return getattr(django_settings, "REQUIRE_STANDALONE_MODULES", {})
    
    @property
    def REQUIRE_DEBUG(self):
        return getattr(django_settings, "REQUIRE_DEBUG", settings.DEBUG)
    
    @property
    def REQUIRE_EXCLUDE(self):
        return getattr(django_settings, "REQUIRE_EXCLUDE", ("build.txt",))
    
    
settings = LazySettings()