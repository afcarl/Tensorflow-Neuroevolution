---
layout: post
title: Development Log of Week 7 (24.Jun - 30.Jun 2019)
author: Paul Pauls
---


* _Task_: Rework Complete Architecture to better seperate responsibilities. Also:
  - Introduce seperate encoding factory that produces properly configured genomes
  - Make config flexible and enable multiple configuration sections in .cfg
  - Debug and log complete run of fashion mnist environment


* _Task_: Create proper README


* _Issues and ToDos with Framework_:
  - [ ]: Need to check if adding layers retrospectively in KerasLayer encoding is properly solved by rebuilding layers or e.g. if model also needs to be rebuilt
  - [ ]: Fix Bug: That in YANA algorithm the ids of the genomes seem to randomly change
  - [ ]: Implement proper MultiAgent usage and environment
  - [ ]: Implement proper logging
  - [ ]: Implement OpenAI Gym Cartpole Environment


