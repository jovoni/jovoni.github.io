import pandas as pd
import os
import sys

def write_book(titolo, autore, link, is_special):
    if not is_special:
        res = f'<div class="item"> <a href="{link}">{titolo}</a> <span>di {autore}</span> </div>'
    else: 
        res = f'<div class="item"> <div class="special"> <a href="{link}">{titolo}</a> <span>di {autore}</span> </div> </div>'    
    return res

if __name__ == "__main__":
    
    df = pd.read_csv("letture.csv")
    
    with open("books.txt", "w") as f:
        for i in range(len(df)):
            print(i)
            titolo = (df["titolo"][i])
            autore = (df["autore"][i])
            link = (df["link"][i])
            is_special = (df["special"][i])
            
            line = write_book(titolo,autore,link,is_special)
            f.write(line)
            f.write("\n")
        
        