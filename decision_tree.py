from sklearn.tree import DecisionTreeClassifier

features = [[150,0],[154,0],[155,0],[158,0],[160,1],[163,1],[165,1],[167,1],[162,1]]
labels = ['Apple','Apple','Apple','Apple','Orange','Orange','Orange','Orange','Orange']

clf = DecisionTreeClassifier()
clf.fit(features,labels)

num1=input("enter the size: ")
num2=input("enter the colour : ")
print(clf.predict([[num1,num2]]))

