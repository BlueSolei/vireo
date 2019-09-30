from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
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

    def source(self):
        self.run("git clone --depth 1 https://github.com/twitter/vireo")

    def build(self):
        temp_installed_folder = os.path.join(self.build_folder, 'temp_installed')
        with tools.chdir("./vireo/vireo"):
            self.run('./configure --prefix={}'.format(temp_installed_folder))        
            self.run('make')        

    def package(self):
        with tools.chdir("./vireo/vireo"):        
            self.run('make install')       
        src_include = 'temp_installed/include'
        src_bin = 'temp_installed/bin'
        src_lib = 'temp_installed/lib'
        self.copy(pattern="*", dst="include", src=src_include)
        self.copy(pattern="*", dst="bin", src=src_bin)
        self.copy(pattern="*.so*", dst="bin", src=src_lib)
        self.copy(pattern="*", dst="lib", src=src_lib)

    def package_info(self):
        self.cpp_info.libs = ["vireo", "imagecore"]
