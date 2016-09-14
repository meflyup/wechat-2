#索引和分片（未对分片处理）

    class Indexer:

        def __getitem__(self, index):

            return index**2



#迭代器对象

*单迭代对象*



    # coding = utf-8
    class Squares:
       def __init__(self, start, stop):
           self.start = start - 1
           self.stop = stop
       def __iter__(self):
           return self
       def __next__(self):
           if self.start == self.stop:
               raise StopIteration
           self.start+=1
           return self.start **2
    for i in Squares(1, 5):
       print(i)

*多迭代对象（每次调用__iter__返回一个对象即可）*



    # coding = utf-8
    class SkipIterator:
       def __init__(self, wrapped):
           self.wrapped = wrapped
           self.offset = 0
       def __next__(self):
           if self.offset >= len(self.wrapped):
               raise StopIteration
           else:
               item = self.wrapped[self.offset]
               self.offset += 2
               return item
    class SkipObject:
       def __init__(self, wrapped):
           self.wrapped = wrapped
       def __iter__(self):
           return SkipIterator(self.wrapped)
    if __name__ == '__main__':
       alpha = 'abcdefg'
       skipper = SkipObject(alpha)
       I = iter(skipper)
       print(next(I), next(I), next(I))
       for x in skipper:
           for y in skipper:
               print(x + y, end = ' ')

#属性引用（当通过继承树搜索找不到属性时调用）



    # coding = utf-8
    class empty:
       def __getattr__(self, item):
           if item == 'age':
               return 40
           else:
               raise AttributeError
    x = empty()
    print(x.age)
    print(x.name)

#属性赋值



    # coding = utf-8
    class AccessControl:
       def __setattr__(self, key, value):
           if key == 'age':
               self.__dict__[key] = value  #不可用 self.key = value 否则造成无限循环调用__setattr__方法，只能通过实例属性字典赋值

           else:

               raise AttributeError
    x = AccessControl()
    x.age = 40

#加法（右侧加法，原处加法）



    # coding = utf-8
    class Number:
       def __init__(self, data):
           self.data = data
       def __add__(self, other):
           return self.data + other
       def __radd__(self, other):
           return other + self.data
       def __iadd__(self, other):
           return self.data + other
    x = Number(10)
    y = Number(11)
    x+=1

#Call 表达式



    # coding = utf-8
    class Callee:
       def __call__(self, *args, **kwargs):
           print('Called', args, kwargs)
    x = Callee()

#对象析构函数



    # coding = utf-8
    class Life:
       def __init__(self, name):
           self.name = name
       def __del__(self):
           print("Goodbye %s"%self.name)
    x = Life('bob')
    x =1