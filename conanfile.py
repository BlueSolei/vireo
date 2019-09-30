from conans import ConanFile
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
        os.chdir("./vireo/vireo")
        self.run('./configure --prefix={}'.format(self.package_folder))        
        self.run('make')        

    def package(self):
        os.chdir("./vireo/vireo")
        self.run('make install')       

    def package_info(self):
        self.cpp_info.libs = ["vireo", "imagecore"]
