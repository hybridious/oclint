#! /usr/bin/env python

import os

__python_package_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.dirname(__python_package_dir)
root_dir = os.path.dirname(scripts_dir)
build_root = root_dir + os.sep + "build"

def module_source_dir(module_name):
    return root_dir + os.sep + module_name

def oclint_module_source_dir(module_name):
    return module_source_dir("oclint-" + module_name)

def module_build_dir(module_name):
    return build_root + os.sep + module_name

def oclint_module_build_dir(module_name):
    return module_build_dir("oclint-" + module_name)

def oclint_module_test_dir(module_name):
    return module_build_dir("oclint-" + module_name + "-test")    

class Source:
    clang_dir = module_source_dir("llvm")
    googletest_dir = module_source_dir("googletest")

    core_dir = oclint_module_source_dir("core")
    metrics_dir = oclint_module_source_dir("metrics")
    rules_dir = oclint_module_source_dir("rules")
    reporters_dir = oclint_module_source_dir("reporters")
    driver_dir = oclint_module_source_dir("driver")

    json_compilation_database_dir = oclint_module_source_dir("json-compilation-database")
    xcodebuild_dir = oclint_module_source_dir("xcodebuild")

class Build:
    clang_install_dir = module_build_dir("llvm-install")

    core_build_dir = oclint_module_build_dir("core")
    metrics_build_dir = oclint_module_build_dir("metrics")
    rules_build_dir = oclint_module_build_dir("rules")
    reporters_build_dir = oclint_module_build_dir("reporters")
    driver_build_dir = oclint_module_build_dir("driver")
