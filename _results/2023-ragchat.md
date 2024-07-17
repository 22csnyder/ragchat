---

title: RAG Chat
description: 'Chat with a PDF - A Working Demo'
author: 
date: 2023-12-01
time_period: 2023
published: true
collections: 
tags: llms, ai, python
categories: Exploratory, Projects, Demos
disciplines: Large Language Models, AI, python

github_repo: 22csnyder/ragchat
thumbnail: 
intro: |
  <a href="https://github.com/22csnyder/ragchat"> GitHub Repo (Working Demo) </a><br>
  While foundation Large Language Models (LLMs) excel at a broad range of non-technical domain tasks, they often struggle in deployment in niche (e.g. institution specific) situations as out-of-dataset challenges inevitably arise. The first solution proposed was to "fine-tune" the LLM model: to do the same as in the preparation of the foundation model, but with training data supplemented strategically with specialized task examples. 

  Interestingly, it was discovered that attention over a crafted context could supplement for training, as data-scientists augmented the language generation process by allowing attention (or at least initialization) over instructive corpora. This represented an interesting paradigm shift as the model itself was always previously--as an identify and a means of training--synonymous with its weights which defined the model. Now, the learned tasks could be augmentated without reference to the parameters at all!

  When entire corpora are of relevance in general, one hopes that each individual question only requires a subset of that context that can be retrieved as per relevance to each question, hence Retrieval Augmented Generation (RAG).

  By this writing in 2024, chat.openai allows one to upload a pdf (e.g. a resume) and ask questions about it, though no such feature existed at time of the original project summarized here. 
  
  This is a working demo of the chat with a pdf feature. It's purpose was to demonstrate the explore and demonstrate the utility and practicallity of RAG as a novel tool for context-aware language modeling.



# permalink:
# excerpt:

content_layout:
  # - section_layout: 2col
  #   images:
  #     - caption:
  #       description: #'Description of the image'
  #       url: #'/projects/abstract-photography/abstract-2.jpg'
  #       width:
  #       height:
  #     - caption:
  #       description:
  #       url:
  #       width:
  #       height:
---

date: 2023-12-01
time_period: 2022
published: false
title: LLM Short Code Snippets

collections:
categories: Exploratory, Projects 
disciplines: Large Language Models, AI, python

thumbnail: 
intro: |
  This is the introduction to the project. Under construction

# permalink:
# excerpt:

content_layout:
  # - section_layout: 2col
  #   images:
  #     - caption:
  #       description: #'Description of the image'
  #       url: #'/projects/abstract-photography/abstract-2.jpg'
  #       width:
  #       height:
  #     - caption:
  #       description:
  #       url:
  #       width:
  #       height:
---


