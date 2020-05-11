from myutils import *
persons=[
    {
    "name":"yerassyl1",
    "year":1998
    },
    { 
    "name":"yerassyl2",
    "year":1997
    },
    { 
    "name":"yerassyl3",
    "year":1999
    },
]
for i in persons:
    realage =  getAge(i)
    print(realage)