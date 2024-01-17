<a name="iJTS1"></a>
# 目录结构

---

E:.<br />│  DataPreprocess.py                                         //  脚本程序，负责数据预处理<br />│  ModelPrediction.py                                       //  脚本程序，负责模型预测<br />│  requirements.txt                                            //  环境依赖<br />│  README.md                                                  //  帮助文档<br />│  SituationAnalysis.py                                      //  脚本程序，负责现状分析<br />│          <br />├─dataset                                                          //  实验数据集，程序运行时创建<br />│      all_city_data.csv                                         //  所有城市数据集<br />│      selected_city_data.csv                                //  拥有五大联盟球队的城市数据集<br />│      team_data.csv                                            //  球队数据集<br />│      <br />├─model                                                            //  模型相关类、函数封装<br />│      model.py                                                    //  模型调用程序<br />│      <br />├─picture                                                           //  词云图背景图片<br />│      beckham.jpg<br />│      harden.jpg<br />│      ovechkin.jpg<br />│      usa_map.jpg<br />│      <br />├─raw_dataset                                                   //  原始数据集<br />│      US_2019_GDP_by_state.csv<br />│      US_2020_census_by_city_density.csv<br />│      US_2020_census_by_city_location.csv<br />│      US_2020_census_by_state.csv<br />│      US_teams.csv<br />│      <br />└─result                                                             //  词云图，程序运行时创建<br />        city_success_index_wordcloud.png<br />        predicted_city_success_index_wordcloud.png<br />        team_number_wordcloud.png<br />        team_success_index_wordcloud.png
<a name="u287t"></a>
# 项目部署

---

<a name="Hgoh1"></a>
## 进入工作目录
```python
C:\Users\user> cd /your/path/Project
```
<a name="JIgnp"></a>
## 安装环境依赖
```python
/your/path/Project> pip install -r requirements.txt
```
<a name="bgSy2"></a>
## 运行脚本程序
请按照先后顺序依次运行三个脚本程序。
```python
/your/path/Project> python DataPreprocess.py
/your/path/Project> python SituationAnalysis.py
/your/path/Project> python ModelPrediction.py
```
