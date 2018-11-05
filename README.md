# fuzzing - 无前提下直接进行黑盒挖掘

```
1.>快速测试：
在"generate.sh"文件中修改"python generator.py --output_dir ../recurve/ --no_of_files 999"中最后的生成数目调小进行

2.>工程化：
./generate.sh //构造利用页面，默认创建1000个页面进行长时间的自动黑盒
python fuzzing.py //开始奔跑!
```
> 核心是使用了谷歌的domato项目，创造了这个小小的自动化机器人，希望你能找到Crash，如果找到了请告诉我。
```


