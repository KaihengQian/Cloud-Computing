import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from model.model import polynomial_regression_model


# 训练并评估城市当地五大联盟球队成功指数预测模型
def train_model(dataset_path):
    # 读取selected_city_data.csv文件内容
    selected_city_data = pd.read_csv(dataset_path)

    X = np.array(selected_city_data.loc[:, ['Longitude', 'Latitude', 'City Population Density',
                                        'Population Proportion(City in State)', 'State GDP Per Capita']].values)
    y = np.array(selected_city_data.loc[:, ['Success Index']].values)

    # 按照8:2固定比例划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = polynomial_regression_model(X_train, X_test, y_train, y_test)

    return model


# 利用模型预测所有城市的当地五大联盟球队成功指数
def predict_model(model, dataset_path):
    # 读取all_city_data.csv文件内容
    all_city_data = pd.read_csv(dataset_path)

    # 由于Anchorage的predicted success index过偏，对后续的最大最小归一化处理有较大的不良影响，故去除这个城市
    all_city_data.drop(all_city_data[(all_city_data['City'] == 'Anchorage')].index, inplace=True)
    all_city_data = all_city_data.reset_index(drop=True)

    # 添加Predicted Success Index列
    X = np.array(all_city_data.loc[:, ['Longitude', 'Latitude', 'City Population Density',
                                   'Population Proportion(City in State)', 'State GDP Per Capita']].values)
    poly_reg = PolynomialFeatures(degree=3)
    poly_X = poly_reg.fit_transform(X)
    y_pred = model.predict(poly_X)

    # 由于predicted_success_index中含有负数，进行最大最小归一化处理
    min_max_scaler = MinMaxScaler()
    predicted_success_index = min_max_scaler.fit_transform(y_pred)
    all_city_data['Predicted Success Index'] = predicted_success_index * 10
    all_city_data.to_csv(dataset_path, index=False)

    all_city_data = all_city_data.sort_values(by=['Predicted Success Index'], ascending=False)
    all_city_data = all_city_data.reset_index(drop=True)

    # 在还未拥有MLS球队的城市中，查看Miami的排名
    test_1 = all_city_data.drop(all_city_data[(all_city_data['MLS Team'] > 0)].index)
    test_1 = test_1.reset_index(drop=True)
    print("%d/%d" % (test_1[test_1['City'] == 'Miami'].index.tolist()[0] + 1, test_1.shape[0]))
    # 在还未拥有MLS球队且人口超过40万的城市中，查看Miami的排名
    test_2 = test_1.drop(test_1[(test_1['City Population'] < 400000)].index)
    test_2 = test_2.reset_index(drop=True)
    print("%d/%d" % (test_2[test_2['City'] == 'Miami'].index.tolist()[0] + 1, test_2.shape[0]))

    # 在还未拥有NBA球队的城市中，查看Las Vegas的排名
    test_3 = all_city_data.drop(all_city_data[(all_city_data['NBA Team'] > 0)].index)
    test_3 = test_3.reset_index(drop=True)
    print("%d/%d" % (test_3[test_3['City'] == 'Las Vegas'].index.tolist()[0] + 1, test_3.shape[0]))
    # 在还未拥有NBA球队且人口超过40万的城市中，查看Las Vegas的排名
    test_4 = test_3.drop(test_3[(test_3['City Population'] < 400000)].index)
    test_4 = test_4.reset_index(drop=True)
    print("%d/%d" % (test_4[test_4['City'] == 'Las Vegas'].index.tolist()[0] + 1, test_4.shape[0]))

    # 查看排在前五位的城市
    print(all_city_data.head())

    # 查看排在后五位的城市
    print(all_city_data.tail())


# 绘制预测城市成功指数地理分布气泡图
def plot_predicted_city_success_index_map(dataset_path, fig_path):
    # 读取all_city_data.csv文件内容
    all_city_data = pd.read_csv(dataset_path)

    all_city_data = all_city_data.sort_values(by=['Predicted Success Index'], ascending=False)
    all_city_data = all_city_data.reset_index(drop=True)

    predicted_city_map_info = all_city_data[['City', 'Longitude', 'Latitude', 'Predicted Success Index']].copy()
    predicted_city_map_info['text'] = (predicted_city_map_info['City'] + '<br>Predicted Success Index: ' +
                                       (predicted_city_map_info['Predicted Success Index']).astype(str))
    limits = [(0, 3), (3, 12), (12, 52), (52, 117), (117, 210), (210, 325)]  # 根据预测成功指数将城市分类
    colors = ["crimson", "MediumPurple", "royalblue", "lightseagreen", "orange", "lightgrey"]  # 每类一种颜色
    cities = []
    scale = 0.006  # 保证气泡的大小合适

    fig = go.Figure()

    for i in range(len(limits)):
        lim = limits[i]
        predicted_city_map_info_sub = predicted_city_map_info[lim[0]:lim[1]]
        fig.add_trace(go.Scattergeo(
            locationmode='USA-states',
            lon=predicted_city_map_info_sub['Longitude'],
            lat=predicted_city_map_info_sub['Latitude'],
            text=predicted_city_map_info_sub['text'],
            marker=dict(
                size=predicted_city_map_info_sub['Predicted Success Index']/scale,  # 气泡大小与预测成功指数正相关
                color=colors[i],
                line_color='rgb(40,40,40)',
                line_width=0.5,
                sizemode='area'
        ),
        name='{0} - {1}'.format(lim[0], lim[1])))

    fig.update_layout(
        title_text='US city predicted success indexes<br>(Click legend to toggle traces)',
        showlegend=True,
        geo=dict(
            scope='usa',
            landcolor='rgb(217, 217, 217)',
            projection_scale=1
        )
    )

    # 将气泡图导出为html文件
    fig.write_html(fig_path)


# 绘制预测城市成功指数词云图
def plot_predicted_city_success_index_wordcloud(dataset_path, fig_path):
    # 读取all_city_data.csv文件内容
    all_city_data = pd.read_csv(dataset_path)

    all_city_data = all_city_data.drop_duplicates(['City'])  # 存在同名城市，不删除的话无法画出词云图
    all_city_data = all_city_data.reset_index(drop=True)

    predicted_city_wordcloud_info = pd.DataFrame(index=all_city_data['City'])  # 以all_city_data的City列为index新生成一个dataframe
    predicted_city_wordcloud_info['权重'] = 0
    for i in range(0, all_city_data.shape[0]):
        predicted_city_wordcloud_info.iloc[i, 0] = all_city_data.loc[i, 'Predicted Success Index']
    predicted_city_wordcloud_info = predicted_city_wordcloud_info['权重'].sort_values(ascending=False)
    predicted_city_wordcloud_info = dict(predicted_city_wordcloud_info)  # 生成字典形式的数据

    background_Image = np.array(Image.open("picture/usa_map.jpg"))  # 读取背景图片
    img_colors = ImageColorGenerator(background_Image)  # 提取背景图片颜色

    plt.figure(figsize=(10, 8), dpi=1000)  # 创建画板 ,定义图形大小及分辨率
    mask = plt.imread("picture/usa_map.jpg")  # 自定义背景图片
    # 设置词云图相关参数
    predicted_city_wordcloud = WordCloud(mask=mask, width=800, height=500, scale=2, mode="RGBA", background_color='white')
    predicted_city_wordcloud = predicted_city_wordcloud.generate_from_frequencies(predicted_city_wordcloud_info)  # 利用生成的字典形式的数据制作词云图
    predicted_city_wordcloud.recolor(color_func=img_colors)  # 根据图片色设置背景色

    predicted_city_wordcloud.to_file(fig_path)


if __name__ == "__main__":
    dataset_paths = ['dataset/selected_city_data.csv', 'dataset/all_city_data.csv']

    fig_paths = ['result/predicted_city_success_index_wordcloud.png']

    html_paths = ['result/predicted_city_success_index_map.html']

    model = train_model(dataset_paths[0])

    predict_model(model, dataset_paths[1])

    plot_predicted_city_success_index_wordcloud(dataset_paths[1], fig_paths[0])
    print("Fig 'predicted_city_success_index_wordcloud.png' has been plotted.")

    '''
    plot_predicted_city_success_index_map(dataset_paths[1], html_paths[0])
    '''
