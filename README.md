
<h1 align="center">CPL 2019: Foxes & Marksmen</h1>
<h3 align="center">Looking at the willy foxes and marksmen in the Canadian Premier League 2019</h3>
<br>

<!--Introduction-->
<h4>Introduction</h4>
Having obtained the statistics for inaugural Canadian Premier League 2019 season, I thought for a while I can do with the statistics. What facts would I want to find out about?

With this script, I present my first findings derived from this dataset - to find out the players putting themselves in great positions and the sharpshooter
<br>
<br>
<!--Built With: Language and Packages-->
<h4>Built With</h4>
Language: Python
<br>
Packages: Pandas, Matplotlib
<br>
<br>
<!--Methodology-->
<h4>Further Details</h4>

The player season long statistics were in the form of csv. With pandas, I am able to pull the data in the csv into a dataframe and put in additional statistics to be used to plot the scatter plot.

Two characteristics of a good striker that one can consider is having good positioning and to be able to convert chance. With the objective of trying to measure good positioning, I used the metric of xG/Shots. If the player was able to obtain high average xG per shot that they take, one may presume that they were able to position themselves well to be able to get a high xG shot. For good conversion of chances I used goals/xG as a ratio of how much they were able to overperform with regards to the expected chances they were having.

The data for shots taken were separately presented as shots on target ('SOG'), off target ('Off'), and inclusive of penalties.
The goals and xG ('ExpG') statistics were also inclusive of penalty shots. Therefore, I had to remove the statistics to penalties as we are looking at how the player performed in open play, and penalties-related statistics will skew our understanding of the statistics.

Players with high average xG (good positioning) are labelled 'foxes', with no indication of their finishing ability, while players who were able to convert their chances well were labelled 'marksmen' for their accuracy (with no indication of their ability to get into good positions). Players who were able to fulfil both criteria were labelled 'all-stars' in recognition of their overall ability.

The scatter plot was created with the top quartile of players by number of shots (43 players in this case, more than enough to cover notable players in a league of seven teams) to prevent players with low playing time from skew the statistics (eg. played little but had one good chance). We also want a relatively high number of shots so that we are able to gather a more complete understanding of the actions by the player.
<br>
<br>
<!--Results-->
<h4>Results</h4>


![Scatter Plot: Foxes & Marksmen CPL 2019](https://github.com/gdianxiang/cpl_2019_foxes_and_marksmen/blob/b2093a974a405a6a60a19209e740a8c69ce4dddc/cpl2019_foxes_marksmen_scatter%20plot_result.png)


<!--Observations-->
<h4>Looking At The Results</h4>
Based on the produced scatter plot, we are able to see that the best overall performer for Season 2019 was Anthony Novak (Forge FC) and Tyler Attardo (Valour FC).

Highly rated foxes for the season based on the data include Easton Ongaro (FC Edmonton), Dominique Malonga (Calvary FC), Jordon Brown (Calvary FC), Emery Welshman (Forge FC), and Marcel Zajac (Forge FC).

Notable marksmen include Julian Büscher (Calvary FC), Victor Blasco (Pacific FC), Christopher Nanco (Forge FC), Tristan Borges (Forge FC), and Dylan Carreiro (Valour FC).

One may also notice that the best Fox (Sergio Camargo, Calvary FC) and Marksman (Julian Büscher, Calvary FC) were extreme outliers in their category, which played a part in making the All-Stars look less impressive on the chart. Checking back on the data, despite being a strong finisher, Julian Büscher took but missed one penalty shot. Nevertheless, they set the respective benchmark for their league for the season based on the statistics provided. Perhaps if the two of them had done a dragonball fusion, Cavalry FC would have been able to win the World Cup.

<!--Addendum-->
<h4>Addendum</h4>

* You can also obtain the dataset for free by registering your email [here](https://canpl.ca/centre-circle-data/), with breakdown of data on a game-by-game basis and season overall. Thank you to the Canadian Premier League for your willingness to put out the data for free.
* York9 FC was subsequently renamed York United. For the purpose of this chart I kept to the name as they were officially known then.
* The inaugural Canadian Premier League season in 2019 had only seven teams. Atlético Ottawa joined the league in the 2020 season.