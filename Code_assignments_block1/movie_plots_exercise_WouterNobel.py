import pandas as pd

#In this exercise, we're going to create a program that allows us do 
#cross-cultural cinematic research. A tool that prints the percentage of movie
#descriptions containing a certain word (scraped from Wikipedia),
#for different cultures. First we will practice a little with Pandas.
#Then, follow the steps to create the program.

#As a challenge, you can also ignore these steps and code it without help.

#1. First, download the movie_plots.csv file from Canvas and open it

#import dataset
movie_plots = pd.read_csv("C:/Users/woute/Documents/Minor/Assignments/Assignment_2/movie_plots-1.csv") #open the file from the saved location

#2. Let's inspect the data. Display the first rows and get the summary (.info)
print(movie_plots.head()) #print the first rows
print(movie_plots.info()) #print the summary

#3. Print out the number of movies for each Origin/Ethnicity
print(movie_plots["Origin/Ethnicity"].value_counts()) # print out the amount of movies for each Origin/Ethnicity

#4. Subsetting: select only the rows with Bollywood movies
bollywood_movies = movie_plots[movie_plots["Origin/Ethnicity"] == "Bollywood"] #subsetting where origin/ethnicity is equale to Bollywool

#5. Subsetting: select only the rows with Turkish movies released after 2000
Turkish_mov_aftr_00 = movie_plots[(movie_plots["Origin/Ethnicity"] == "Turkish") & (movie_plots["Release Year"] >= 2000)] #subsetting where origin/ethnicity is equale to Turkish and the release year is above 2000

#6. Subsetting: create a new df with only Title, Release Year, Origin/Ethnicity, Plot
Mov_Tit_RelY_Orig_plot = movie_plots[["Title", "Release Year", "Origin/Ethnicity", "Plot"]]

#7. Change the column names to Title, Year, Origin, Plot. Find online how to this.
Mov_Tit_RelY_Orig_plot = Mov_Tit_RelY_Orig_plot.rename(columns ={ 
    "Release Year": "Year", #change the name of release year to just Year
    "Origin/Ethnicity" : "Origin" #change the name of origin/ethnicity to just origin
    })

##This is where the basic section ends.##
##Advanced section: for a more challenging assignment, try (some of) the steps below##

#8. Create a new column "kimono" that is True if the Plot contains the word "kimono"
#and false if not (tip: find a suitable Pandas string method).
#Tip: use Pandas .astype(int) to convert the resulting Boolean in 0 or 1.
Mov_Tit_RelY_Orig_plot["kimono"] = Mov_Tit_RelY_Orig_plot["Plot"].str.contains("kimono", na = False) #looks in the plot string for the word kimono if nothing is there put False

#9. Using your new column, pd.groupby() and another Pandas function, count the number of movies
#with "kimono" in the plot, for the different origins.

kimono_origin_count = Mov_Tit_RelY_Orig_plot.groupby("Origin")["kimono"].sum()

#10. Using your earlier code, create a function add_word_present() with one argument (word),
#that adds a column df[word] with a 1 if the word occurs in the plot,
#and 0 if not.
#Extra challenge: make sure that it's not counted if it's inside another word.
def add_word_present(word):
    Mov_Tit_RelY_Orig_plot[word] = Mov_Tit_RelY_Orig_plot["Plot"].str.contains(rf"\b{word}\b", na = False).astype(int) #make an new colum in movie_plots with the given word, the rf"\b{word}\b" ensures that it isnt containd a a other word


#11. Write another function compare_origins() with one argument (word), that:
#1. adds a column to your data frame (simply call your earlier function)
#2. prints the proportion of movies for different origins containing that word

def compare_origins(word):
    add_word_present(word) #example with the word Man
    print("Comparing origins of word: " + word)
    print(Mov_Tit_RelY_Orig_plot.groupby("Origin")[word].mean()) # Computes the proportion of movies where the word appears (since 1 = word present and 0 = word absent, the mean gives the proportion).


compare_origins("He") # test with He
compare_origins("She") #test with She

#12. We need one more tweak: to really compare different cultures,
#we need to account for the fact that the total number of movies is not the same.
#Write another, better function that calculates a percentage rather than a count.
#Hint: note that df.groupby(["Origin"])[word].count() will get you the number of movies, grouped by origin.
#Also sort the result so that the percentage is descending.
#Finally, make it user-friendly: print the word and what the numbers mean
    
#You're done! Try out your function and paste your most interesting result
#as a comment

