# WXML 2021 Project: ImPaCT Improving Panel Consensus Tool

Faculty Mentor: Dr. Marina Meila

Project Description: This project aims to build a visualisation and analysis software to assist in collective decision making. Imagine a student project competition, with n projects, and a jury (sometimes called a *panel*) consisting of m members. Each of the m jury members ranks the n projects. These m rankings may differ from each other, even though one hopes they will have something in common. Sometimes the jury members also “grade” the projects with numerical grades. After independently ranking and grading, the experts need to find some form of consensus. For example, what is the “consensus ranking”, i.e. the ranking that all members of the jury can most easily agree with? If the jury must choose k winners from the n projects, which should these be?

Where is the mathematics? Each ranking is a permutation of n objects. Sometimes the jury members only give you part of the permutation (a partial order). You will have to learn about distances between permutations, and about distributions over the space of all permutations. With clever combinatorics we can calculate probabilities from these distributions very efficiently. Algorithms for finding consensus ranking exist, and some of them are implemented.

This project is mainly about helping a jury (of non-matematicians) use the algorithms. Part I: The team will develop code that visualizes the m rankings, as well as the grades given by the experts, in a way that highlights the amount of consensus and disagreement between them. Part II: Further, the team will use different methods to calculate a consensus ranking, and to “measure” how good is the consensus between experts. Some of these methods are already implemented, other will be the task of the current project. Part III: Finally, all that was calculated in Part II must be displayed to the jury in an intuitive way, to help them make their decision.


Project Level: Intermediate: students who have taken Math 300
Additional Course Requirements: Combinatorics, algebra, probability
Programming Requirements: very good python skills, especially visualization and plotting, numpy, scipy, file management, strings

