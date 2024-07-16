r1=['roll no.','name','grade','div','mobile no.']
r=[['1','Arya Patil','XII','A','9865477321'],
   ['5','Smita Nayak','XI','C','9873326547'],
   ['7','Roshni Singh','XII','E','8755612973'],
   ['12','Mansi T.','X','D','7798651112'],
   ['18','Fehmida Khan','XI','B','8765443218']]
import csv
file=open(r'student.csv','w')
file1=csv.writer(file)
file1.writerow(r1)
file1.writerows(r)
file.close()


