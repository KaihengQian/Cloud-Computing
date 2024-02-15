# 目录结构
```
│  DataPreprocess.py                                    // 脚本程序，负责数据预处理
│  ModelPrediction.py                                   // 脚本程序，负责模型预测
│  requirements.txt                                     // 环境依赖
│  README.md                                            // 帮助文档
│  SituationAnalysis.py                                 // 脚本程序，负责现状分析
│          
├─dataset                                               // 实验数据集，程序运行时创建
│      all_city_data.csv                                // 所有城市数据集
│      selected_city_data.csv                           // 拥有五大联盟球队的城市数据集
│      team_data.csv                                    // 球队数据集
│     
├─model                                                 // 模型相关类、函数封装
│      model.py                                         // 模型调用程序
│      
├─picture                                               // 词云图背景图片
│      beckham.jpg
│      harden.jpg
│      ovechkin.jpg
│      usa_map.jpg
│      
├─raw_dataset                                           // 原始数据集
│      US_2019_GDP_by_state.csv
│      US_2020_census_by_city_density.csv
│      US_2020_census_by_city_location.csv
│      US_2020_census_by_state.csv
│      US_teams.csv
│      
└─result                                                // 词云图，程序运行时创建
        city_success_index_wordcloud.png
        predicted_city_success_index_wordcloud.png
        team_number_wordcloud.png
        team_success_index_wordcloud.png
```
# 项目部署
## 进入工作目录
```
C:\Users\user> cd /your/path/Project
```
## 安装环境依赖
```
/your/path/Project> pip install -r requirements.txt
```
## 运行脚本程序
请按照先后顺序依次运行三个脚本程序。
```
/your/path/Project> python DataPreprocess.py
/your/path/Project> python SituationAnalysis.py
/your/path/Project> python ModelPrediction.py
```
