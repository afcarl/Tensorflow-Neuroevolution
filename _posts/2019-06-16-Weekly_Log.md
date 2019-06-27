---
layout: post
title: Development Log of Week 5 and 6 (10.Jun - 23.Jun 2019)
author: Paul Pauls
---


* _Task_: Create a complete test architecture with a test algorithm ('YANA') and fashion mnist dataset as the accuracy environment. The 'YANA' algorithm is configured via a seperate .cfg file, which has a YANA section and is configured through it. The YANA algorithm itself is very basic and only mutates genomes in a very basic way, adding a DENSE layer. Create Fashion-MNIST test environment to train Image Classifiers.


* _Task_: Finish seminar paper that gives an overview of the current state of Neuroevolution and NEAT. See [here](https://github.com/PaulPauls/Neuroevolution_of_Augmenting_Topologies_Paper).


* _Notes_: A simple save/load of population with pickle or dill package won't work due to the complicated nature of the population object.

