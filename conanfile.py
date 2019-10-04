from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class VireoConan(ConanFile):
    name = "vireo"
    version = "0.1"
    license = "MIT"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "Vireo is a lightweight and versatile video processing library written in C++11"
    topics = ("video processing")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "GPL": [True, False]}
    default_options = {"shared": False, "GPL": False}
    requires = "libjpeg-turbo/2.0.2@bincrafters/stable"

    def source(self):
        repo = tools.Git()
        repo.clone('https://github.com/twitter/vireo', shallow=True)

    def build(self):
        os.chdir(f"{self.source_folder}/vireo")
        autotools = AutoToolsBuildEnvironment(
            self, win_bash=tools.os_info.is_windows)
        args = ["--enable-gpl"] if self.options.GPL else []
        autotools.configure(args=args)
        autotools.make()
        autotools.install()

    def package_info(self):
        self.cpp_info.libs = ["vireo", "imagecore"]
