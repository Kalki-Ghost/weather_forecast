index<-as.numeric(readline(prompt="Enter the index:"))

var=switch(index,"arun","venkatesh","Ranjitha")
print(var)

var=switch("Null","Venkatesh"=as.Date("2004-05-15"),"Arun"=as.Date("2003-12-13"),as.Date("2000-01-01"))
print(var)

