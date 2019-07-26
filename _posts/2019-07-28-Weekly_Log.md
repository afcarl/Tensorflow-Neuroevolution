---
layout: post
title: Development Log of Sprint 8 (Week 10/11) (15.Jul - 28.Jul 2019)
author: Paul Pauls
---

Completed Tasks in this sprint:

* _Task_: Realize the proposed genotype encoding (with Gene class etc) properly, 
    though additionally to the Input and Output specification of each connection 
    also specify the activation function. This encoding mimics the encoding 
    style proposed in the original NEAT papers, though since the final genome 
    differs in e.g. being trainable via SGD, is it only 'NEAT-like'.

* _Task_: Create a translation function that translates a 'NEAT-like' encoding into a 
    custom-topological graph that is still highly integrated with TF 2.0, as 
    demonstrated yesterday.

* _Task_: Create a Genome that properly wraps the genotype encoding and translation
    function.

* _Task_: Create a test encoding to create a genome whose translated phenotype
    topology can satisfyingly showcase the CartPole environment when trained via
    SGD.

* _Task_: Create a rudimentary tool to visualize the exact topology of a genome's 
    phenotype

* _Task_: Properly define a base class Genome and subclass the NEAT-like genome from 
    this in the final framework (though this is already employed in the current 
    TFNE framework genomes)

* _Task_: The genome should internally save the genotype as a linked-list. (Also make
    available in the constructor of the genome to create a genome with a 
    genotype specified as linked-list or as a dictionary for fast prototyping, 
    though internally convert to linked-list)

* _Thoughts_: As I now created a NEAT-Like genome with a translation function
for the arbitrary encoded topology, will I now finally be able to focus on
integrating these elements into the new TFNE framework, which will be the focus
of my next sprint

