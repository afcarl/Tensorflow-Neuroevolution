---
layout: post
title: Development Log of Sprint 10 (Week 15) (19.Aug - 25.Aug 2019)
author: Paul Pauls
---

Completed Tasks in this sprint:

* _Task_: Fixed Bug for Direct-Encoding Model in which the default activation
    function is used as the out activation as well

* _Task_: Further refactored framework to clarify code and optimize speed (
    especially of the Direct-encoding model)

* _Task_: Implemented proper logging

* _Task_: Implemented historic logging of the best genome and its graph after 
    each generation

* _Task_: Added early-stopping functionality to XOR environment to enable a high 
    number of epochs to develop but not waste time on stuck genomes.

* _Task_: Added list of Issues and list of ToDos to project README. Added
    illustration of architecture, showcasing entity relations and the sequence
    diagrom of the core modules.

* _Task_: Created a sepearte branch to create the NEAT algorithm in. Progressed
    on the NEAT algorithm creation, by creation a variant of the YANA algorithm
    that also evolves weights. Eventually historical markings and speciation
    will be added.

