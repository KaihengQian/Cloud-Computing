import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import plotly.graph_objects as go


# 绘制球队成功指数词云图
def plot_team_success_index_wordcloud(dataset_path, fig_path):
    # 读取team_data.csv文件内容
    team_data = pd.read_csv(dataset_path)

    team_wordcloud_info = pd.DataFrame(index=team_data['Team'])  # 以team_data的Team列为index新生成一个dataframe
    team_wordcloud_info['权重'] = 0
    for i in range(0, team_data.shape[0]):
        team_wordcloud_info.iloc[i, 0] = team_data.loc[i, 'Success Index']
    team_wordcloud_info = team_wordcloud_info['权重'].sort_values(ascending=False)
    team_wordcloud_info = dict(team_wordcloud_info)  # 生成字典形式的数据

    background_Image = np.array(Image.open("picture/ovechkin.jpg"))  # 读取背景图片
    img_colors = ImageColorGenerator(background_Image)  # 提取背景图片颜色

    plt.figure(figsize=(10, 8), dpi=1000)  # 创建画板 ,定义图形大小及分辨率
    mask = plt.imread("picture/ovechkin.jpg")  # 自定义背景图片
    team_wordcloud = WordCloud(mask=mask, width=800, height=500, scale=2, mode="RGBA", background_color='white')  # 设置词云图相关参数
    team_wordcloud = team_wordcloud.generate_from_frequencies(team_wordcloud_info)  # 利用生成的字典形式的数据制作词云图
    team_wordcloud.recolor(color_func=img_colors)  # 根据图片色设置背景色

    # 保存词云图
    team_wordcloud.to_file(fig_path)


# 绘制球队数量地理分布词云图
def plot_team_number_wordcloud(dataset_path, fig_path):
    # 读取selected_city_data.csv文件内容
    selected_city_data = pd.read_csv(dataset_path)

    team_wordcloud_info = pd.DataFrame(index=selected_city_data['City'])  # 以selected_city_data的City列为index新生成一个dataframe
    team_wordcloud_info['权重'] = 0
    for i in range(0, selected_city_data.shape[0]):
        team_wordcloud_info.iloc[i, 0] = selected_city_data.loc[i, 'Team Number']
    team_wordcloud_info = team_wordcloud_info['权重'].sort_values(ascending=False)
    team_wordcloud_info = dict(team_wordcloud_info)  # 生成字典形式的数据

    background_Image = np.array(Image.open("picture/harden.jpg"))  # 读取背景图片
    img_colors = ImageColorGenerator(background_Image)  # 提取背景图片颜色

    plt.figure(figsize=(10, 8), dpi=1000)  # 创建画板 ,定义图形大小及分辨率
    mask = plt.imread("picture/harden.jpg")  # 自定义背景图片
    team_wordcloud = WordCloud(mask=mask, width=800, height=500, scale=2, mode="RGBA", background_color='white')  # 设置词云图相关参数
    team_wordcloud = team_wordcloud.generate_from_frequencies(team_wordcloud_info)  # 利用生成的字典形式的数据制作词云图
    team_wordcloud.recolor(color_func=img_colors)  # 根据图片色设置背景色

    # 保存词云图
    team_wordcloud.to_file(fig_path)


# 绘制球队数量地理分布气泡图
def plot_team_number_map(dataset_path, fig_path):
    # 读取selected_city_data.csv文件内容
    selected_city_data = pd.read_csv(dataset_path)

    team_map_info = selected_city_data[['City', 'Longitude', 'Latitude', 'Team Number']]
    team_map_info = team_map_info.sort_values(by=['Team Number'], ascending=False)
    team_map_info = team_map_info.reset_index(drop=True)

    team_map_info['text'] = team_map_info['City'] + '<br>Team Number: ' + (team_map_info['Team Number']).astype(str)
    limits = [(0, 2), (2, 7), (7, 12), (12, 20), (20, 37), (37, 57)]  # 根据拥有的球队数量将城市分类
    colors = ["crimson", "MediumPurple", "royalblue", "lightseagreen", "orange", "lightgrey"]  # 每类一种颜色
    cities = []
    scale = 0.004  # 保证气泡的大小合适

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        team_map_info_sub = team_map_info[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon=team_map_info_sub['Longitude'],
            lat=team_map_info_sub['Latitude'],
            text=team_map_info_sub['text'],
            marker=dict(
                size=team_map_info_sub['Team Number']/scale,  # 气泡大小与拥有的球队数量正相关
                color=colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode='area'
            ),
            name='{0} - {1}'.format(lim[0], lim[1])))

    fig.update_layout(
        title_text='US city team numbers<br>(Click legend to toggle traces)',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='rgb(217, 217, 217)',
        )
    )

    # 将气泡图导出为html文件
    fig.write_html(fig_path)


# 绘制城市成功指数词云图
def plot_city_success_index_wordcloud(dataset_path, fig_path):
    # 读取selected_city_data.csv文件内容
    selected_city_data = pd.read_csv(dataset_path)

    city_wordcloud_info = pd.DataFrame(index=selected_city_data['City'])  # 以selected_city_data的City列为index新生成一个dataframe
    city_wordcloud_info['权重'] = 0
    for i in range(0, selected_city_data.shape[0]):
        city_wordcloud_info.iloc[i, 0] = selected_city_data.loc[i, 'Success Index']
    city_wordcloud_info = city_wordcloud_info['权重'].sort_values(ascending=False)
    city_wordcloud_info = dict(city_wordcloud_info)  # 生成字典形式的数据

    background_Image = np.array(Image.open("picture/beckham.jpg"))  # 读取背景图片
    img_colors = ImageColorGenerator(background_Image)  # 提取背景图片颜色

    plt.figure(figsize=(10, 8), dpi=1000)  # 创建画板 ,定义图形大小及分辨率
    mask = plt.imread("picture/beckham.jpg")  # 自定义背景图片
    city_wordcloud = WordCloud(mask=mask, width=800, height=500, scale=2, mode="RGBA", background_color='white')  # 设置词云图相关参数
    city_wordcloud = city_wordcloud.generate_from_frequencies(city_wordcloud_info)  # 利用生成的字典形式的数据制作词云图
    city_wordcloud.recolor(color_func=img_colors)  # 根据图片色设置背景色

    city_wordcloud.to_file(fig_path)


# 绘制城市成功指数地理分布气泡图
def plot_city_success_index_map(dataset_path, fig_path):
    # 读取selected_city_data.csv文件内容
    selected_city_data = pd.read_csv(dataset_path)

    city_map_info = selected_city_data[['City', 'Longitude', 'Latitude', 'Success Index']]
    city_map_info = city_map_info.sort_values(by=['Success Index'], ascending=False)
    city_map_info = city_map_info.reset_index(drop=True)

    city_map_info['text'] = city_map_info['City'] + '<br>Success Index: ' + (city_map_info['Success Index']).astype(str)
    limits = [(0, 2), (2, 10), (10, 16), (16, 27), (27, 40), (40, 57)]  # 根据成功指数将城市分类
    colors = ["crimson", "MediumPurple", "royalblue", "lightseagreen", "orange", "lightgrey"]  # 每类一种颜色
    cities = []
    scale = 0.008  # 保证气泡的大小合适

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        city_map_info_sub = city_map_info[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon=city_map_info_sub['Longitude'],
            lat=city_map_info_sub['Latitude'],
            text=city_map_info_sub['text'],
            marker=dict(
                size=city_map_info_sub['Success Index']/scale,  # 气泡大小与成功指数正相关
                color=colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode='area'
            ),
            name='{0} - {1}'.format(lim[0], lim[1])))

    fig.update_layout(
        title_text='US city success indexes<br>(Click legend to toggle traces)',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='rgb(217, 217, 217)',
        )
    )

    # 将气泡图导出为html文件
    fig.write_html(fig_path)


if __name__ == "__main__":
    dataset_paths = ['dataset/team_data.csv', 'dataset/selected_city_data.csv', 'dataset/all_city_data.csv']

    fig_paths = ['result/team_success_index_wordcloud.png', 'result/team_number_wordcloud.png',
                 'result/city_success_index_wordcloud.png']

    html_paths = ['result/team_number_map.html', 'result/success_index_map.html']

    plot_team_success_index_wordcloud(dataset_paths[0], fig_paths[0])
    print("Fig 'team_success_index_wordcloud.png' has been plotted.")

    plot_team_number_wordcloud(dataset_paths[1], fig_paths[1])
    print("Fig 'team_number_wordcloud.png' has been plotted.")

    plot_city_success_index_wordcloud(dataset_paths[1], fig_paths[2])
    print("Fig 'city_success_index_wordcloud.png' has been plotted.")

    '''
    plot_team_number_map(dataset_paths[1], html_paths[0])

    plot_city_success_index_map(dataset_paths[1], html_paths[1])
    '''
