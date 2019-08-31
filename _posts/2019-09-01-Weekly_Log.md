---
layout: post
title: Development Log of Sprint 11 (Week 16) (26.Aug - 01.Sep 2019)
author: Paul Pauls
---

**As the GSoC 2019 program officially ended this week and the project goals have
  all been sufficiently met will I discontinue this developer diary. The project
  however will continue to be actively developed, though development updates 
  will from now on be given in the patch notes of newly released versions.**


**Thank you for reading my developer diary and using the TFNE framework**


Completed Tasks in this sprint:

* _Task_: Various minor bug fixes and feature additions

* _Task_: Revamped direct encoding to eliminate dependency on prebuilt layers
    but instead define kernel, bias, initializer, building, etc itself in order
    to increase performance and have better control of getting/setting/
    initializing weights.

* _Task_: Differentiate now between regular XOR_environment and Weight-Training
    XOR_environment and implement new regular XOR_environment (which only 
    evaluates, not weight trains, genome)

* _Task_: Introduced Gene-ID bank to give unique Gene-ID to each connection in
    order to enable the principle of Historical markings for NEAT's 
    recombination

* _Task_: Implement creation of initial genomes and new generations for NEAT,
    allowing for recombination and weight-, connection-, node- mutation.
    Only aspect of NEAT missing is speciation, which will be supplied early next
    week.

* _Thought_: During introduction of new algorithm and complete revamp of direct-
    encoding and introduction of a new environment was it never necessary to
    change or adjust the frameworks core. This speaks very favourably for the
    flexibility and architecture design of the framework.

* _Though_: Rezsa reviewed framework and was satisfied with current state, 
    architecture and performance. He considers the project goals fully met.

