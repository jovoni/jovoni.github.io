import pandas as pd
import os
import sys

def write_item(titolo, autore, link, is_special):
    if not is_special:
        res = f'<div class="item"> <a href="{link}">{titolo}</a> <span>di {autore}</span> </div>'
    else: 
        res = f'<div class="item"> <div class="special"> <a href="{link}">{titolo}</a> <span>di {autore}</span> </div> </div>'    
    return res

if __name__ == "__main__":
    
    csv_names = ["album.csv", "visioni.csv", "letture.csv", "serietv.csv", "singoli.csv"]
    txt_names = ["album.txt", "visioni.txt", "letture.txt", "serietv.txt", "singoli.txt"]
    
    
    for j, csv in enumerate(csv_names):
        df = pd.read_csv(csv)
        print(csv)
        file_name = txt_names[j]
        
        with open(file_name, "w") as f:
            print(file_name)
            
            for i in range(len(df)):
            
                titolo = (df["titolo"][i])
                autore = (df["autore"][i])
                link = (df["link"][i])
                is_special = (df["special"][i])
                
                line = write_item(titolo,autore,link,is_special)
                f.write(line)
                f.write("\n")
            
        
        
    
    # csv = sys.argv[1]
    # file_name = sys.argv[2]
    
    # df = pd.read_csv(csv)
    
    # with open(file_name, "w") as f:
    #     for i in range(len(df)):
    #         print(i)
    #         titolo = (df["titolo"][i])
    #         autore = (df["autore"][i])
    #         link = (df["link"][i])
    #         is_special = (df["special"][i])
            
    #         line = write_item(titolo,autore,link,is_special)
    #         f.write(line)
    #         f.write("\n")
        
        