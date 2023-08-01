class Point:
    def __init__(point, x=None, y=None):#初始化方法:param x: 横坐标:param y: 纵坐标
        if x==None and y==None:
            point.x=0
            point.y=0
        elif x==None or y==None:
            raise PointError("Cannot create point.")
        else:
            point.x = x
            point.y = y
class PointError(Exception):
    def __init__(self, error):
        self.error = error
#     def __str__(self):
#         return self.error
#     print("PointError: Cannot create point.")
# Will be tested only when passing no, one or two arguments,
# that have to be named; moreover, when an argument is passed,
# it will be a Point object.
class NonVerticalLine():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    def __init__(line,**kwargs):#kwargs字典
        if "point_1" not in kwargs and "point_2" not in kwargs:#就没有
            raise NonVerticalLineError("Cannot create nonvertical line.")
        if "point_1"==None and "point_2"==None:#俩都没有
            point_1=Point(0,0)
            point_2=Point(0,0)
        if "point_1"not in kwargs:#没给1
            point_1=Point(0,0)
            line.point_1=point_1
        if "point_2"not in kwargs:#没给2
            point_2=Point(0,0)
            line.point_2=point_2
        if "point_1" in kwargs:
            point_1=kwargs.get("point_1")
            line.point_1=point_1
        if "point_2" in kwargs:
            point_2=kwargs.get("point_2")
            line.point_2=point_2
        if "point_1" in kwargs and "point_2" in kwargs:
            if line.point_1.x==line.point_2.x:#垂直线
                raise NonVerticalLineError("Cannot create nonvertical line.")
        line.slope=((line.point_2.y-line.point_1.y) /(line.point_2.x-line.point_1.x))
        line.intercept=line.point_1.y-line.slope*line.point_1.x
#     def change_point_or_points(line,point_1=None,point_2=None):
#         print(line.point_1.x,line.point_2.x)
#         if line.point_1 is not None and line.point_2 is not None:
#             line.point_1=point_1
#             line.point_2=point_2
#             if point_1.x==point_2.x:
#                 raise NonVerticalLineError("Cannot perform this change.")
    def change_point_or_points(line,**kwargs):
        if "point_1" in kwargs and "point_2"in kwargs:
            point_1=kwargs.get("point_1")
            line.point_1=point_1
            point_2=kwargs.get("point_2")
            line.point_2=point_2
        if "point_1"in kwargs:
            point_1=kwargs.get("point_1")
            line.point_1=point_1
        if "point_2"in kwargs:
            point_2=kwargs.get("point_2")
            line.point_2=point_2
        if line.point_1.x==line.point_2.x:
            raise NonVerticalLineError("Cannot perform this change.")
        line.slope=((line.point_2.y-line.point_1.y) /(line.point_2.x-line.point_1.x))
        line.intercept=line.point_1.y-line.slope*line.point_1.x
class NonVerticalLineError(Exception):
    def __init__(self,error):
        self.error=error
# pt = Point()
# pt.x, pt.y
# Point(0)
# pt = Point(0, 0)
# pt.x, pt.y
# pt = Point(2, 4.6)
# pt.x, pt.y
# NonVerticalLine() 
# NonVerticalLine(pt)
# line = NonVerticalLine(point_1=pt)
# line.point_1.x, line.point_1.y, line.point_2.x, line.point_2.y
# line = NonVerticalLine(point_2=pt)
# line.point_1.x, line.point_1.y, line.point_2.x, line.point_2.y
# NonVerticalLine(point_1=pt, point_2=pt)
# p1 = Point(1, 2)
# p2 = Point(4, 4)
# p4 = Point(6,2)
# line = NonVerticalLine(point_1=p1, point_2=p2)
# line.slope
# line.intercept
# p3 = Point(1,5)
# NonVerticalLine(point_1=p1, point_2=p3)
# line = NonVerticalLine(point_1=p1, point_2=p2)
# line.change_point_or_points()
# line.slope
# line.intercept
# line.change_point_or_points(point_2=p1)
# line.slope
# line.change_point_or_points(point_2=p3)
# line.slope
# line.change_point_or_points(point_2=p4)
# print(line.slope)
# line.intercept
# p5 = Point(3,1)
# line.change_point_or_points(point_1=p5)
# line.slope
# line.intercept
# line.change_point_or_points(point_1=p4)
# line.slope
# line.change_point_or_points(point_1=p2, point_2=p1)
# line.slope
# line.intercept
