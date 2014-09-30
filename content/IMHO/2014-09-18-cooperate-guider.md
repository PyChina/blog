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

#### 7牛 使用:
参考:

- [我们是如何使用7牛云储存的 | GDG Livin ZhuHai Life;-)](http://blog.zhgdg.org/2013-08/usage7niu/)
    - [How to from Jekyll jump into Pelican |蠎周刊 |汇集全球蠎事儿 !-)](http://weekly.pychina.org/chaos/jekyll-to-pelican.html)
- [qrsync 命令行同步工具 | 七牛云存储](http://developer.qiniu.com/docs/v6/tools/qrsync.html)

背景:

- `cn.pycon.org` 主机在国外
- 相关配置为:

```
location ^~ /2014/ {
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host pyconcn.qiniudn.com;
    proxy_pass  http://pyconcn.qiniudn.com/2014/ ;
}
```


所以,7牛空间的协同思路:

- 为发布 官网, 本地统一预留使用 `/2014` 目录链接为文档工程中的 `site`
- 其它目录, 确保唯一即可
- e.g. 在 7牛 空间中可以是:

```
http://pyconcn.qiniudn.com/
    +- 2014/
    +- zoomquiet/
    |   +- 2011
    |   +- 2012
    |   +- 2013
    |   +- ...
    |   `- stuff14
    +- [someone]
    +- ...

```


- 但是,在不同的志愿者本地, 目录可以是:


```
http://pyconcn.qiniudn.com/
    +- 2014/
    `- [someone]
        +- foto
        +- logo
        +- ...

```


- 因为, 7牛 不是 `Dropbox` 不是一种多点双向同步空间服务
- 而是, `高速单向数据同步服务`
- 实际上 7牛 是没有目录的概念的
    - 比如: `http://pyconcn.qiniudn.com/zoomquiet/stuff14/logo/cmcm-logo.png`
    - 其中 `zoomquiet/stuff14/logo/cmcm-logo.png` 即是数据对象 `ID`
    - 所以, 我们想在 7牛空间中有文件索引可看,就要自个儿生成
    - 即运行 `$ python gen4idx.py ./ footer-7niu.html 2014`
    - 当然的,在本地 7牛 同步目录中

综合上,对于协同志愿者,对 7牛 的启用应该是:

- 安排好工作目录, 类似:

```
/path/2/ur/local/cn.pycon/
    +- 7niu-pycon.json
    +- 7niu.pyconcn/ 
    |   +- 2014/ <~~~~~+
    |   +- [someone]   |
    |   +- ...         |
    +- ...             |
    +- MkDoc4PyCon/    |
    |   +- .git/     ln -s
    |   +- _theme/     |
    |   +- docs/       |
    |   +- site/ ~~~~~~+
    |   +- .gitignore
    |   +- fabfile.py
    |   +- footer-7niu.html
    |   +- gen4idx.py
    |   +- mkdocs.yml
    |   +- ...
    +- ...

```


- 当然的,本地的目录名,不用完全和这里的一样,关键要确保 `fabric` 可运行成功就好
- 对应的配置项可以自行根据需求变更 `fabfile.py`: 

```
env.qiniu = '/opt/bin/7niu_package_darwin_amd64/qrsync'
env.qiniu_conf = '../7niu-pycon.json'
env.qiniu_path = '../7niu.pyconcn'
```

- 当然的,这种本地配置,就不用同步到协同仓库,所以,提醒,进行了个性化配置后,增补 `.gitignore` 忽略修订,以免意外扩散给小伙伴们.
- 为首次同步将 `footer-7niu.html`, `gen4idx.py` 复制到本地的 7牛目录中
- 建立唯一的 `[someone]` 私人数据目录
- 最好通过其它沟通渠道, 事先和小伙伴们明确 `[someone]` 在团队中的唯一
- 否则,将造成 7牛 空间相同目录浏览时,文件看不到,但是,可以使用的现象 
- 合理配置 `7niu-pycon.json`

```
{
    "src":          "/path/2/your/sync_dir",
    "dest":         "qiniu:access_key=<AccessKey>&secret_key=<SecretKey>&bucket=<Bucket>&key_prefix=<KeyPrefix>&threshold=<Threshold>",
    "deletable":    0,
    "debug_level":  1
}
```


- 正常情况下, 嘦调整 `"src"` 的内容,指向本地目录,即可

然后,可以手工在本地的 7牛 目录中,模拟 `fab pub2cafe` 的行为,运行:

    $ python gen4idx.py ./ footer-7niu.html 2014
    ...
    $ /path/2/local/qrsync -skipsym ../7niu-pycon.json
    ...

明确一切正当, 在 `http://pyconcn.qiniudn.com/[someone]` 中可以看到期望的文件.

表示一切 KO 了.


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

- 140930 增补 7牛 空间的使用理解
- 140919 增补ASCII 图谱
- 140918 针对当前志愿者情况创立

