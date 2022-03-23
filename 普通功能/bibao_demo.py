
#闭包函数，函数可以被引用，被赋值给变量
def output_grade(grade):
    def output_student(name,gender):
        print(f'霍格沃兹开学了，学生姓名为：{name}， 性别为：{gender}， 年级为：{grade}')
    return output_student


stu_info = output_grade(1)
stu_info('Tom','female')
stu_info('Jelly','female')
