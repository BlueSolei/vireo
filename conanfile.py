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
    options = {"shared": [True, False], "GPL": [True, False]}
    default_options = "shared=False", "GPL=False"
    generators = "cmake"
    #requires = "ffmpeg/4.0.2@bincrafters/stable"

    def source(self):
        self.run("git clone --depth 1 https://github.com/twitter/vireo")

    def build(self):
        print("pwd build folder: {}".format(os.getcwd()))
        print("build folder: {}".format(self.build_folder))
        temp_installed_folder = os.path.join(self.build_folder, 'temp_installed')
        with tools.chdir("./vireo/vireo"):
            self.run('./configure --prefix={}'.format(temp_installed_folder))        
            self.run('make')        

    def package(self):
        print("pwd package folder: {}".format(os.getcwd()))
        print("package folder: {}".format(self.package_folder))
        with tools.chdir("./vireo/vireo"):        
            self.run('make install')       
        src_include = 'temp_installed/include'
        src_bin = 'temp_installed/bin'
        src_lib = 'temp_installed/lib'
        self.copy(pattern="*", dst="include", src=src_include)
        self.copy(pattern="*", dst="bin", src=src_bin)
        self.copy(pattern="*.so*", dst="bin", src=src_lib)
        self.copy(pattern="*", dst="lib", src=src_lib)
        # self.copy(pattern="*.lib", dst="lib", src=src_lib)
        # self.copy(pattern="*.a", dst="lib", src=src_lib)

    def package_info(self):
        self.cpp_info.libs = ["vireo", "imagecore"]

# "libpng/1.6.37@bincrafters/stable", \
# "libjpeg/9c@bincrafters/stable", \
# "libfdk_aac/2.0.0@bincrafters/stable", \
# "libvpx/1.8.0@bincrafters/stable", \
# "ogg/1.3.3@bincrafters/stable", \
# "libogg/1.3.2@lasote/vcpkg", \
# "vorbis/1.3.6@bincrafters/stable", \
