# WXML 2021 Project: ImPaCT Improving Panel Consensus Tool
http://www.wxml.math.washington.edu/?page_id=1272

Faculty Mentor: Dr. Marina Meila

Project Description: This project aims to build a visualisation and analysis software to assist in collective decision making. Imagine a student project competition, with n projects, and a jury (sometimes called a *panel*) consisting of m members. Each of the m jury members ranks the n projects. These m rankings may differ from each other, even though one hopes they will have something in common. Sometimes the jury members also “grade” the projects with numerical grades. After independently ranking and grading, the experts need to find some form of consensus. For example, what is the “consensus ranking”, i.e. the ranking that all members of the jury can most easily agree with? If the jury must choose k winners from the n projects, which should these be?

Where is the mathematics? Each ranking is a permutation of n objects. Sometimes the jury members only give you part of the permutation (a partial order). You will have to learn about distances between permutations, and about distributions over the space of all permutations. With clever combinatorics we can calculate probabilities from these distributions very efficiently. Algorithms for finding consensus ranking exist, and some of them are implemented.

This project is mainly about helping a jury (of non-matematicians) use the algorithms. Part I: The team will develop code that visualizes the m rankings, as well as the grades given by the experts, in a way that highlights the amount of consensus and disagreement between them. Part II: Further, the team will use different methods to calculate a consensus ranking, and to “measure” how good is the consensus between experts. Some of these methods are already implemented, other will be the task of the current project. Part III: Finally, all that was calculated in Part II must be displayed to the jury in an intuitive way, to help them make their decision.


Project Level: Intermediate: students who have taken Math 300
Additional Course Requirements: Combinatorics, algebra, probability
Programming Requirements: very good python skills, especially visualization and plotting, numpy, scipy, file management, strings

_a draft of activities_

Lectures by mentors
=====================
1.  What is Panel Consensus? (Elena, Michael) And how our project will help with that.
2.  Rankings (=permutations), top-k rankings, inversions (Marina)
3.  Software tools for finding consensus (Michael) 

Tasks 
========
1.  Generate artificial panel data (e.g. find a list of movies, books, and generate lists of preferences over them)
    * make a set of movies, books, classes,theorems, foods.... that you all know n=10-20 _candidates/proposals_
    * rank and rate them; ask your friends to do this too m=~10 _panelists_
    * create a form for this
    * give them scores 1-9, with 9 being best. Only integer scores.
    * ((come up with 2-4 criteria of quality; rank them on these criteria)) -- not now!
    * upload the data (.csv for example) on github)
    * present the results to us
5.  Learn to use tools to find consensus ranking (you may write yourselves some of the simpler ones)
6.   Write code to visualize the data
  * visualize the Q matrix
  * visualize Borda score below Q matrix
  * choose appropriaate row/column ordering for Q
  *  visualize Q matrices for criteria and differences with overall Q
     * Visualize raw data:
     * compute inversion distances between raw data and use them to improve visualization
     * compute inversion distances between overall and criteria + visualize the agreement of criteria with overall, between each other
     * visualize pairwise distances as matrix
     * compute distances from each individual data point to consensus
     * _bug in numbering... to fix_
12.  Write software tools for measuring consensus (this may be combined with 5.)
13.  Write code to visualize the consensus ranking [+data]
14.  Bootstrap 
15.  Tools to visualize the measures of consensus (this part may be mixed with previous ones)
16.  Incorporate the consensus ranking tools in the software base.
17.  Write report 
