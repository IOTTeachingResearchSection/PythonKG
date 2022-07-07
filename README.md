# PythonKG
这是一个关于Python课程的知识图谱项目

# 1 python课程本体构建

## 1.1 本体的概念

本体理论属于人工智能的内容理论范畴，是共享概念模型的明确形式化规范说明，研究特定领域知识的对象分类、对象属性和对象间的关系，它为领域知识的描述提供术语。简单说，可以将本体理解为公共认同的关于领域知识的明确描述。“本体是关于某个主题的形式化和说明性表示，包括它的领域、论域中诸对象的名称、定义及相关关系”。

**本体是领域知识图谱的 主体框架 或 大纲。**

## 1.2 本体构建原则

Grube提出的本体构建的5个指导原则：

#### 1.明确性和客观性：

概念内容的含义明确、表达客观；

#### 2.一致性：

概念和推理出来的概念不矛盾；

#### 3.可扩展性：

向概念集中添加新概念时，无须修改原有概念集；

#### 4.最小编码偏差

对概念的描述不依赖特定的符号表示方法；

#### 5.最小本体承诺

应对所建模的事物定义尽可能少的约束和公理 ,以满足共享者特定的知识共享需求即可。

**本体的构建并不存在完全正确的方法。应当是一个多次迭代、不断完善和不断优化的过程。**

参考：

1. 学科知识的可视化技术研究与实现_张亚龙 P21-23

### 1.3 本体构建的一般步骤

#### 1.确定本体的领域和范围



#### 2.获取学科知识

主要获取途径：教材特别是目录、教学大纲、专家（教师）。

#### 3.列举学科重要知识概念

列举主要的概念和词汇。

#### 4.确定知识概念的层次、属性并实例化

根据业务需求，参考教材目录结构确定个概念层次，根据业务需求确定属性。

#### 5.编码化

将本体用专业软件编辑保存，如protege。

简化版步骤：

![image-20220706142425925](/home/richard/snap/typora/57/.config/Typora/typora-user-images/image-20220706142425925.png)





### 1.4 利用Protege构建本体

参考：

1. protege下载地址：https://protege.stanford.edu/
2. B站学习视频：[Protege入门](https://www.bilibili.com/video/BV1ME411j7su?spm_id_from=333.337.search-card.all.click&vd_source=3d514af595c86a0e29c4439b4ae8e478)



# 2 git工程管理

## 2.1 git概念

Git是目前世界上最先进的分布式版本控制系统。

工作原理 / 流程：

![img](https://pic2.zhimg.com/80/v2-3bc9d5f2c49a713c776e69676d7d56c5_720w.jpg)

Workspace：工作区
Index / Stage：暂存区
Repository：仓库区（或本地仓库）
Remote：远程仓库

## 2.2 安装git

[Git官网](https://link.jianshu.com/?t=https://git-scm.com/)下载Git的安装程序。

## 2.3 git常用命令

```bash
git init                                                  # 初始化本地git仓库（创建新仓库）
git config --global user.name "xxx"                       # 配置用户名
git config --global user.email "xxx@xxx.com"              # 配置邮件
git clone git+ssh://git@192.168.53.168/VT.git             # clone远程仓库
git status                                                # 查看当前版本状态（是否修改）
git add xyz                                               # 添加xyz文件至index
git add .                                                 # 增加当前子目录下所有更改过的文件至index
git commit -m 'xxx'                                       # 提交
git commit --amend -m 'xxx'                               # 合并上一次提交（用于反复修改）
git commit -am 'xxx'                                      # 将add和commit合为一步
git rm xxx                                                # 删除index中的文件
git rm -r *                                               # 递归删除
git log                                                   # 显示提交日志
git remote add origin git+ssh://git@192.168.53.168/VT.git # 增加远程定义（用于push/pull/fetch）
git merge origin/master                                   # 合并远程master分支至当前分支
git push origin master                                    # 将当前分支push到远程master分支
git pull origin master                                    # 获取远程分支master并merge到当前分支
git reset --hard HEAD                                     # 将当前版本重置为HEAD（通常用于merge失败回退）
```

参考：

1.https://zhuanlan.zhihu.com/p/30044692

2.https://www.jianshu.com/p/db3396474b96

### 2.4 github项目仓库

### 2.4.1 github的概念

*GitHub*是一个在线软件源代码托管服务平台，使用*Git*作为版本控制软件。

### 2.4.2 github项目及使用

#### 1. 项目地址：

https://github.com/IOTTeachingResearchSection/PythonKG

#### 2. 团队:

https://github.com/orgs/IOTTeachingResearchSection/teams/team-1/members

![image-20220706125656796](/home/richard/snap/typora/57/.config/Typora/typora-user-images/image-20220706125656796.png)

需要大家提供github的邮箱或账户才能邀请加入团队。

#### 3. 项目操作

##### 方式一：

​	用git客户端，通过git的相关命令操作；

##### 方式二：

​	用github桌面客户端，通过图形界面操作，具体参考：https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop

##### 方式三：

  将项目git clone下来，在桌面vscode中打开，并利用vscode的版本控制功能；

##### 方式四：

  直接利用web版vscode，这也是推进方式。激活方法是在[项目地址](https://github.com/IOTTeachingResearchSection/PythonKG)上敲击键盘上的 . （句号）键。

【方式四】激活后效果：

![image-20220706130927611](/home/richard/snap/typora/57/.config/Typora/typora-user-images/image-20220706130927611.png)



![image-20220706131122117](/home/richard/snap/typora/57/.config/Typora/typora-user-images/image-20220706131122117.png)

​    如果添加或修改项目中的文件，直接在web版vscode中执行即可。这里也支持文件拖放，即直接将文件从本体拖放到项目的EXPLORER栏（即左侧导航栏）中，或反过来。针对添加或修改的文件，左侧导航栏会显示A或M符号。但这些修改并未真正提交到远程仓库。

​    要将修改提交到远程仓库，需要切换到source controller栏，填入提交内容说明，再执行提交。

![image-20220706132044885](/home/richard/snap/typora/57/.config/Typora/typora-user-images/image-20220706132044885.png)