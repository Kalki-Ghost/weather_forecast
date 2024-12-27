# fuction of without argument ant return type
var1=function(){
  print("Hello")
}

# function of with argument and without return type
var2=function(a,b) print(a*b)

# function of without argument and with return type
var3=function() {
  return(10*20)
}

# function of with argument and with return type
var4=function(a,b){
  return(a*b)
}

# function with default arguments
var5=function(a=5,b=6) return(a*b)

#function with multiple argument
var6=function(a,...) {
  args=list(...)
  return(a+sum(unlist(args)))
}


var1()
var2(10,20)
print(var3())
print(var4(10,20))
print(var5(4))
print(var5(b=5))
print(var6(1,10,20,30))
