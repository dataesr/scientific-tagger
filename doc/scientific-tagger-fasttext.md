---
title: Content-based subject classification at article level in biomedical context
author:
  - Eric Jeangirard:
      institute: mesri
institute: 
  - mesri:
      name:  'French Ministry of Higher Education, Research and Innovation, Paris, France'
keywords: subject classification, fasttext, 
date: April 2021
lang: en
csl: ieee.csl
citeproc: true
bibliography: tagger.bib
---

# Abstract
Subject classification is an important task to analyze scholarly publications. In general, mainly two kinds of approaches are used : classification at a journal level and classification at the article level. <br>
We propose a mixed approach, leveraging on embeddings technique in NLP to train classifiers with article metadata (title, abstract, keywords in particular) labeled with the journal-level classification FoR (Fields of Research) and then apply theses classifiers at the article level. <br>
We use this approach in the context of biomedical publications using metadata from Pubmed. Fasttext classifiers are trained with FoR codes and used to classify publications based on their available metadata. Results show that using a stratification sampling strategy for training help reduce the biais due to unbalanced fields distribution. An implementation of the method is proposed on the repository https://github.com/dataesr/scientific_tagger

# 1. Introduction

Classifying scholarly literature in subjects or fields can have multiple applications, for example helping for search and discovery in bibliographic and bibliometric tools, creating indicators to understand how a research area is structured or to detect new trends. <br>
In our case, we are building tools to support and help the streering of the Open Science public policy in France. In the French Open Science Monitor [@jeangirard_monitoring_2019], a first attempt to classify publications is proposed in order to monitor the open access trends at the discipline level. With the COVID-19 crisis, the need to open up science in the health field has been reaffirmed. A classification at a lower level in the biomedical area is then needed to help steering the Open Science public policy.

Different approaches for subject classifications have been put in place, both at the journal level and the article level. At the journal-level, expert-based classification are possible, like the ARC journal list [@australian_research_council_arc_era_2018] with university consultations and disciplinary groups feedback. More algorithmic approaches, for example using journal-journal citations pattern [@leydesdorff_global_2009] have been implemented.<br>
Going to a publication-level classification brings several advantages: first, it should allow to classify every type of document, published in a well-established journal or as a preprint. Also, it should handle better article published in multidisciplinar journals like Science or Nature (even though a single article can by itslef be classified as multidisciplinar). <br>
At the article level, clustering techniques are often proposed, based on citations links like [@boyack_clustering_2011] or [@waltman_new_2012]. More recently, content-based deep learning techniques have been applied to wikipedia articles [@semberecki_deep_2017].

In this paper, we investigate an article-level classification method based only on content (not the full-text for now, but metadata like title, abstract, keywords), so not depending on citation indexes, and that could be, maybe, transposed to classify other objects that scholarly publications.


# 2. Method

## 2.1 Data sources

First, we need a datasource for the publications (actually for their metadata). For the moment, we chose a simple, reliable and easy source to harvest, which is Pubmed. Pubmed metadata can easily be harvested through a public API, and the available metadata are rich, including affiliations, abstract, keywords and MeSH (Medical Subject Headings) [@us_nation_library_of_medicine_medical_nodate].

Then we need a labeled database to train machine learning algorithms. That is the tough part as there is no open, recent, comprehensive, article-level tagged publications database. That is why we chose to introduce a proxy to go in-between journal-level and article-level tagging.

Through Excellence in Research for Australia (ERA), the Australian Research Council (ARC) released the ERA 2018 Journal List ([@mercieca_new_2008], [@australian_research_council_arc_era_2018]) . This list associates, for more than 25,000 journals, up to 3 Field of Research (FoR) codes, or ‘MD’ for multidisciplinary journals. This journal-level information can be transposed to an article-level database (all the articles with the same ISSN will be assigned the same fields), that can be used to train algorithms based on the other article-level metadata available, in particular the title, abstract, keywords and MeSH.

The Fields of Research (FoR) is a hierarchical classification, with 2-digits, 4-digits and 6-digits classes. We use the 2-digits and 4-digits FoR codes from the ERA 2018 journal list. More than 150 4-digits FoR codes exist, and most of them are not relevant for a health specific classifier.  

This source present the merits of being quite recent, with a hierarchical structure and produced by a public organization.

Selecting the FoR codes that are relevant for Pubmed papers (and biomedical in general) is not an obvious task. Of course we could limit ourselves to FoR code 11 "Medical and Health Sciences" but that would miss a lot of fields, in particular from Biology, Chemistry and Psychology.<br>
Asking for experts inputs could have been an option but it seems there is no strong consensus on the perimeter. So we eventually chose a quantitative approach, looking at the distribution of the FoR codes in Pubmed data (based on the ISSN).

## 2.2 Training

Getting labeled data at article-level is very costly (high level of domain specific expertise for a huge amount of publications). In the same time, label data does exist at the journal level. We try here to leverage on that data to produce an article-level classifier.

The idea is to extract relevant informations from available metadata (title, abstract, keyword, MeSH) to classify a publication. We assume that, the publications of journals tagged with a given Field of Research, "Chemical Sciences" for example, will contain field-specific words and n-gram in their metadata that will be catched by a machine learning classifier. As a consequence, if an article from, say, a "Multidisciplinary" journal contains enough words specific to "Chemical Sciences", then we guess that a machine learning approach will be able to classify it as "Chemical Sciences" rather than "Multidisciplinary". In that case the classification at the article level would be different from the one at journal level.

We propose to train multiple machine learning models, one for each metadata type: title,  abstract, keywords, MeSH and journal title.

The design of the training dataset is key in the final model relevance and performance. We evaluate two techniques to set-up the training dataset. <br>
First, with a simple random sampling. This way the distribution of the classes in the training dataset is the same as in the whole datatset. <br>
In a second approach, with a stratification sampling, each class being represented equally. The aim of this second sampling technique is to lower the risk of biais: indeed, if the dataset is very unbalanced, with one class being largely predominant, the risk the classifier overfits this class can be high. Imagine an extreme case in which 99% of the cases are tagged with label A, and 1% of the cases with label B. Then a dummy classifier that always predicts A would have a 99% precision, but would miss all the B cases. The idea of the stratified sampling is to train the algorithm with 50% of A cases and 50% of B cases to try to make the algorithm learn more relevant features.

Machine learning models are built with fasttext [@joulin_bag_2016] from Facebook. It uses word embeddings techniques like in word2vec models used in [@semberecki_deep_2017]. Contrary to the latest deep learning models, fasttext is extremely efficient on CPU and very fast, and so is very adapted to low budgets environments.

## 2.3 Prediction

For the field prediction at the article level, we propose to combine the outputs of each of the 5 models (for each metadata available) with a voting system, giving slightly more weight to journal title in case of equality. <br>
Only the prediction with an associated score above a given threshold are taken into account. <br>
As an example, if the model for title and keywords predict "Chemical Sciences" (FoR 03) and the model based on abstract and the one based on journal title predict "Biochemistry and Cell Biology" (FoR 0601), the heuristic to pick up the selected field chooses the second one. <br>
But in another case, if the model for journal title predicts "Multidisciplinary" (MD) whereas models for keywords, MeSH and title predict "Psychology and Cognitive Sciences" (FoR 17), then the heuristic returns the latter, giving a result different from the pure journal title information.

# 3. Results

## 3.1 FoR codes selection

After matching the ISSN from the Pubmed metadata and the ERA journal list, we end up with an article-level database, enriched with Fields of Research (matched at the ISSN level)

**Table 1 : Sample of the available data**

|pmid|issn_electronic|issn_print|journal_title|FoR|
|---|---|---|---|---|
|31739602||2076-2607|Microorganisms|
|31178264|1950-6007||Biomedicine & pharmacotherapy|Pharmacology and Pharmaceutical Sciences|
|31218652|1874-9356||Folia microbiologica|Microbiology;Medical Microbiology|
|31669771|1556-3871||Heart rhythm|Biomedical Engineering;Cardiorespiratory Medicine and Haematology|
|31473396|1095-8630||Journal of environmental management|Multidisciplinary|

We use a sample of 500,000 records published in 2019 from the Pubmed metadata to evaluate the following statistics.

First, it appears that 18% of the publications in PubMed cannot be attached directly to a FoR code as their ISSN is not ERA data giving a correspondance between ISSN and FoR codes.


![Number of FoR matched to publications in Pubmed](https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/images/nb_for_pubmed.png){ width=400 }

At the 2-digits FoR code level, all the 150+ FoR codes are present in the Pubmed data (from FoR 11 "Medical and Health Sciences" for 52% of the papers to FoR 19 "Studies in Creative Arts and Writing" for less than 0.1% of the papers). Note that a paper can be attacted to multiple FoR codes (up to 3).

**Table 2: Distribution of the 2-digits FoR codes in pubmed (sample from 2019)**

|FoR|FoR code| Percentage of publications |
|----|----|----|
| Medical and Health Sciences | 11 | 51.8% 
| Biological Sciences | 06 | 16.8% 
| Chemical Sciences | 03 | 11.3% 
| Engineering | 09 | 8.9% 
| Multidisciplinary | MD | 8.1% 
| Psychology and Cognitive Sciences | 17 | 7.2% 
| Physical Sciences | 02 | 3.2% 
| Agricultural and Veterinary Sciences | 07 | 3.1% 
| other | x | < 3% 

Concerning the the two main codes FoR 11 "Medical and Health Sciences" and FoR 06 "Biological Sciences", we look deeper into the 4-digits FoR codes. For the others, we selected only the FoR codes representing more than 3% of the papers in Pubmed.<br>
With the same logic, for the 4-digits FoR codes in 11 - "Medical and Health Sciences" and 06 - "Biological Sciences", we selected those representing more than 2% of the papers, and grouping the others into "Other Medical and Health Sciences" and "Other Biological Sciences".

After this selection process, we end up with the 17 fields presented in Table 3 to classify publications in Pubmed.

**Table 3: Distribution of the selected fields in pubmed (sample from 2019)**

|Class|FoR code|Percentage of publications
|---|---|---|
| Clinical Sciences | 1103 | 19.9%
| Chemical Sciences | 03 | 11.3%
| Other Medical and Health Sciences |-| 10.3%
| Engineering | 09 | 8.9%
| Multidisciplinary | MD | 8.1%
| Public Health and Health Services| 1117 | 7.4%
| Psychology and Cognitive Sciences | 17 | 7.2%
| Biochemistry and Cell Biology | 0601 | 5.4%
| Neurosciences | 1109 | 4.5%
| Other Biological Sciences |-| 4.5%
| Pharmacology and Pharmaceutical Sciences | 1115 |4.1%
| Oncology and Carcinogenesis | 1112 | 3.7%
| Cardiorespiratory Medicine and Haematology | 1102 | 3.3%
| Physical Sciences | 02 | 3.2%
| Agricultural and Veterinary Sciences | 07 | 3.1%
| Paediatrics and Reproductive Medicine | 1114 | 2.6%
| Microbiology | 0605 | 2.1%

With this field selection, some publications do not get a field anymore (the publications whose ISSN are not the selected scope). However this loss is very low (less than 1%) as shown in Table 4.

**Table 4: Number of fields matched to publications in pubmed**

|Number of fields  | 2-digits FoR | Selected fields
|---|---|---
| 0 | 17.9% |18.7%
| 1 | 37.1% | 56.6%
| 2 | 22.9% | 20.9%
| 3 | 22.1% | 3.8%


## 3.2 Metadata availability in pubmed

In our approach, we assume rich metadata is available, in particular metadata that can help infere a scientific discipline: title, abstract, keywords, MeSH (and journal title).  In the general case (on Crossref for example), for most of the publications, the abstract and keywords are not available. We look here at Pubmed metadata.

**Table 5: Metadata availability in Pubmed (sample from 2019 publications)**

| Metadata | Availability |
|---|---|
| Abstract  | 87.5%
| Keywords | 64.2%
| MeSH | 69.1%
| at least 1 among abstract, keywords, MeSH | 96.6%
| at least 2 among abstract, keywords, MeSH | 80.9%
| all 3 metadata | 43.4%

So the coverage is far from perfect, but in more than 80%, 2 out of 3 key metadata are available.

Field wise, there is of course a variety of situations as shown in Figure 2. However most the selected fields have a good metadata availability, except from "Physical Sciences" (FoR 02) with less than 30% of publications with keywords availble (but abstract is available in more than 95%).<br>
As a consequence, the situation is not perfect (100% availability would be a better scenario) but rich metadata (at least partially) remain available in the vast majority of the cases.


![Proportion of publications with metadata available in Pubmed for the selected fields](https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/images/missing_meta.png){ width=400 }

## 3.3 Training data

We used two training datasets of each 850, 000 publications. Each of them is splitted for training and testing (90%, 10%). The first dataset is a random sample from the Pubmed metadata (with at least a selected field assigned). The second dataset is a stratified sample, each selected field representing an equal part of the total. 

For each dataset, we trained 5 *fasttext* models, on for each metadata type: title, abstract, keywords, MeSH and journal title. The training parameters are presented in Table 6, the other being set to default values. All the possible paramaters and their effects are detailed in fasttext online documentation [@facebook_fasttext_nodate].

**Table 6: fasttext parameters used for training**

| Parameter | Value |
|---|---|
| epoch | 50 |
| wordNgrams | 2
| loss | ova
| minCount | 20

Several metrics can measure the performance of a classifier. In particular, the precision computes the fraction of predicted classes that are relevant, and the recall that computes the fraction of relevant classes that are successfully predicted. The f1 score combines precision and recall  (it is the harmonic mean of precision and recall).<br>
We report the f1 score of each model in Table 7.

**Table 7: f1 score of trained model**

| Sampling technique | Journal title model | Title model | Abstract model | Keywords model | MeSH model
|---|---|---|---|---|---
| Random  | 99.7 | 40.7 | 44.8 | 43.9 | 42.9
| Stratified | 99.9 | 52.2 | 56.1 | 53 | 52.5

We observe that the stratified sampling approach give overall better performance on each model.

We also notice that models based on journal title have almost a perfect f1 score. That can be explained as the model simply tries to replic a simple correspondance between ISSN (and so journal titles) and assigned FoR. The only advantage of the machine learning approach rather than the simple ISSN - FoR correspondance is the generalization for out of sample journals. The model is still able to predict a field, even for journals that are not part of the ERA 2018 journal list.

A part from the journal title model, the performance for the other model could seem low. Actually, we have to keep in my mind that a perfect f1 score is not even the objective, as, in that hypothetic case, the prediction would be exactly the same as the one based only on journal title.

## 3.4 Gaining insights on calibrated fasttext embeddings

fasttext is a word embeddings model, meaning that each word is represented by a numeric vector, in our case in dimension 100. The strength of this type of model is that the numeric distance between these vectors can be interpreted as a semantic distance.

The fasttext library comes with two handy functions to explore the word embeddings: *get_nearest_neighbors* and *get_analogies*. The first function list the words whose embeddings are the closest the input. For instance, using the model calibrated on titles, the 3 neighbors of "pathogen" are "ixodes", "virus" and "host" (the ixodes are a type of ticks, known as desease vectors).

![fasttext 'nearest neighbors' functions to explore word embeddings](https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/images/pathogen.png){ width=350 }

The other function enables the user to play around with word analogies. fasttext documentation gives the example of the triplet ("berlin", "germany", "france"), that can be interpreted as : "What is to France what Berlin is to Germany ?". In fasttext documentation, the first result given by the model they use is "paris". We played the same game with the model calibrated on titles, with the triplet ("hypertension", "heart", "brain"). That is to say, according to the model we calibrated, what is to brain what hypertension is for heart ? The two first results are "subarachnoid" and "seizures".

![fasttext 'analogy' functions to explore word embeddings](https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/images/hypertension.png){ width=400 }

## 3.5 Classification inference

We applied the classification method on 45, 000 publications from Pubmed with a French affiliation. For each one, we computed the field infered with only the journal title and the field predicted using the combination of the 5 models (one for each metadata). For each model, we keep only the predictions with a probability above 0.5. The probability of each tag is directly computed by the fasttext library.<br>
We then look at the transition matrix between journal-based and article-based classification.

![Transition matrix from journal-based to article-based classifier](https://storage.gra.cloud.ovh.net/v1/AUTH_32c5d10cb0fe4519b957064a111717e3/images/transition_matrix.png){ width=400 }


As expected, in the majority of the cases, the article based prediction is the same than the journal level one.<br>
However, a few things can be noticed.<br>
All the articles with no prediction at the journal level are classified with the article-level approach.<br>
Some fields are more re-distributed than others (in particular,  "Multidisciplinary" or "Other Medical and Health Services").
For example, a publication whose title is "'Impact of an early childhood intervention on the home environment, and subsequent effects on child cognitive and emotional development: A secondary analysis.'", published in PloS one was classified "Multidisciplinary" with a journal-based model and became classified "Psychology and Cognitive Sciences" with the combination of the models.
Also, some transitions are more frequent, like "Physical Sciences" to "Engineering" or "Neurosciences" to "Psychology and Cognitive Sciences".

# 4. Discussion and conclusion

In this paper we show how we combined existing and open data sources (Pubmed, Fields of Research) to train a machine learning model able to classify publications in the area of medecine and health. We proposed a mixed approach between journal based and article based classification and apply it to the metadata of French publications in Pubmed. This work was done as a pre-requisite for the construction of the French Open Science Monitor in Health and Medecine that will be released later. We propose a python implementation in https://github.com/dataesr/scientific_tagger

## 4.1 Findings

We first have shown that a combination of 17 Field of Research (2-digits and 4-digits) have a good coverage of the publications in Pubmed, and propose to use these 17 fields for building a biomedical publication classifier.

We also underlined the role of the construction of the training dataset and put in place a technique to handle unbalanced classes distribution using stratification.

With a few examples, we show the ability of fasttext models to manage to encode in their word embeddings at least part of the meaning of the words used in publications metadata (in the title in particular).

Finally we have constructed a heuristic to predict a subject at the article level, using informations from the available metadata (title, abstract, keywords, MeSH and journal title). This method is most of the time inline with a pure journal-based classification, but brings two main advantages, being able to predict a class even if the journal is unknown and handling a bit better the articles published in Multidisciplinary journals.


## 4.2 Limitations and future research

The main limit of this work is the difficulty to evaluate the relevance of the final classification. Indeed, only a manual check on a representative sample of several hundreds of publications would allow to really measure the validity of the approach. That is part of future work we would like to conduct, like [@bornmann_field_2018] but on a larger scale to get insights on the potential biais of our method.

Another way to test the relevance of the output classes would be to use citations patterns to confirm or infirm the classes predictions like in [@wang_large-scale_2016]. 

Finally, we have to keep in mind that at the time of writing of [@joulin_bag_2016], fasttext was very efficient and on par with more complex deep learning architecture, but this area is moving extremely fast and more recent NLP techniques should be investigated as well.

# Software

The source code is released under a MIT licence in the GitHub repository https://github.com/dataesr/scientific_tagger

# References
