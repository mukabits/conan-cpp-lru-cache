import os
from conans import ConanFile, AutoToolsBuildEnvironment, tools


class CppSubprocessConan(ConanFile):
    name = "lrucache"
    version = "1.0"
    license = "BSD-3-Clause License"
    author = "Alexander Ponomarev "
    url = "https://github.com/lamerman/cpp-lru-cache"
    description = "Simple and reliable LRU cache for c++ based on hashmap and linkedlist"
    topics = ("lru-cache", "cache")
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone https://github.com/lamerman/cpp-lru-cache")

    def package(self):
        self.copy("*.hpp", src="cpp-lru-cache/include", dst="lrucache/lrucache")

    def package_info(self):
        self.cpp_info.includedirs = ["lrucache"]
