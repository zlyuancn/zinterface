# python的interface模式

## 它是什么, 有什么用
#### zinterface是一个帮助python实现接口模式的模块, interface模式能让多人合作开发变得轻松, 能解决代码依赖, 让程序逻辑更加清晰

## python有了本身就是鸭子类型的, 为什么还要多此一举
#### 在python中, 一个类可以当成另一个类型来使用, 前提是这个类实现了该类型的方法, 但是在IDE中它不会显示的告诉你这个类是否实现了该类型的所有方法, zinterface能帮助你强行要求某个类必须实现某个类型的所有方法, 能在代码预编译时就会报告某些方法未被实现

## 如何安装它
##### `pip install zinterface`

## 主页
#### [github.com/zlyuancn/zinterface](https://github.com/zlyuancn/zinterface "github")

## 导入zinterface
```python
from zinterface import InterfaceBase, InterfaceCheck
```

## 创建接口类
```python
@InterfaceBase
class IAA():
    def test(self):  # 需要实现的类型
        pass
```

## 创建一个类实现该接口
```python
@InterfaceCheck
class AA(IAA):
    def test(self):
        print('测试')
```

## 高级用法实例
```python
from zinterface import InterfaceBase, InterfaceCheck

@InterfaceBase
class IRead():
    def read(self):
        pass

@InterfaceBase
class IWrite():
    def write(self, data):
        pass

@InterfaceBase
class IFile(IRead, IWrite):
    pass

@InterfaceCheck
class MyFileBase(IFile):
    def read(self):
        print('读取')

    def write(self, data):
        print('写入')

a = MyFileBase()
a.read()
a.write(None)
```

### 更新日志
发布时间|发布版本|发布说明
--|:--:|---
19-02-19 | 0.1.0 | 发布第一版

- - -
##### 本项目仅供所有人学习交流使用, 禁止用于商业用途
