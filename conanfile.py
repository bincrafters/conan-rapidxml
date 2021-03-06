from conans import ConanFile, tools
import os


class RapiXMLConan(ConanFile):
    name = "rapidxml"
    version = "1.13"
    description = "RapidXml is an attempt to create the fastest XML parser possible"
    url = "https://github.com/bincrafters/conan-rapidxml"
    homepage = "http://rapidxml.sourceforge.net"
    license = ("BSL-1.0", "MIT")
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    _source_subfolder = "source_subfolder"
    no_copy_source = True

    def source(self):
        source_url = "https://cfhcable.dl.sourceforge.net/project/rapidxml/rapidxml/rapidxml%20"
        tools.get("{0}{1}/{2}-{3}.zip".format(source_url, self.version, self.name, self.version))
        os.rename(self.name + "-" + self.version, self._source_subfolder)

    def package(self):
        self.copy(pattern="license.txt", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
