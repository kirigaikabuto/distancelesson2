# #
# school
#     grade
#         student
#             first_name
#             last_name
#             marks-[5 3 6 7]
# arr[0][0][0]->"yerassyl"
# arr[0][0][2]->[5,3,4,5],
arr=[
        [
            [
                "yerasyl",
                "tleugazy",
                [1,2,3,4],
            ],
            [
                "yerasyl",
                "tleugazy",
                [1,2,3,4]
            ],
            [
                "yerasyl",
                "tleugazy",
                [1,2,3,4]
            ]
        ],
        [
        [
                "yerasyl",
                "tleugazy",
                [5,3,4,5],
            ],
            [
                "yerasyl",
                "tleugazy",
                [5,3,4,5]
            ],
            [
                "yerasyl",
                "tleugazy",
                [5,3,4,5]
            ]
        ],
]
for grade in arr:
    sumi_avg=0
    for student in grade:
        marks=student[2]
        n = len(marks)
        sumi=0
        for mark in marks:
            sumi=sumi+mark
        sumi_avg=sumi_avg+sumi/n
    print(sumi_avg)
# len(arr)->количество классов
# len(arr[0])->количество учеников в первом классе
# len(arr[0][0])->количество данных у первого ученика первого класса