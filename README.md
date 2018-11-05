# fuzzing - 无前提下直接进行黑盒挖掘

```
1.>快速测试：
在"generate.sh"文件中修改"python generator.py --output_dir ../recurve/ --no_of_files 999"中最后的生成数目调小进行

2.>工程化：
./generate.sh //构造利用页面，默认创建1000个页面进行长时间的自动黑盒
python fuzzing.py //开始奔跑!

3.>浏览器添加：
我不知道还有哪些浏览器你希望挖掘它的漏洞，如果你需要的话，告诉我
```
4.>自主开发建议：
核心是使用了谷歌的domato项目，然后我们创造了这个小小的自动化机器人，这不妨碍它成为一个伟大的python代码，在linux下可以快速零门槛的帮助任何人进行黑盒测试找到Crash，如果你找到了请告诉我。

5.>漏洞报告地址:
1. https://bugs.chromium.org/p/chromium/issues/list
2. https://bugzilla.mozilla.org/enter_­bug.cgi?product=Firefox
```


