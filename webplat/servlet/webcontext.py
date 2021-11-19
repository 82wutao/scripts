
from typing import Any

WEBCTX_RESPONSE_ENCODING_KEY = "ENCODING"
WEBCTX_RESPONSE_ENCODING_UTF8 = "UTF-8"
# WEBCTX_TEMPLATES_DIR_KEY = "TEMPLATESDIR"
WEBCTX_TEMPLATES_DIR_DEFAULT = "template"
WEBCTX_RESOURCE_DIR_DEFAULT = "resource"
# WEBCTX_WORK_DIR_KEY = "WORKDIR"
WEBCTX_WORK_DIR_DEFAULT = "./"


class WebContext(object):

    def __init__(self, work_dir: str, static_resource: str, template_dir: str, **attrs) -> None:
        super().__init__()
        self.workdir = work_dir
        self.resourcedir = static_resource
        self.templatedir = template_dir
        self.otherattributes = attrs
        pass

    def getstaticpath(self) -> str:
        return self.resourcedir

    def gettemplatedir(self) -> str:
        return self.templatedir

    def getworkdir(self) -> str:
        return self.workdir

    def getotherattr(self, key: str) -> Any:
        r = self.otherattributes.get(key, None)
        return r
