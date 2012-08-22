pywebpackages
=========

A collection of modules to help make loading modules and packages directly from the web easy. This has been inspired by Python for iOS which lets you access the web through urllib but which doesn't have a method for downloading packages. This set of tools is there to help bridge the gap.

The first goal is to create a module finder/loader based on pep 302 which can load modules from a given web address using the http protocol.