# 目录结构

---

E:.<br />
│  DataPreprocess.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;脚本程序，负责数据预处理<br />
│  ModelPrediction.py &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;脚本程序，负责模型预测<br />
│  requirements.txt &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; //&emsp;环境依赖<br />
│  README.md &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;帮助文档<br />
│  SituationAnalysis.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;脚本程序，负责现状分析<br />
│<br />
├─dataset&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;实验数据集，程序运行时创建<br />
│ &emsp; all_city_data.csv &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;所有城市数据集<br />
│ &emsp; selected_city_data.csv &emsp;&emsp;&emsp; //&emsp;拥有五大联盟球队的城市数据集<br />
│ &emsp;  team_data.csv&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;球队数据集<br />
│<br />
├─model &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;模型相关类、函数封装<br />
│ &emsp; model.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;//&emsp;模型调用程序<br />
│<br />
├─picture &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; //&emsp;词云图背景图片<br />
│ &emsp; beckham.jpg<br />
│ &emsp; harden.jpg<br />
│ &emsp; ovechkin.jpg<br />
│ &emsp; usa_map.jpg<br />
│<br />
├─raw_dataset &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; //&emsp;原始数据集<br />
│ &emsp; US_2019_GDP_by_state.csv<br />
│ &emsp; US_2020_census_by_city_density.csv<br />
│ &emsp; US_2020_census_by_city_location.csv<br />
│ &emsp; US_2020_census_by_state.csv<br />
│ &emsp; US_teams.csv<br />
│<br />
└─result &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; //&emsp;词云图，程序运行时创建<br />
&emsp;&emsp; city_success_index_wordcloud.png<br />
&emsp;&emsp; predicted_city_success_index_wordcloud.png<br />
&emsp;&emsp; team_number_wordcloud.png<br />
&emsp;&emsp; team_success_index_wordcloud.png
# 项目部署

---

## 进入工作目录
```python
C:\Users\user> cd /your/path/Project
```
## 安装环境依赖
```python
/your/path/Project> pip install -r requirements.txt
```
## 运行脚本程序
请按照先后顺序依次运行三个脚本程序。
```python
/your/path/Project> python DataPreprocess.py
/your/path/Project> python SituationAnalysis.py
/your/path/Project> python ModelPrediction.py
```
