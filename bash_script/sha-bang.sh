#!/usr/bin/env bash
# sha-bang 只有在第一行才是, 在其他行都是注释; 不能指定解释器

echo "i am bash shell code"

:<<!
  【在bash执行其他语言的代码块】
!

#如果需要在shell脚本中执行其他语言的代码,可以采用如下方式：
/user/bin/python <<-EOF   #必须是 <<-
#以下代码重定向给python
print("i am python code")
# 这个区域也可以定向给bash来执行
EOF

:<<!
shell脚本的执行方式
  1、在 子shell 中执行
  2、在当前shell中执行
!
# 在 子shell 中执行：等同于新开的shell窗口执行命令集
bash shell-demo.sh
sh shell-demo.sh
./shell-demo.sh

# 在当前shell中执行：等同于在当前窗口执行命令集
# 使用场景：希望命令、变量等等能够影响到当前shell时， 就用这种方式
. shell-demo.sh
source shell-demo.sh


