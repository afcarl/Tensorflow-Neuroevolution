---
layout: post
title: Development Log of Week 2 (20.-26. May 2019)
author: Paul Pauls
---

* _Assignmet_: Main assignment of this week is to research and discuss all available encoding schemes and their advantages and disadvantages.


* _Thoughts_: The neuroevolution research community has largely moved away from evolving  weights through evolution as proposed in the original NEAT algorithm and has moved to modern and very powerful differential techniques like backpropagation.


* _Future Work_: Seperate the code responsible for the genetic encoding scheme from the code applying the evolutionary algorithm. It is common that for a single encoding scheme there are multiple available evolutionary algorithms. Though sometimes an evolutionary method is so closely knit with its encoding scheme that they have to be implemented together - generally seperating those functional units and concerns (genetic encoding, evolutionary algorithm) is good architecture. This will be done later, as current work requires research focus.

