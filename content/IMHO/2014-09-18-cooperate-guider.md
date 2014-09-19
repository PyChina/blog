Title: PyCon2014China 志愿者协同手册
Date: 2014-09-18 19:19
Categories: Doc
Tags:  PyCon, guider, volunteer
Slug: cooperate-guider
Author: Zoom.Quiet

## 背景
参考: [PyCon2014China](http://cn.pycon.org/2014/) 官网

PyCon 中国到今年是第四届了,以往志愿者基本只负责了现场会务,
而更加复杂长期的赞助/官网/宣传... 基本都是号称志愿者,实为义务组织者的少数人在支撑,
这不科学!

CPyUG 列表可是聚集了 11K 行者哪!

所以,今年求上进!

## 任务
筹备期间,最要紧的任务有:

1. 官网日常内容增补
2. 官网E文版本翻译
3. 宣传/纪念品设计
4. CSDN 等媒体合作渠道每周文案起草

而任务的并行解决,需要有完备/统一/固定的:

- 任务说明
- 执行支持
- 成果检验
- 任务管理


## 方案
参考: [制造开源软件](http://producingoss.com/zh/) ~ 如何成功运营自由软件项目

将一次大会视作一个标准的开源软件项目来管理的话,
自然的形成了常见的工具链:

- 创建 [CnPyCon-volunteer](cnpycon-volunteer@googlegroups.com) ~ 中国PyCon-志愿者 列表, 进行日常讨论
- 创建 [PyConChina](https://gitcafe.com/PyConChina) ~ gitcafe组织,管理git 仓库,容纳各种制品
- 开辟 [PyCon2014China筹办 | Trello](https://trello.com/b/TLsl0TM7/pycon2014china) 故事板, 追踪长期任务
- 实施 `AKA` (All Know All) 原则,鼓励主动创建/认领/完成 任务

## 细则
随着协同的范围扩大,以下细则将持续增补

### 加入

成为 PyCon2014China 志愿者,要主动完成的流程:

1. 填写 [志愿申请表单](http://cn.pycon.org/2014/volunteer/)
2. 订阅 [CnPyCon-volunteer](cnpycon-volunteer@googlegroups.com)列表
3. 注册 [gitcafe](https://gitcafe.com)

最后向 [列表](cnpycon-volunteer@googlegroups.com) 发送邮件说明:

- 志愿担当的领域任务
- [gitcafe](https://gitcafe.com) 帐号

## 官网运维

### 小组加入流程:

1. 参考 [README.md](https://gitcafe.com/PyConChina/MkDoc4PyCon/blob/master/README.md) 在本地部署成功
2. 截屏,在 [列表](cnpycon-volunteer@googlegroups.com) 发送邮件说明:
    -  [gitcafe](https://gitcafe.com) 帐号
    -  申请 7niu 相关配置文件
3. 由大妈完成相关操作:
    - 配置为 [MkDoc4PyCon](https://gitcafe.com/PyConChina/MkDoc4PyCon) `项目协作人员` 
    - 私下发放 7niu 配置文件 
4. 主动加入 `cn.pycon 志愿运维组` 微信群

至此,获得官网维护的所有配置资源,进入实时维护状态 ;-)

### 日常运维流程:

1. 关注 [列表](cnpycon-volunteer@googlegroups.com) / 微信群 中的信息更新
2. 在有关协同文档中增补信息
    - [讲师信息](https://docs.google.com/spreadsheet/ccc?key=0AgPxePCteZKodHRiNHV1N0Y0OVR5RTh2a2VWLWY5WUE#gid=7) 增补讲师数据变化
    - **[cn.pycon 官网内容统稿池](https://docs.google.com/document/d/1baO6J9LL4QGsSk9bVkHu7G0iF-1TUhuTwAubj4xETeg/edit#)** 增补整理好的文案
    - 同步头像等图片到合适的 7niu 空间,比如说: [头像](http://pyconcn.qiniudn.com/zoomquiet/stuff14/id/index.html)
3. 在 [列表](cnpycon-volunteer@googlegroups.com) / 微信群 提示自己的增补
4. 发布到官网:
    - 通过 git 仓库提交 `.md` 的修订
    - 通过 [qrsync 命令行同步工具](http://developer.qiniu.com/docs/v6/tools/qrsync.html) 同步最新编译网页到 7niu
5. 检查官网内容变化, 进行必须的修订

E文版本翻译也基于以上,一样的流程.

### 日常增进流程:
指功能等非内容方面的改进.

1. 在 [工单 · PyConChina/MkDoc4PyCon - GitCafe](https://gitcafe.com/PyConChina/MkDoc4PyCon/tickets) 描述想法
2. 在 [列表](cnpycon-volunteer@googlegroups.com) / 微信群 发起讨论
3. 明确具体改进后,独自或是联合完成改进
4. 发布到官网:
    - 通过 git 仓库提交代码修订, 配合应该的足够详细的注释
5. 关闭对应 [工单](https://gitcafe.com/PyConChina/MkDoc4PyCon/tickets)


### 约定

- 请参考:[图片处理（imageView2） | 七牛云存储](http://developer.qiniu.com/docs/v6/api/reference/fop/image/imageview2.html) 应用在 md 代码的图片引用中,统一大小
- 暂时没有收到合适头像的,统一使用

![nopic](http://pyconcn.qiniudn.com/zoomquiet/stuff14/id/nopic.gif)


## 小结

所以,整体上,目前的协同,非常简洁


    wechat|列表
    ~~~~~~~~~~  内部讨论|提醒
     ^      \
     |       +- gitcafe     协同平台                  
     |            |  \
     |            |   +- Repo.  制品管理
     |            |         \
     |            |          +- MkDocs  生成工具
     |            |                 \
     |            |                  +- 7niu    发布空间
     |            `- Issues     提案追踪
      \_______________/





## 版本

- 140919 增补ASCII 图谱
- 140918 针对当前志愿者情况创立

