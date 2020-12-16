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

项目是通过 `git clone` 将github 上的项目拷贝到本地的（ `https` 的方式），但是每次使用 `git push` 将项目推送到github上的时候都提示要登陆，具体提示内容如下所示：

（1）提示GitHub Login

![](images/20201216_01_GithubLogin.png)

 

（2）提示OpenSSH

![](images/20201216_02_OpenSSH.png)

# 问题分析

1、这是 git 的一个认证问题，所以我们可以把认证信息存储下来，避免重复访问

# 解决方式

## 1、git config --global credential.helper store

进入到 git 项目中，然后运行命令 `git config --global credential.helper store` ，该命令会在

# 参考资料

[1] git-credential-store: https://git-scm.com/docs/git-credential-store

[2] git credential: https://git-scm.com/docs/gitcredentials