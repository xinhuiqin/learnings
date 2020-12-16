[TOC]

《git push 总是要登陆问题的解决办法》

# 背景描述

1、windows

```
>systeminfo
Windows 10 Pro
```

2、Git Bash:

```
$ git --version
git version 2.28.0.windows.1
```

# 问题描述

项目是通过 `git clone` 将github 上的项目拷贝到本地的（HTTPS的方式），但是每次使用 `git push` 将项目推送到github上的时候都提示要登陆，具体提示内容如下所示：

（1）提示GitHub Login

![](images/20201216_01_GithubLogin.png)

 

（2）提示OpenSSH登录

![](images/20201216_02_OpenSSH.png)