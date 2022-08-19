texto = '''the python software foundation and the global python 
community welcome and encourage participation by everyone our community is based on 
mutual respect tolerance and encouragement and we are working to help each other live up 
to these principles we want our community to be more diverse whoever you are and 
whatever your background we welcome you'''.split()
print (len(texto))
pp = []
for p in texto:
    if p[0:-1] in 'phyton' and len (p) > 4:
        pp.append (p)
print (pp)
        
