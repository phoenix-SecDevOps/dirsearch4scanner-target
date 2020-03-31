# dirsearch4scanner-target
Target for dirsearch scanner version to test false positive and true nagetive.

## ENV

```bash
$ python -V
Python 3.7.1
$ pip install -r requirments.txt
```

## USAGE

```bash
$ export FLASK_APP=sen.py
$ export FLASK_ENV=development      # for debug 
$ flask run
```

## 靶场说明

1. 自定义404响应，响应码200
2. 自定义WAF响应，响应码200
3. `phpinfo.php` 触发WAF
4. 特殊路径处理逻辑一：`app.[anything]`, 响应逻辑为同一个
5. 特殊路径处理逻辑一：`[anything].config`, 响应逻辑为同一个
6. `webadmin/`触发禁止请求，响应码403
7. `webadmin/web.7z`，响应吗200

## WAVSEP靶场

1. http://222.186.129.63:8089/wavsep/active/Obsolete-Files/ObsoleteFile-Detection-Evaluation-GET-200Error/index.jsp
2. http://222.186.129.63:8089/wavsep/active/Obsolete-Files/ObsoleteFile-FalsePositives-GET/index.jsp