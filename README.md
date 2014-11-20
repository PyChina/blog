# PyChina.org

in fact from 2003 there is CZUG.org ~ the 1st(and only one) focus Zope tech community be set up;

so years ago, there is soooooooo many python tech abt. commuity in China

but never group as one unify community brand,
like as: perl-china/ruby-china etc. 

so after PyCon2013China, some `old` Chinese Pythonista together and building:

![](PyChina_logo_131217_zq_h200.png)

## goal

- by Pythonner in China Operations
- as Pythonner in China Deleloping
- for Pythonista in Global support events organizing srvice


## organizer

- Sting
- Zoom.Quiet

## volunteer
cnpycon-volunteer <cnpycon-volunteer@googlegroups.com>

# usage
How to update the site contents?

as summary:

- generating all pages in local by `Pelican`
- usage `qrsync` push into pychina.qiniudn.com
- finally Nginx+DNS publish as http://pychina.org/

depending:

- Python
- Pelican
- git
- fabric


## main loop:

1. git clone
1. edit some .md in `content/`
1. `fab build` for test local
1. `fab put7niu` published all
1. git add->ci->push

in fact because github only embded Jekll,
but we r PyChina.org, so play with pure Python tools!

so, the site is generating in local, push into github,
but be sync into pychina.qiniudn.com,
publish as bind pychina.org  ;-)

### writing

- fork https://gitcafe.com/CPyUG/PyChina into local
- or becamed https://gitcafe.com/CPyUG member hold the repo. ACL
- cd into content/
- the sub-dir means:

        content/
            +- Events       首字母大写的是分类目录 收集对应文章
            +- Volunteer    ...志愿者
            +- _extra       扩展功能文件 e.g robots.txt
            +- _files       站内文件
            +- _images      样式图片
            `- pages        类似 about 的导航栏文档

#### 文章格式
- 标准 Markdown 格式
- 以 .md 为后缀
- 文件名不得使用中文/空格/符号
- 内容模板:

    Title: 中E可以混杂的标题
    Date: 2013-12-09
    Tags: people, shanghai
    Slug: sting-chen
    Author: Zoom.Quiet

- 其中:
    - `Date:` 如果没有将使用文件的系统时间
    - `Tags:` 使用逗号作间隔, 不宜过多,建议三个为界,以人物/行为/目标领域 为方向进行定义
        - 参考: [如何规划blog的标签（tag）和分类 - 心内求法 - 博客园](http://www.cnblogs.com/holbrook/archive/2012/11/05/2755268.html)
    - `Slug:` 是实际输出的页面文件名, 建议全部小写E文, 使用中划线, 不使用特殊符号

`注意:`

- 所有图片,应该事先发布到 7ni 空间中以便引用, 而不应该 push 到 git 仓库中
- 参考: [我们是如何使用7牛云储存的](http://blog.zhgdg.org/2013-08/usage7niu/)
- 自然的, 要加入协同编辑团队, 首先要获得 7niu 相关空间的配置文件
- 获取流程:
    + 注册 gitcafe 
    + 针对 [CPyUG/PyChina - GitCafe](https://gitcafe.com/CPyUG/PyChina) 发起一个有效的 `pull-request` , 证明你懂的
    + 向社区说明意愿 support@pychina.org
    + 获得 `7niu4pychina.json`

### deploy

支持本地调试! 使用 `fabric` 进行管理, 支持的命令:

    fab 
    Available commands:

        build       编译所有页面
        put7niu     本地完成编译,通过工具上传到 7niu
        reserve     重编译所有页面再启动本地服务
        serve       启动本地服务 localhost:8000


参考: [qrsync 命令行同步工具 | 七牛云存储](http://developer.qiniu.com/docs/v6/tools/qrsync.html)

### design

基于 [pelican-bootstrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3) 深度定制

- 配置: `pelicanconf.py`
- 样式: `_themes/pelican-bootstrap3/`
- 插件: `_plugins/`

## changelog

- 141120 增补文档,明确协同流程
- 141119 upgrade as 3.5.0 base [issue #264](https://github.com/getpelican/pelican-plugins/issues/264) fixed sitemap.py 
- 131218 base pelican build and through qiniu.com publish