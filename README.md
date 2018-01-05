# Github-WP-SidebarTools

----

### Github Wordpress 侧边栏小工具

最近读了一下Github的文档，于是想在自己的blog的侧边栏上放置一个Github动态小工具。

### 用法

#### 安装依赖

`pip install -r requirements.txt`

#### 配置

将github的用户名填写进代码中。

`Url = https://api.github.com/user/yourname/events`

将yourname替换为你的Github用户名

#### 使用

在主机商开启定时任务，定时运行Python脚本生成包含Github事件动态的的json文件(day.json)

在需要显示的地方使用JQurey代码来ajax获取day.json并输出到网页当中。

test目录内带有一个简易用法演示。