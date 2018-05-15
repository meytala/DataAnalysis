import numpy as np

##arreys of zeros shaped 2, 3, 4
np_zeros = np.zeros([2,3,4])
print ("np_zeros", np_zeros)

##arreys of ones shaped 2, 3, 4
np_ones = np.ones([2,3,4])
print ("np_onez", np_ones)

###arrey range from 0 to 999
np_1000 = np.arange(0, 1000)
print("np_1000", np_1000)

##2d arrey from given arrey

a = np.array([[1, 2.1, 3.2], [4, 5.4, 6.5]])
print("np a array", a)

###arrey of zros in the same shape as a
zero_a = np.zeros_like(a)
print("zeros as a", zero_a)


###arrey of ones in the same shape as a
ones_a = np.ones_like(a)
print("onze as a", ones_a)

###5x5 of zeros and one in diagnoal
diagnoal = np.identity(5)
print("diagnoal", diagnoal)

###diagnoal in the third

diagonal_third = np.eye(5, k=2)
print("diagonal third", diagonal_third)

#create an arrey from the list [2,3.4, 5.5, -6.4, -2.2, 2.4]
a= np.array([2,3.4, 5.5, -6.4, -2.2, 2.4])
print("new a", a)
print("a at index 1", a[1])
print("a at index 1 to 4", a[1:4])

##is 10 in a?
print("is 10 in a? ", 10 in a)

##create a 2d arrey
b = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],
              [1, 22, 4, 0.1, 5.3, -9],
              [3, 1, 2.1, 21, 1.1, -2]])

print("b ", b)

print("b at index 3", b[:,3]) #-6.4, 0.1, 21
print("b at index 1 to 4 and 0:4", b[1:4,0:4])##[1, 22, 4, 0.1], [3, 1, 2.1, 21]
print("b[1:,2]", b[1:,2]) #[ 4],[ 2.1]


#################excersize 2

##create a 2d array shape 2, 4 containing two lists: range(4), range(10,14)
##arr_test =np.array([[np.arange(4)],[np.arange(10,14)]]) #####################somthing does not work in here
##print("arr test:", arr_test)

##arr =np.array([range(4),range(10,14)]) #####################somthing does not work in here
arr1 = np.array([[0, 1, 2, 3], [10, 11, 12, 13]], float)
print("arr1", arr1)

print("arr1", arr1)
print("arr1 shape", arr1.shape)
print("arr1 size", arr1.size)
print("arr1 max", np.max(arr1))
print("arr1 min", np.min(arr1))


reshaped_arr1 = arr1.reshape(2,2,2)
print("reshaped array:", reshaped_arr1)

transposed = arr1.transpose()
print("transposed:", transposed)

###print the array flatten to a single dimention
single_dimention = arr1.flatten()
print("single dimention:", single_dimention)

###convert to float
reshaped = arr1.astype(float)
print("reshaped:", reshaped)


###create a 2d array shape (2, 4) containing 2 lists
arr2 = np.array([[0, 3.1, 2.2, 1.1], [7, 4, 3.14, 11]], float)
print("arr2:", arr2)

###concatenate
arr_concatenate = np.concatenate((arr1, arr2))
print("concatenate arr1 and arr2", arr_concatenate)

###expend_dim
expand = np.expand_dims(arr1, axis=2)
print("expand", expand)


###################################
#####excersize 1.3
###################################


a = np.array([[0,1,2,3], [10,11,12,13]])
print("a", a)
b = np.array([2, -1, 1, 0])
print("b", b)
print("multiple", a *b)
b1 = b*100
print("b1 = b*100: ", b1)
print("b1 type: ", type(b1))
b2 = b*100.0
print("b2: ", b2)
print("b2 type: ", type(b2))
print("b1==b2: ", b1==b2)


######print sum, mean product in 2 different ways
print("sum ", a.sum())
print("sum ", np.sum(a))

print("mean ", a.mean())
print("mean ", np.mean(a))

print("prod ", a.prod())
print("prod ", np.prod(a))

print("variance ", a.var())
print("variance ", np.var(a))

print("std ", a.std())
print("std ", np.std(a))

print("max in axis 0 ", a.max(axis=0))
print("max in axis 1 ", a.max(axis=1))



#####1.3   3
arr = np.arange(10)
print(arr)

greater_than_3 = arr<3
print("less than 3 ", greater_than_3)
greater_than_3_1 = np.where(arr<3)
print("greater than 3_1 ", greater_than_3_1)
greater_than_3_2 = np.less(arr,3)
print("greater than 3_2 ", greater_than_3_2)


less_3_more_8 = np.logical_or(arr<3, arr>8)
print("less_3_more_8 ", less_3_more_8)

condition = np.where(arr<3, arr*5, arr*-5 )
print("condition ", condition)



#####1.3   4
print ("a greater than 1 ", a> 1)
print("a greater than 3 smaller than 11 ", np.logical_and(a>3, a<11))
b=np.arange(6)
print("b ", b)
##new_b = b.put(0, 6)###########not working
##new_b = np.put(b, [0], 6, mode="clip") ##############not working
##print(new_b)

b.put(0, 6)
print("b put1 ", b)

c=np.arange(5)
print("c:", c)
###new_b = b.put(0, c[-1],mode="raise") not working
b.put(0, c[-1])
print("b put2 ", b)


#####1.3   5

a= np.array([2, -1, 1, 0])
b=np.array([0, 3, 2, 1])

print("dot: ", np.dot(a,b))

c = np.array([[[1,2,3], [10,11,12], [1,2,1]]])
##print("c", c.lingalg.det(c))   #######################could not find lingalg
print("c ", c)


##############1.3  6
print("roots ", np.roots([1, 2, 10, 18, 9]))
print("coeeficients ", np.poly([1, -1, 3, -3]))
print("value of a polynom ", np.polyval([3, 5, -16, -12], 2))

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,5,6,8,9,11,13,15,17,19])

print("fit ", np.polyfit(x, y, 2)) ######@#did not work - expected tto have similar length added 19




########exc. 2 part 4

a = np.array([[0,1,2,3], [10,11,12,13]])
print("median of a: ", np.median(a))
print ("correlation coeefician: ", np.corrcoef(a))
print("random array: ", np.random.rand(2,4))
print("random_ between 2 and 10: ", np.random.randint(5, 10))
b = np.random.normal(size=40)
print("a sample of 40 from normal distribution as b: ", b)
new_b=np.array(b)
print("new b", new_b)
print("suffled b: ", np.random.shuffle(new_b)) #####################not working




##########final exercise



