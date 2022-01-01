#!/usr/bin/env bash
# sha-bang 只有在第一行才是, 在其他行都是注释; 不能指定解释器
a=10
b=5
# shellcheck disable=SC2003
c=$(expr $a + $b)
# shellcheck disable=SC2086
echo $c

# 定义函数：有参数函数
function add_demo() {

#  定义的参数： $1 第一个参数; $2 第二个参数; .... 第十个参数 ${18};
  sum=$(expr $1 + $2)
:<<!
    1、函数返回值，可以显式增加return语句；如果不加，会将最后一条命令运行结果作为返回值。
    2、Shell 函数返回值只能是整数，一般用来表示函数执行成功与否，0表示成功，其他值表示失败。
 如果 return 其他数据，比如一个字符串，往往会得到错误提示：“numeric argument required”。
    3、如果一定要让函数返回字符串，那么可以先定义一个变量，用来接收函数的计算结果，
 脚本在需要的时候访问这个变量来获得函数返回值。
!
  return $sum
}
:<<!
函数的调用： 函数名 parameter1 parameter2 parameter3
!
add_demo 1 2

:<<!  多行注释
 功能：ping 一个域名, 通过时返回 success，失败时返回 failed
 1、 -c1 表示只ping一次;
 2、 && 命令连接符; 连接两个命令，如果第一个命令执行成功,则执行 && 后面一个, 否则不执行
 3、 || 命令连接符; 连接两个命令，如果第一个命令执行成功,则执行 || 后面一个, 否则不执行
!
ping -c1 baidu.com.cn>/dev/null && echo "ping success" || echo "ping failed"


#重定向 >
#追加文件内容 >>
