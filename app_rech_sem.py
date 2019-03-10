import tkinter as tk
import os
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import numpy as np

class interf:
      
    def __init__(self) :
        self.fenetre = tk.Tk()
        self.fenetre.title("Devoir indexation semantique")
        self.makeWidgets()

    def lecture(self):
        self.b_r.configure(state="disabled")
        input = self.e_chemin.get("1.0",'end-1c')
        self.b_tok.configure(state="normal")
        for element in os.listdir(input):
            input = self.e_chemin.get("1.0",'end-1c')
            if element.endswith('.txt'):
                input=input+"\\"+element
              
                self.b_tok.configure(state="normal")
                self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
                self.l_text_contenu.insert(tk.END, input+"\n")
                fichier = open(str(input),"r")
                for ligne in fichier:
                   
                    self.l_text_contenu.insert(tk.END, ligne)
                fichier.close()
                self.l_text_contenu.insert(tk.END, "\n")
                self.l_text_contenu.insert(tk.END, "\n")
        self.l_text_contenu.configure(state="disabled",font=("Helvetica", 8))
        
        
    def tokens(self):
        fich={}
        input = self.e_chemin.get("1.0",'end-1c')
        self.b_tok.configure(state="normal")
        for element in os.listdir(input):
            txt=""
            input = self.e_chemin.get("1.0",'end-1c')
            if element.endswith('.txt'):
                input=input+"\\"+element
         
                self.b_tokn.configure(state="normal")
                self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
                fichier = open(str(input),"r")
                for ligne in fichier:
                    txt=txt+ligne
                fichier.close()
                word_tokens = word_tokenize(txt)
                
                filtered_sentence = [] 
                for w in word_tokens:
                    filtered_sentence.append(w)
                fich[str(element)]=filtered_sentence
        return fich
    
    def affich_tokens(self):
        self.b_r.configure(state="disabled")
        self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
        self.l_text_contenu.delete(1.0, tk.END)
        x=self.tokens()
        for cle,valeur in x.items():
            self.l_text_contenu.insert(tk.END, cle+":\n")
            for word in valeur:
                self.l_text_contenu.insert(tk.END, word+"\n")
        self.l_text_contenu.configure(state="disabled",font=("Helvetica", 8))    
            
    def tokenn(self):
        self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
        stop_words = set(stopwords.words('english'))
        stop_words.add('us')
        x=self.tokens()
        fich1={}
        for cle,valeur in x.items():
            t=[]
            aux=[word.lower() for word in valeur if word.isalpha()]
            for w in aux:
                if w not in stop_words:
                    t.append(w)
            fich1[cle]=t
        return fich1
    
    def affich_tokenn(self):
        self.b_r.configure(state="disabled")
        self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
        self.l_text_contenu.delete(1.0, tk.END)
        x=self.tokenn()
        self.b_oc.configure(state="normal")
        for cle,valeur in x.items():
            self.l_text_contenu.insert(tk.END, cle+":\n")
            for word in valeur:
                self.l_text_contenu.insert(tk.END, word+"\n")
        self.l_text_contenu.configure(state="disabled",font=("Helvetica", 8))
        
    def occurence(self):
        fich3={}
       
        x=self.tokenn()
        for cle,val in x.items():
            t=[]
            for word in val:
                wn={}
                n=val.count(word)
                wn[word]=n
                if wn not in t:
                    t.append(wn)
            fich3[cle]=t
       
        return fich3
    
    def affiche_occurence(self):
        self.lema.configure(state="normal")
        self.b_r.configure(state="disabled")
        self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
        self.l_text_contenu.delete(1.0, tk.END)
        x=self.occurence()
        for cle,val in x.items():
            self.l_text_contenu.insert(tk.END, cle+":\n")
            for wn in val:
                for c,v in wn.items():
                    self.l_text_contenu.insert(tk.END, c+"-->"+str(v)+"\n")
        self.l_text_contenu.configure(state="disabled",font=("Helvetica", 8))
        
    def lemma(self,p):
        verb=["VB","VBD","VBG","VBN","VBP","VBZ"]
        noun=["NN","NNS","NNP","NNPS"]
        adj=["JJ","JJS","JJR"]
        adv=["RB", "RBR", "RBS", "RP"]
        lemmatizer = WordNetLemmatizer()
        result = nltk.pos_tag([p])
        v=[x[1] for x in result][0]
        
        if v in verb:
            return lemmatizer.lemmatize(p, pos="v")
        if v in noun:
            return lemmatizer.lemmatize(p, pos="n")
        if v in adj:
            return lemmatizer.lemmatize(p, pos="a")
        if v in adv:
            return lemmatizer.lemmatize(p, pos="r")
    
    def lemmatization(self):
        fich4={}
        x=self.occurence()
        for cle,val in x.items():
            t=[]
            for w in val:
                
                for c,v in w.items():
                    l={}
                    nw=self.lemma(c)
                    l[nw]=v
                    t.append(l)
                    
            fich4[cle]=t
        return fich4
            
    def affich_lemmatization(self):
        self.synset.configure(state="normal")
        self.b_r.configure(state="disabled")
        self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
        self.l_text_contenu.delete(1.0, tk.END)
        x=self.lemmatization()
        for cle,val in x.items():
            self.l_text_contenu.insert(tk.END, cle+":\n")
            for wn in val:
                for c,v in wn.items():
                    self.l_text_contenu.insert(tk.END, str(c)+"\n")
        self.l_text_contenu.configure(state="disabled",font=("Helvetica", 8))
            
            
    def synsetz(self):
        fichs={}
        x=self.lemmatization()
        for cle,valeur in x.items():
            t=[]
            for wn in valeur:
                for c,v in wn.items():
                    synonym=[]
                    
                    for syn in wordnet.synsets(c):
                        for l in syn.lemmas():
                            synonym.append(l.name())
                    if(len(synonym)!=0):
                        wns={}
                        wns[c]=[v,synonym[0]]
                        t.append(wns)
                    else:
                        wns={}
                        wns[c]=[v,c]
                        t.append(wns)
                        
            fichs[cle]=t
        
        return fichs
    
    def affich_synset(self):
        
        self.b_r.configure(state="normal")
        self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
        self.l_text_contenu.delete(1.0, tk.END)
        x=self.synsetz()
        for cle,valeur in x.items():
            self.l_text_contenu.insert(tk.END, cle+":\n")
            for wns in valeur:
                for c,v in wns.items():
                    self.l_text_contenu.insert(tk.END, c+"---"+v[1]+"\n")
        self.l_text_contenu.configure(state="disabled",font=("Helvetica", 8))
    
    def recherche(self):
        fichf={}
        mot= self.e_cherch.get("1.0",'end-1c')
        mot=self.lemma(mot)
        
        synonyms = []
        for syn in wordnet.synsets(mot):
            for l in syn.lemmas():
                synonyms.append(l.name())
        x=self.synsetz()
        y=np.unique(synonyms)
        for cle,valeur in x.items():
            
            tab=[]
            for wn in valeur:
                for c,v in wn.items():                
                    for t in range(len(y)):
                        if v[1]==y[t]:
                            tab.append(v[0])
                            tab.append(c)
                            tab.append(y[t])
                    fichf[cle]=tab
                    
        
        new=[]
        for cle,valeur in fichf.items():
            new.append([cle,valeur])
        for i in range(len(new)):
            if(len(new[i][1])!=0):
                
                for j in range(len(new)-1):
                    if(len(new[j+1][1])!=0):
                        
                        if(new[i][1][0]>new[j+1][1][0]):
                            
                            A=new[i]
                            new[i]=new[j]
                            new[j]=A
                                
        self.l_text_contenu.configure(state="normal",font=("Helvetica", 8))
        self.l_text_contenu.delete(1.0, tk.END)
        for i in range(len(new)):
            if(len(new[i][1])!=0):
                self.l_text_contenu.insert(tk.END, "requete :"+str(self.e_cherch.get("1.0",'end-1c')))
                break
        self.l_text_contenu.insert(tk.END, "\n \n")
        for i in range(len(new)):
            if(len(new[i][1])!=0):
                self.l_text_contenu.insert(tk.END, "le fichier :"+str(new[i][0])+"    contient :"+str(new[i][1][2])+"\n")
        self.l_text_contenu.configure(state="disabled",font=("Helvetica", 8))
            
                    
                
           
                
                
                
       
        
                            
                

        
    def makeWidgets(self):
        self.fenetre.geometry('1000x650+100+10')
        self.l_chemin = tk.Label(self.fenetre, text="chemin fichier :",font=("Helvetica", 12))
        self.e_chemin = tk.Text(self.fenetre, width="30",height=1)
        
        self.l_cherch = tk.Label(self.fenetre, text="chercher mot :",font=("Helvetica", 12))
        self.e_cherch = tk.Text(self.fenetre, width="30",height=1,state="normal")
        
        self.b = tk.Button(self.fenetre, text="valider",height=1, width=10,command=self.lecture)
        self.b_r = tk.Button(self.fenetre, text="recherche",height=1, width=10,state="disabled", command=self.recherche)
        self.b_tok = tk.Button(self.fenetre, text="tokens",height=1, width=10,command=self.affich_tokens,state='disabled')
        self.b_tokn = tk.Button(self.fenetre, text="tokens\nnettoyé",height=1,command=self.affich_tokenn, width=10,state='disabled')
        self.b_oc = tk.Button(self.fenetre, text="occurence",height=1,command=self.affiche_occurence, width=10,state='disabled')
        self.lema = tk.Button(self.fenetre, text="lemmatisation",height=1,command=self.affich_lemmatization, width=10,state='disabled')
        self.synset = tk.Button(self.fenetre, text="synset",height=1,command=self.affich_synset, width=10,state='disabled')
                        
        txt_frm = tk.Frame(self.fenetre, width=700, height=700)
        txt_frm.place(x=170,y=200)           
        self.l_text_contenu = tk.Text(txt_frm,width=120,height=30,font=("Helvetica", 8),state='disabled')
        self.l_text_contenu.grid(row=0, column=0, padx=0, pady=0)
        scrollb = tk.Scrollbar(txt_frm, command=self.l_text_contenu.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.l_text_contenu['yscrollcommand'] = scrollb.set
        
        
        self.l_chemin.place(x=250,y=70)
        self.e_chemin.place(x=380,y=72)
        
        self.l_cherch.place(x=250,y=100)
        self.e_cherch.place(x=380,y=102)
        
        self.b.place(x=650,y=69)
        self.b_r.place(x=650,y=99)
        
        self.b_tok.place(x=40,y=300)
        self.b_tokn.place(x=40,y=340)
        self.b_oc.place(x=40,y=380)
        self.lema.place(x=40,y=420)
        self.synset.place(x=40,y=460)
        
    
        
       
   
        
b = interf()

b.fenetre.mainloop()