---
layout: post
title: Development Log of Week 3 (27.May - 02.June 2019)
author: Paul Pauls
---


* _Task_: Read into Protobuffers and how they will be used in the Tensorflow-Neuroevolution framework. [Google-Developer Protobuffer Guide](https://developers.google.com/protocol-buffers/), [Tensorflow-Protobuffer Guide](https://www.tensorflow.org/guide/extend/model_files), [Tensorflow-Protobuffer Implementation](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/protobuf)


* _Task_: Worked on seminar paper that intends to give an overview of the current state of Neuroevolution and NEAT


* _Task_: Start development of a the first basic neuroevolution framework that realizes the most simple Neuroevolution technique (most likely Binary Tournament Selection with random search). This basic framework has the features:
  - basic mutation / recombination of networks
  - seperate encoding scheme to evolutionary algorithm
  - Basic OpenGym Test environment (double pole balancing)
  - Complete System run
  - Use pickle to save/load models for the first deliverable, afterwards protobuffs

