---
layout: post
title: Development Log of Sprint 9 (Week 12/13/14) (29.Jul - 18.Aug 2019)
author: Paul Pauls
---

Completed Tasks in this sprint:

* _Task_: Refactored framework to decrease coupling, optimize performance, fix
    bugs and clear up API

* _Task_: Integrated arbitray feed forward topology direct-encoding previously
    tested into the Tensorflow framework. Completely overhauled it, optimized it
    and created proper a proper 'encoding' wrapper for the genome so explicitely
    defined genotypes are converted to the genome and sanity-checked.

* _Task_: Integrated XOR problem environment into the tensorflow framework and
    overhauled/adjusted it according to framework requirements

* _Task_: Implemented a version of the YANA algorithm that fits with the direct
    encoding and the XOR environment and consequently implemented a full working
    example using Yana, Direct-Encoding and the XOR environment

* _Task_: Carried over previous cartpole and xor test classes into a test/ 
    folder, though not yet particularly adapted to the framework. Put in ToDo.

* _Task_: Overhauled README and added a lot of documentation to project.

* _Thoughts_: Actual implementation of the NEAT algorithm using direct encoding
    and developing the weights itself is the next task. The framework will also
    profit from increased requests for comments.

