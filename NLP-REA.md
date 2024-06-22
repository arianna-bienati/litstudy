# An NLP-mediated dialogue with the Reggio Emilia Approach

Arianna Bienati<sup>1,2</sup>

<sup>1</sup> Università degli Studi di Modena e Reggio Emilia  
<sup>2</sup> Eurac Research

*keywords*: NLP, literature review, postgraduates, Reggio Emilia Approach.

Writing an in-depth and comprehensive literature review is one of the most critical tasks during a PhD. Reviews not only provide readers with the framework that grounds the empirical or theoretical work and explain the choice of research question and its relevance, but also, and perhaps more importantly, they document the process with which the acquired knowledge has been organized and synthetized. Performing a review is becoming increasingly professionalized, with a large body of research dealing with the definition of the different types of reviews (e.g., Grant & Booth, 2009) and the methodologies and best practices that support them (e.g., Page et al., 2021). In this framework, the emergence of computational, often NLP-powered tools to help with the automatation of data extraction as well as coding is gaining huge momentum, both commercially (e.g., [Connected Papers](https://www.connectedpapers.com/), [Research Rabbit](https://www.researchrabbit.ai/)) and in the academia (e.g., van Dinter et al., 2021; de la Torre-López et al., 2023).

In this work, Litstudy (Heldens et al., 2022), a freely available, open-source tool based on Natural Language Processing (NLP), is used to perform a mapping review (Campbell et al., 2023) of the different topics related to the Reggio Emilia Approach (REA), an educational philosophy centered on the child as a subject with strong developmental capabilities and rights. Litstudy automates the literature review process by accessing the main bibliographic data sources, such as [Scopus](https://www.elsevier.com/products/scopus), [Semantic Scholar](https://www.semanticscholar.org/about) and [CrossRef](https://www.crossref.org/about/). Bibliographic data can then be analyzed via descriptive statistics and visualizations, as well as network graphs and topic modeling, an automated analysis whose aim is to find abstract topics from a collection of documents. The insights gained from the topic modeling will be interpreted in the light of one year of readings that inspired the REA, which was meant for understanding the historical foundations and main philosophical, psychological and educational principles of the approach.

For the present study, only bibliographic data indexed in Scopus, for a total of 1653 papers, were used to perform the analyses. Results show that publications date from 1994 and follow an increasing trend (see fig. \ref{years}).

![years\label{years}](/Users/ariannabienati/git/litstudy/years.png)

The United States and the United Kingdom, followed by Australia, Canada, Italy, and Turkey, are the countries where institutions publish the most on the REA in absolute numbers (see fig. \ref{countries}). We can thus infer from the missing 'big countries', such as China and India, that the approach is firmly positioned in the western educational world and as a western 'invention'.

![countries\label{countries}](/Users/ariannabienati/git/litstudy/countries.png)

Topics automatically extracted from the topic modeling, presented in fig. \ref{topics}, reflect the centrality of the child, especially in the pre-school years, and their relationship with the teachers and the environment, often called the 'third teacher' (Strong-Wilson & Ellis, 2007). A large body of research is dedicated to teachers, their professional development and the methods, such as pedagogical documentation (e.g., Fleet & Machado, 2022), with which they document their work in the classroom. Particular attention is given to the topics of inclusivity and disabilities (e.g., Gilman, 2007), which clearly cluster together, forming a distinct yet interrelated research strand. One of the fundamental tenets of the REA, the existence and interplay of multiple 'languages' (i.e., the hundred languages, Edwards et al., 1998) in the repertoires of the children, emerges as the model classifies papers, clustering them around either 'language' and 'multilingualism', 'art' and 'drawing', 'music' and 'multimodality'. The idea of an educational model that leverages the playfulness of the children is also clearly detected by the topic modeling, as we can see from the group of studies aggregated under the labels 'play' and 'construction'. Lastly, 'curriculum' and 'assessment' represent two additional focai, often re-elaborated and innovated with respect to traditional curricula and assessment techniques (e.g., Helm, 2011).

![topic modeling\label{topics}](/Users/ariannabienati/git/litstudy/topicmodeling.png)

Automating the review process of the scientific output from 1994 to 2024 on the REA proved useful for obtaining a bird's-eye view of the most central topics to the approach. Although still broad and exploratory, the review seems to return an accurate picture of the possible research strands within or closely related to the REA. These results, however, could not be interpreted without the one-year dialogue with the literature that inspired the approach. The automated NLP-mediated process, therefore, could be used as either a first exploratory step or a litmus test to see if large amounts of, often noisy, data coincide with the richer insights one could get from direct socialization in the research community that investigates these topics.

### References
Campbell, F., Tricco, A. C., Munn, Z., Pollock, D., Saran, A., Sutton, A., White, H., & Khalil, H. (2023). Mapping reviews, scoping reviews, and evidence and gap maps (EGMs): The same but different— the “Big Picture” review family. Systematic Reviews, 12(1), 45. https://doi.org/10.1186/s13643-023-02178-5  
de la Torre-López, J., Ramírez, A., & Romero, J. R. (2023). Artificial intelligence to automate the systematic review of scientific literature. Computing, 105(10), 2171–2194. https://doi.org/10.1007/s00607-023-01181-x  
Edwards, C., Gandini, L., & Forman, G. (1998). The Hundred Languages of Children: The Reggio Emilia Approach Advanced Reflections. Bloomsbury Publishing USA.  
Fleet, A., & Machado, I. (2022). Special Issue on Pedagogical Documentation – Researching a Powerful and Evolving Idea. European Early Childhood Education Research Journal, 30(2), 179–183. https://doi.org/10.1080/1350293X.2022.2051244  
Gilman, S. (2007). Including the Child With Special Needs: Learning From Reggio Emilia. Theory Into Practice, 46(1), 23–31. https://doi.org/10.1080/00405840709336545  
Grant, M. J., & Booth, A. (2009). A typology of reviews: An analysis of 14 review types and associated methodologies. Health Information & Libraries Journal, 26(2), 91–108. https://doi.org/10.1111/j.1471-1842.2009.00848.x  
Heldens, S., Sclocco, A., Dreuning, H., van Werkhoven, B., Hijma, P., Maassen, J., & van Nieuwpoort, R. V. (2022). litstudy: A Python package for literature reviews. SoftwareX, 20, 101207. https://doi.org/10.1016/j.softx.2022.101207  
Helm, J. H. (2011). From Theory to Curriculum: The Project Approach. In Curriculum in Early Childhood Education. Routledge.  
Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. BMJ, 372, n71. https://doi.org/10.1136/bmj.n71  
Strong-Wilson, T., & Ellis, J. (2007). Children and Place: Reggio Emilia’s Environment As Third Teacher. Theory Into Practice, 46(1), 40–47. https://doi.org/10.1080/00405840709336547  
van Dinter, R., Tekinerdogan, B., & Catal, C. (2021). Automation of systematic literature reviews: A systematic literature review. Information and Software Technology, 136, 106589. https://doi.org/10.1016/j.infsof.2021.106589