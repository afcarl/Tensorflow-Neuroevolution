---
layout: post
title: Development Log of Sprint 7 (Week 8/9) (1.Jul - 14.Jul 2019)
author: Paul Pauls
---

* _Task_: Read up on TF theory and figured out a way to create arbitray
feedforward topologies with sparse layers and connections over multiple layers.
Advantages to preceding methods:
  - Fully compatible with rest of TF infrastructure
  - Even though sparsely connected, it is compatible with GPU acceleration
  - Supports TF on-board optimizers like SGD


* _Task_: Created and implemented OpenAI Gym CartPole environment properly


* _ToDo_: Now that I can implement fast arbitray feedforward topologies, can I
focus on creating a translation from Direct-Encoding (of nodes and connections)
to such a network and therefore create a fast Genome for the eventual NEAT 
implementaion.


* _Thoughts_: Custom topology layers can be accelerated further if there is a
TF functionality that can parallelize the execution of layers. In this case
can I parallelize the independent parts of the topology and accelerate the
genome further.

