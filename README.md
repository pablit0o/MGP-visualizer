# MGP-visualizer - A visualization of mathematical genealogy
## Context
I created this repository to simulate visualizations with academic (or doctoral) advisors instead of biological descendance. Part of this was inspired by the "Wikipedia game" whereby you try to find the fastest route from one Wikipedia page to another. One of the fields seen in many scientists is the "Academic Advisor" and "Doctoral Students" fields, where you can access a gigantic scientific pedigree of Advisor-Advisee relationships. 

I've noted that there is quite the extensive lineage from any one mathematician to another. I remember Weierstrass in particular had dozens of doctoral advisees. Chances are, if you ever talk to a math professor, you likely talked to someone who talked to someone who...talked to Weierstrass. Also, somehow someway you could always wiki-your way to Euler, Newton, etc. Go past the 1500s-1400s and you don't really see that many mathematicians anymore.

I initially wanted to use Wikidata for accessing this data, but I stumbled upon an even greater resource while researching. The Mathematics Genealogy Project [1] (hence the repo name) gives you a rich source of information for each of their documented mathematicians. Additionally, I also found a repo that did similar functionality to my goal [2], but I personally wanted to widen the things you could do with the MGP data. There are also some fantastic data analysis [3] done on the dataset from MGP. 

Most of the functionality is direct applications of graph theory. As such, it was definitely nice seeing some of compsci knowledge coming to fruition. 

Anyways, from one genealogy geek to another, enjoy!

## Dependencies
- Python 3.6 or above

## Usage
...

The IEEE-style references are denoted as [X], while footnotes are denoted [X*].

## Footnotes
[1*] The MGP API can obscurely be accessed through [1] and going over to the 'Contact Us' page. By selecting 'Request access to data for research purposes', you will be redirected to their API. The code can be found when creating an account and downloading
their sample python script.  
[2*] The mgp_data.json has data queried from the MGP API on 22-06-2026. It contains 346,140 entries. I wanted to note that at around entry 276,244, the MGP API servers were down for a couple days. I couldn't get any response from their API, so I'd highly advise to just
download my dataset to avoid overloading their servers. 

## References
[1] Mathematics Genealogy Project, _Mathematics Genealogy Project_ [Online]. Available: https://www.genealogy.math.ndsu.nodak.edu/. [Accessed: Jun. 22, 2026].  
[2] J. Kun, _math-genealogy-scraper_. Github. [Online]. Available: https://github.com/j2kun/math-genealogy-scraper. [Accessed: Jun. 22, 2026].  
[3] A. Enright, E. Weisstein, _MGP: Computational Exploration in the Wolfram Language_. [Online]. Available: https://blog.wolfram.com/2018/08/02/computational-exploration-of-the-mathematics-genealogy-project-in-the-wolfram-language/. [Accessed: Jun. 30, 2026].