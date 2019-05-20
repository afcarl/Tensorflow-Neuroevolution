---
layout: post
title: Development Log of Week 1 (13.-19. May 2019)
author: Paul Pauls
---

* _Task_: Created and set up project repository, development environment and development log


* _Task_: Processed phone call notes and created extensive private notes, roadmap and ToDos


* _Task_: Read up on Tensorflow and read into Architectures of the following Reinforcement Learning Frameworks to check reference work of others:
  - Tensorforce
  - Tensorlayer
  - Deepmind RTFL
  - Google Dopamine
  - OpenAI Baselines
  - RLLib


* _Task_: Read into existing NEAT/Neuroevolution frameworks to check reference work and analysed their strengths and weaknesses:
  - Original Neat
  - NEAT-Python
  - Tensorflow-Neat


* _Task_: Created first presentable architecture-draft of the Tensorflow-Neuroevolution Framework and uploaded to dedicated github branch. [See here](https://github.com/PaulPauls/Tensorflow-Neuroevolution/tree/architecture-draft-1).


* _Thought_: As of now is most of the 'core neuroevolution' functionality (create_genomes, mutate_genomes, select_genomes, speciate_genomes) outsourced into the implementation of the algorithm itself (neuroevolution.algorithms.NEAT). Once I will implement more Neuroevolution algorithms and the common processes between the same functions of two different ne-algorithms become clearer, will I implement those core functions in the core frameworks 'population' module to minimize code replication and decomplexify the algorithms.


* _Research_: Studied up on the following Research papers:
  - 'Large Scale Evolution of Image Classifiers' 
  - 'Regularized Evolution for Image Classifier Architecture Search'
  - 'Neuroevolution: From Architectures to Learning'
  - 'The Age of Analog Networks'
  - 'Efficient Evolution of Neural Networksthrough Complexification' (Kenneth O'Stanley's dissertation)


* _Thought_: Possible Big-Picture Project Milestones:
  - Implementation of a basic Neuroevolution framework in TF 2.0 that maximizes
    in performance and offers drop-in implementation of various specific
    Neuroevolution algorithms
  - Implementation of various specific Neuroevolution algortihms that are fitted to the 
    created Neuroevolution framework. Possible Algorithms: NEAT, HyperNEAT,
    ES-HyperNEAT, Novelty-Search, CoDeepNEAT, etc
  - Extensive Documentation of framework 
  - Extensive Addition of training examples with established RL test environments
  - Extensive test-coverage
  - Visualization of Neuroevolution process and progress via Tensorboard
  - Possible Integration into Tensorflow Ecosystem once it is of sufficient
    quality


* _Future Work_: Research to read:
  - [Research by Claudio Mattiussi](https://sites.google.com/site/claudiomattiussi/Publications), especially his PhD Thesis 'Evolutionary Synthesis of Analog Networks'


* _Future Work_: Further read into established RL architectures and brainstorm first drafts of the Tensorflow-Neuroevolution architecture

