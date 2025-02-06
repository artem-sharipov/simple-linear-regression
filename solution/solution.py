# Part №1 - read the data from the source file, convert it, and fill in the coordinate lists. 
myfile=open('data/data023.txt','r')
x_list = []
y_list = []
N = 0   # Number of points
i = 0   # The loop variable
for u in myfile:
    p = u.split()
    if p[0] == '(*':    # If the string starts with "(*", it is skipped,
        continue        # the cycle continues
    else:
        r = u.split('***')    # Divide the data rows by "***"
        r[0] = r[0].split()    # Divide the parts of the lines with coordinates by spaces
        r[1] = r[1].split()
        xnf_list = r[0][2].split(']')   # Separation of the abscissa of the row list
        ynf_list = r[1][2].split(']')   # Separating the ordinates of the row list
        x_list.append(float(xnf_list[0]))   # Filling in the abscess list
        y_list.append(float(ynf_list[0]))   # Filling out the list of ordinates
        Nni_list = r[0][0].split('(')   # Converting a list to highlight the number of points
        Nni_list = Nni_list[1].split(')')
        N = int(Nni_list[0])
myfile.close()
############################################
# Part #2 - based on the data obtained in part #1, we create a new .csv file for reading in Mathcad
mathfile = open('data/mathdata.csv','w')
for i in range(N):
    u=str(x_list[i]) + ';' + str(y_list[i]) +'\n'
    mathfile.write(u)
mathfile.close()
############################################
# Part #3 - performing calculations of linear regression coefficients
i=0     # The loop variable
sumX = 0    # The sum of the abscissas
sumY = 0    # The sum of ordinates
sumXY = 0   # The sum of the product of the abscissa and ordinate
sumXX = 0   # The sum of the squares of the abscissa
a = 0   # The slope coefficient of the linear regression function
b = 0   # Coefficient is a free term of a linear regression function
sumX = sum(x_list)
sumY = sum(y_list)
for i in range(N):
    sumXY += x_list[i]*y_list[i]
    sumXX += x_list[i]**2
a = ((sumX*sumY-N*sumXY)/(sumX**2-N*sumXX))
b = ((sumY-a*sumX)/N)
print('a =',a,'\nb =',b)    #Output the coefficients to the console
############################################
# Part #4 - Graph construction in python and its displa
from matplotlib import pyplot as plt
lin=[a*x+b for x in x_list]
plt.plot(x_list,y_list,'g*')
plt.plot(x_list,lin)
plt.grid()
plt.show()
