from copy import copy, deepcopy
import linecache
from collections import defaultdict
from itertools import combinations

class DiffCommands:
    def __init__(self, file_name=None):
        self.file_name = file_name
        self.file_lines=[]
        self.error_output = "Cannot possibly be the commands for the diff of two files"
        if file_name!=None:
            DiffCommands.CheckOrder(self, file_name)  # 检查是不是正确的命令
    def __str__(self):  # 班门弄斧只为返回值
        if self.file_name:
            file = open(self.file_name)
            file_content = file.read()
            return file_content[:-1]
        else:
            return ""
    def CheckOrder(self, file_name):
        for self.count, line in enumerate(open(file_name)):
            pass
        self.count += 1  # 文件行数
        #         print(self.count)
        with open(file_name)as open_file:
            for line in open_file:
                line = line.replace("\n", "")
                if " " in line:  # 有空格
                    raise DiffCommandsError(self.error_output)
                if line == "":  # 有空行
                    raise DiffCommandsError(self.error_output)
                if "d" in line:
                    DiffCommands.delete_order(self, line)
                elif "a" in line:
                    DiffCommands.add_order(self, line)
                elif "c" in line:
                    DiffCommands.change_order(self, line)
                else:  # 谁知道啥情况，没命令就算错
                    raise DiffCommandsError(self.error_output)

    def delete_order(self, line):
        if self.count <= 0:
            raise DiffCommandsError(self.error_output)
        left, right = line.split("d")
        left_file = []
        right_file = []
        if left == "" or right == "":
            raise DiffCommandsError(self.error_output)
        if "," in left:
            left_file = line.split(",")
        else:
            left_file.append(left)
        if "," in right:
            right_file = line.split(",")
        else:
            right_file.append(right)
        if len(right_file) > 1:
            raise DiffCommandsError(self.error_output)
        self.count = self.count - len(left_file)
        if self.count < 0:
            raise DiffCommandsError(self.error_output)
    def add_order(self, line):
        if self.count <= 0:
            raise DiffCommandsError(self.error_output)
        left, right = line.split("a")
        if left == "" or right == "":
            raise DiffCommandsError(self.error_output)
    def change_order(self, line):
        if self.count <= 0:
            raise DiffCommandsError(self.error_output)
        left, right = line.split("c")
        if left == "" or right == "":
            raise DiffCommandsError(self.error_output)
class DiffCommandsError(Exception):
    def __init__(self, error):
        self.error = error
class OriginalNewFiles:
    def __init__(self, file_1, file_2):
        self.file1 = []
        self.file2 = []
        with open(file_1) as open_file_1:
            for line in open_file_1:
                line = line.replace("\n", "")
                self.file1.append(line)
        with open(file_2) as open_file_2:
            for line in open_file_2:
                line = line.replace("\n", "")
                self.file2.append(line)
    def is_a_possible_diff(self, order):
        try:
            file1 = copy(self.file1)
            file2 = copy(self.file2)
            left_line = []
            right_line = []
            command = str(order)
            command_file = command.split("\n")
            #         print(command_file)
            for i in range(len(command_file)):
                # print(command_file[i])
                if "d" in command_file[i]:
                    left_line = []
                    right_line = []
                    left, right = command_file[i].split("d")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    #                 if int(right)>len(left_line):
                    #                     return False
                    left_line = [int(x) for x in left_line]
                    #                 if max(left_line)>len(file1):
                    #                     return False
                    for j in range(len(left_line)):
                        file1[left_line[j] - 1] = "(//▽//)"
                #                 print(left,right)
                #             for line in file1:
                #                 print(line)
                if "a" in command_file[i]:
                    left_line = []
                    right_line = []
                    left, right = command_file[i].split("a")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    if "," in right:
                        right_line = right.split(",")
                    else:
                        right_line.append(right)
                    left_line = [int(x) for x in left_line]
                    right_line = [int(x) for x in right_line]
                    if len(right_line) == 1:
                        if left_line[0] == 0 and len(left_line) == 1:
                            for j in range(len(right_line)):
                                file2[right_line[j] - 1] = "(//▽//)"
                        else:
                            file2[right_line[0] - 1] = file1[left_line[0] - 1]
                            file2[right_line[0] - 2] = "(//▽//)"
                    if len(right_line) == 2:
                        if left_line[0] == 0 and len(left_line) == 1:
                            for j in range(len(right_line)):
                                file2[right_line[j] - 1] = "(//▽//)"
                        else:
                            file2[right_line[0] - 1] = file1[left_line[0] - 1]
                            file2[right_line[0] - 2] = "(//▽//)"
                            file2[right_line[1] - 1] = "(//▽//)"
                if "c" in command_file[i]:
                    left_line = []
                    right_line = []
                    left, right = command_file[i].split("c")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    if "," in right:
                        right_line = right.split(",")
                    else:
                        right_line.append(right)
                    left_line = [int(x) for x in left_line]
                    right_line = [int(x) for x in right_line]
                    if len(right_line) == 1:
                        del file2[right_line[0] - 1]
                    else:
                        # print(file2[right_line[0] - 1:right_line[1]])
                        del file2[right_line[0] - 1:right_line[1]]
                    if len(left_line) == 1:
                        file2.insert(right_line[0] - 1, file1[left_line[0] - 1])
                    else:
                        if i > len(file1):
                            return False
                        else:
                            for j in range(left_line[1] - 1, left_line[0] - 2, -1):
                                # print(j)
                                file2.insert(right_line[0] - 1, file1[j])
            for i in range(len(file1) - 1, -1, -1):
                if file1[i] == "(//▽//)":
                    del file1[i]
            for i in range(len(file2) - 1, -1, -1):
                if file2[i] == "(//▽//)":
                    del file2[i]
            if file1 == file2:
                return True
            else:
                return False
        except:
            return False
    def output_diff(self, order):
        if OriginalNewFiles.is_a_possible_diff(self, order):
            file1 = copy(self.file1)
            file2 = copy(self.file2)
            command = str(order)
            command_file = command.split("\n")
            for line in command_file:
                print(line)
                if "d" in line:
                    left_line = []
                    right_line = []
                    left, right = line.split("d")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    left_line = [int(x) for x in left_line]
                    for j in range(len(left_line)):
                        print("< " + file1[left_line[j] - 1])
                if "a" in line:
                    left_line = []
                    right_line = []
                    left, right = line.split("a")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    if "," in right:
                        right_line = right.split(",")
                    else:
                        right_line.append(right)
                    left_line = [int(x) for x in left_line]
                    right_line = [int(x) for x in right_line]
                    if len(right_line) == 1:
                        print("> " + file2[right_line[0] - 1])
                    if len(right_line) == 2:
                        print("> " + file2[right_line[0] - 1])
                        print("> " + file2[right_line[1] - 1])
                if "c" in line:
                    left_line = []
                    right_line = []
                    left, right = line.split("c")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    if "," in right:
                        right_line = right.split(",")
                    else:
                        right_line.append(right)
                    left_line = [int(x) for x in left_line]
                    right_line = [int(x) for x in right_line]

                    if len(left_line) == 1:
                        print("< " + file1[left_line[0] - 1])
                    else:
                        for i in range(left_line[0] - 1, left_line[1], 1):
                            print("< " + file1[i])
                    print("---")
                    if len(right_line) == 1:
                        print("> " + file2[right_line[0] - 1])
                    else:
                        for i in range(right_line[0] - 1, right_line[1]):
                            print("> " + file2[i])
    def output_unmodified_from_original(self,order):#左边的
        if OriginalNewFiles.is_a_possible_diff(self, order):
            file1 = copy(self.file1)
            command = str(order)
            command_file = command.split("\n")
            for line in command_file:
                if "d" in line:
                    left_line = []
                    right_line = []
                    left, right = line.split("d")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    left_line = [int(x) for x in left_line]
                    for j in range(len(left_line)):
                        file1[left_line[j] - 1]="..."
                if "c" in line:
                    left_line = []
                    right_line = []
                    left, right = line.split("c")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    left_line = [int(x) for x in left_line]
                    right_line = [int(x) for x in right_line]
                    if len(left_line) == 1:
                        file1[left_line[0] - 1]="..."
                    else:
                        for i in range(left_line[0] - 1, left_line[1], 1):
                            file1[i]="..."
            for q in range(len(file1)):
                if q-1>=0 and file1[q-1]=="..."and file1[q]=="...":
                    pass
                else:
                    print(file1[q])
    def output_unmodified_from_new(self,order):#右边的
         if OriginalNewFiles.is_a_possible_diff(self, order):
            file2 = copy(self.file2)
            command = str(order)
            command_file = command.split("\n")
            for line in command_file:
                if "a" in line:
                    left_line = []
                    right_line = []
                    left, right = line.split("a")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    if "," in right:
                        right_line = right.split(",")
                    else:
                        right_line.append(right)
                    left_line = [int(x) for x in left_line]
                    right_line = [int(x) for x in right_line]
                    if len(right_line) == 1:
                        file2[right_line[0] - 1]="..."
                    if len(right_line) == 2:
                        file2[right_line[0] - 1]="..."
                        file2[right_line[1] - 1]="..."
                if "c" in line:
                    left_line = []
                    right_line = []
                    left, right = line.split("c")
                    if "," in left:
                        left_line = left.split(",")
                    else:
                        left_line.append(left)
                    if "," in right:
                        right_line = right.split(",")
                    else:
                        right_line.append(right)
                    left_line = [int(x) for x in left_line]
                    right_line = [int(x) for x in right_line]
                    if len(right_line) == 1:
                        file2[right_line[0] - 1]="..."
                    else:
                        for i in range(right_line[0] - 1, right_line[1]):
                            file2[i]="..."
            for q in range(len(file2)):
                if q-1>=0 and file2[q-1]=="..."and file2[q]=="...":
                    pass
                else:
                    print(file2[q])
    def get_all_diff_commands(self):
        if self.file1 == self.file2:
            return [DiffCommands()]
        m = len(self.file1) + 1
        n = len(self.file2) + 1
        #存储路径
        emmmm = [[0 for _ in range(n)] for _ in range(m)]
        points = []
        #最短距离的算法
        for i in range(1,len(emmmm)):
            for j in range(1,len(emmmm[0])):
                left = self.file1[i-1]
                right = self.file2[j - 1]
                if left == right:
                    emmmm[i][j] = emmmm[i - 1][j - 1] + 1
                    points.append((i,j,emmmm[i][j]))
                else:
                    emmmm[i][j] = max(emmmm[i][j - 1], emmmm[i - 1][j])
        max_value = points[-1][-1]
        all_commands = combinations(points,max_value)
        result = []
        for commands in all_commands:
            first = commands[0]
            for second in commands[1:]:
                if second[0]<first[0] or second[1]<first[1] or second[2]<=first[2]:
                    break
                first = second
            else:
                result.append(commands)
        output=[]#返回的数组
        for method in result:
            diff = DiffCommands()#该死的类型
            diff_left = []
            diff_right = []
            for i in range(len(method)):
                diff_left.append(method[i][0])
                diff_right.append(method[i][1])
            diff_left.append(len(self.file1) + 1)
            diff_right.append(len(self.file2) + 1)
            left_first=0
            right_first=0
            #zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
            #如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
            for left_second, right_second in zip(diff_left, diff_right):
                #change的情况
                if left_second > left_first + 1 and right_second > right_first + 1:
                    left = self.get_format(left_first + 1, left_second - 1)
                    right = self.get_format(right_first + 1, right_second - 1)
                    line = left + 'c' + right
                    diff.file_lines.append(line)
                #删除
                elif left_second > left_first + 1 and right_second == right_first + 1:
                    left = self.get_format(left_first + 1, left_second - 1)
                    right = self.get_format(right_first, right_second - 1)
                    line = left + 'd' + right
                    diff.file_lines.append(line)
                #添加
                elif left_second == left_first + 1 and right_second > right_first + 1:
                    left = self.get_format(left_first, left_second - 1)
                    right = self.get_format(right_first + 1, right_second - 1)
                    line = left + 'a' + right
                    diff.file_lines.append(line)
                left_first, right_first = left_second, right_second
#             print(diff.file_lines)
#             output=[]
            tool=""
#             print(diff.file_lines)
            for i in range(len(diff.file_lines)):
                tool+=diff.file_lines[i]+"\n"
#             print(tool)
            output.append(tool[:-1])
#             diffs.append(diff)
        output = sorted(output)
#         print(output)
#         print(len(output),output)
        return output
    def get_format(self, first, second):
        if first == second:
            return f"{second}"
        else:
            return f"{first},{second}"
#         order=[]
#         emmmm=[]
#         count_1=0
#         count_2=0
#         line_num=0
#         comma_pos=0
#         order_pos=0
#         f = open(file_name, 'r', encoding='utf-8')
#         order=[item for item in f.read()]
#         for item in order:
#             if item.isupper():#有大写字母
#                 raise DiffCommandsError(self.error_output)
#             if item==" ":#有空格
#                 raise DiffCommandsError(self.error_output)
#         for i in range(len(order)):#有空行 右边数字大于2个
#             if i+1 <len(order) and order[i]=="\n" and order[i+1]=="\n":
#                 raise DiffCommandsError(self.error_output)
#             if order[i]=="d":#右边数字大于两个，待定
#                 count_1=i
#             if order[i]=="\n" and count_1!=0:
#                 count_2=i
#                 if "," in order[count_1:count_2]:
#                     raise DiffCommandsError(self.error_output)
#                 count_1=0
#                 count_2=0
#         for item in order:#获取文件行数
#             if item=="\n":
#                 line_num+=1
# #         file=open(file_name,'rb')
# #         line_read=f.readline(1)
#         for i in range(1,line_num+1):#逐行读取文件
#             line_read = linecache.getline(file_name, i)
#             print(line_read[:-1])
#             if "d" in line_read:#要删除的情况,待定
#                 for j in range(len(line_read)):
#                     if line_read[j]=="," and order_pos==0:
#                         comma_pos=j
#                     if line_read[j]=="d":
#                         order_pos=j    
#                 if comma_pos!=0:
#                     emmmm.append(int(line_read[0:comma_pos]))
#                     emmmm.append(int(line_read[comma_pos:order_pos].replace(",","")))
#                 else:
#                     emmmm.append(int(line_read[0:order_pos]))
#                 print(emmmm)
#                 if max(emmmm)>line_num:
#                     raise DiffCommandsError(self.error_output)
#                 if line_num<=len(emmmm) and i!=line_num:
#                     raise DiffCommandsError(self.error_output)
#             emmmm=[]
#             comma_pos=0
#             order_pos=0
# diff_1 = DiffCommands("diff_1.txt")
# pair_of_files = OriginalNewFiles("file_3_2.txt", "file_3_1.txt")
# print(pair_of_files.is_a_possible_diff(diff_1))
# diffs=pair_of_files.get_all_diff_commands();
# print(diffs[0])
