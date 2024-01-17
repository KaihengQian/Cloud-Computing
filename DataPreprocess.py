import os
import pandas as pd
import numpy as np


# 初始化
def initialize():
    current_directory = os.getcwd()

    folder_name1 = "dataset"
    folder_path1 = os.path.join(current_directory, folder_name1)
    if not os.path.exists(folder_path1):
        os.mkdir(folder_path1)
    else:
        print(f"Folder {folder_name1} has existed.")

    folder_name2 = "result"
    folder_path2 = os.path.join(current_directory, folder_name2)
    if not os.path.exists(folder_path2):
        os.mkdir(folder_path2)
    else:
        print(f"Folder {folder_name2} has existed.")


# 获取球队的部分属性信息
def get_team_data():
    # 所在城市
    cities = ['Dallas', 'Orlando', 'San Antonio', 'Denver', 'New York', 'Washington', 'Oakland', 'Los Angeles',
              'Los Angeles', 'Memphis', 'Milwaukee', 'Phoenix', 'Miami', 'Indianapolis', 'Sacramento', 'Detroit',
              'New York', 'Portland', 'Oklahoma City', 'Cleveland', 'New Orleans', 'Charlotte', 'Atlanta',
              'Minneapolis', 'Boston', 'Houston', 'Chicago', 'Salt Lake City', 'Philadelphia', 'Oakland', 'Kansas City',
              'Dallas', 'Charlotte', 'New Orleans', 'Denver', 'Washington', 'Cleveland', 'Detroit', 'Quincy',
              'Miami Gardens', 'Pittsburgh', 'Buffalo', 'Green Bay', 'Santa Clara', 'Philadelphia', 'Indianapolis',
              'Seattle', 'Baltimore', 'Atlanta', 'Newark', 'Newark', 'Nashville', 'Houston', 'Cincinnati', 'Tampa',
              'Inglewood', 'Inglewood', 'Chicago', 'Glendale', 'Jacksonville', 'Minneapolis', 'Tampa', 'Dallas',
              'Denver', 'Nashville', 'Washington', 'Seattle', 'Los Angeles', 'St. Louis', 'Davie', 'Tempe', 'Anaheim',
              'Buffalo', 'Detroit', 'New York', 'Columbus', 'Raleigh', 'Pittsburgh', 'Newark', 'San Jose', 'Boston',
              'Las Vegas', 'New York', 'Chicago', 'Philadelphia', 'Minneapolis', 'Milwaukee', 'Anaheim', 'St. Louis',
              'Phoenix', 'New York', 'Philadelphia', 'Detroit', 'Denver', 'Los Angeles', 'Boston', 'Arlington',
              'Cincinnati', 'Chicago', 'Kansas City', 'Miami', 'Houston', 'Washington', 'Oakland', 'San Francisco',
              'Baltimore', 'San Diego', 'Pittsburgh', 'Cleveland', 'Seattle', 'Minneapolis', 'Tampa', 'Atlanta',
              'Chicago', 'New York', 'Minneapolis', 'Washington', 'Los Angeles', 'Kansas City', 'Denver', 'Long Beach',
              'Orlando', 'Quincy', 'Columbus', 'Seattle', 'Atlanta', 'San Jose', 'Houston', 'Portland', 'Newark',
              'West Jordan', 'Chicago', 'Philadelphia', 'Frisco', 'Cincinnati', 'New York']

    # 冠军数量
    titles = [1, 0, 5, 0, 0, 1, 4, 0, 12, 0, 2, 0, 3, 0, 1, 3, 2, 1, 0, 1, 0, 0, 1, 0, 17, 2, 6, 0, 3, 3, 2, 5, 0, 1, 3,
              3, 0, 0, 6, 2, 6, 0, 4, 5, 1, 2, 1, 2, 0, 4, 1, 0, 0, 0, 2, 1, 0, 1, 0, 0, 0, 3, 1, 2, 0, 1, 0, 2, 1, 0,
              0, 1, 0, 11, 4, 0, 1, 5, 3, 0, 6, 0, 4, 6, 2, 0, 0, 1, 11, 1, 2, 2, 4, 0, 7, 9, 0, 5, 3, 2, 2, 1, 1, 9, 8,
              3, 0, 5, 2, 0, 3, 0, 4, 3, 27, 0, 4, 0, 2, 1, 5, 0, 0, 2, 2, 1, 2, 2, 1, 0, 1, 1, 0, 0, 0, 0]

    team_values = [2670, 1690, 2050, 1740, 2660, 1990, 4470, 3060, 5550, 1530, 1960, 1900, 2490, 1800, 1880, 1740, 5450,
                   1990, 1670, 1750, 1510, 1600, 1830, 1550, 3410, 2790, 3450, 1690, 2520, 3180, 3080, 6470, 2730, 2820,
                   3800, 4030, 2730, 2440, 4650, 3320, 3570, 2500, 3470, 4220, 3870, 2830, 3600, 3100, 3250, 4630, 4080,
                   2680, 3840, 2400, 2800, 3960, 3000, 4000, 2690, 2650, 3120, 805, 825, 640, 680, 940, 860, 990, 710,
                   520, 410, 690, 600, 960, 1400, 525, 545, 845, 750, 705, 940, 835, 865, 1220, 910, 785, 1.43, 2.11,
                   2.335, 1.36, 2.68, 2.375, 1.45, 1.415, 4.11, 3.89, 1.89, 1.365, 1.715, 1.175, 1, 2.38, 2.16, 1.34,
                   3.34, 1.49, 1.745, 1.3, 1.385, 1.66, 1.59, 1.185, 2.27, 3.82, 5.89, 520, 630, 860, 550, 370, 835,
                   400, 480, 540, 705, 845, 510, 425, 635, 505, 420, 535, 530, 415, 500, 655]

    annual_revenues = [296, 228, 279, 226, 283, 247, 434, 297, 418, 213, 252, 231, 283, 228, 275, 252, 428, 258, 251,
                       256, 213, 227, 236, 218, 308, 344, 304, 251, 284, 386, 491, 871, 478, 484, 496, 561, 449, 407,
                       611, 495, 486, 420, 500, 580, 536, 435, 493, 487, 521, 592, 549, 425, 556, 404, 429, 424, 390,
                       516, 422, 455, 489, 132, 152, 123, 138, 180, 170, 214, 134, 104, 97, 135, 125, 195, 229, 108,
                       116, 157, 159, 133, 186, 156, 94, 191, 184, 144, 286, 364, 388, 266, 394, 396, 259, 283, 555,
                       492, 341, 263, 255, 245, 218, 441, 376, 220, 434, 247, 314, 249, 267, 281, 289, 253, 406, 516,
                       702, 41, 53, 82, 45, 27, 80, 40, 36, 23, 67, 105, 36, 30, 59, 43, 33, 27, 37, 40, 32, 51]

    return cities, titles, team_values, annual_revenues


# 对Titles、Team Value、Annual Revenue列计算各球队占比
def calculate_proportion(data, column_name):
    leagues = ['NBA', 'NFL', 'NHL', 'MLB', 'MLS']
    column_proportion = []

    for league in leagues:
        league_team = data.loc[data['League'] == league]  # 筛选出所有属于该联盟的球队的数据
        league_column = (league_team[column_name].to_numpy()).T
        league_column_sum = np.sum(league_column)  # 对指定列求和
        league_column_proportion = league_column / league_column_sum * 100  # 将指定列除以求得的总和得到各球队占比，并将单位转换为百分比
        column_proportion.append(league_column_proportion)

    result = np.concatenate(column_proportion, axis=0)
    return result


# 制作球队信息数据集
def create_team_dataset(raw_dataset_path, dataset_path):
    # 读取US_teams.csv文件内容
    team_data = pd.read_csv(raw_dataset_path)

    # 取US_teams.csv文件的Team、League列，剔除其他列
    del team_data['Division']
    del team_data['Lat']
    del team_data['Long']

    # 剔除Team列中位于Canada的球队的所在行
    team_data.drop(labels=20, inplace=True)  # Toronto Raptors
    team_data.drop(labels=65, inplace=True)  # Montreal Canadiens
    team_data.drop(labels=67, inplace=True)  # Winnipeg Jets
    team_data.drop(labels=68, inplace=True)  # Ottawa Senators
    team_data.drop(labels=83, inplace=True)  # Vancouver Canucks
    team_data.drop(labels=84, inplace=True)  # Edmonton Oilers
    team_data.drop(labels=86, inplace=True)  # Toronto Maple Leafs
    team_data.drop(labels=87, inplace=True)  # Calgary Flames
    team_data.drop(labels=117, inplace=True)  # Toronto Blue Jays
    team_data.drop(labels=127, inplace=True)  # Vancouver Whitecaps FC
    team_data.drop(labels=128, inplace=True)  # Toronto FC
    team_data.drop(labels=145, inplace=True)  # CF Montréal

    # 剔除Team列中缺乏有关数据的新成立球队的所在行
    team_data.drop(labels=132, inplace=True)  # Inter Miami CF
    team_data.drop(labels=138, inplace=True)  # Nashville SC
    team_data.drop(labels=142, inplace=True)  # Austin FC
    team_data = team_data.reset_index(drop=True)

    # 更正部分球队名的拼写错误
    team_data.loc[14, 'Team'] = 'Sacramento Kings'
    team_data.loc[30, 'Team'] = 'Kansas City Chiefs'
    team_data.loc[69, 'Team'] = 'Florida Panthers'
    team_data.loc[84, 'Team'] = 'Philadelphia Flyers'
    team_data.loc[108, 'Team'] = 'Cleveland Guardians'

    cities, titles, team_values, annual_revenues = get_team_data()

    # 添加City（所在城市）列
    team_data['City'] = cities

    # 添加Titles（冠军数量）列
    team_data['Titles'] = titles
    team_data['Titles'] = team_data['Titles'].astype('float')

    # 添加Proportion(Titles)（在所属联盟总冠军数量中占据的比例）列
    titles_proportion = calculate_proportion(team_data, 'Titles')
    team_data['Proportion(Titles)'] = titles_proportion

    # 添加Team Value（市值）列
    team_data['Team Value'] = team_values
    team_data['Team Value'] = team_data['Team Value'].astype('float')

    # 添加Proportion(Team Value)（在总队伍市值中占据的比例）列
    team_value_proportion = calculate_proportion(team_data, 'Team Value')
    team_data['Proportion(Team Value)'] = team_value_proportion

    # 添加Annual Revenue（年营销收入）列
    team_data['Annual Revenue'] = annual_revenues
    team_data['Annual Revenue'] = team_data['Annual Revenue'].astype('float')

    # 添加Proportion(Annual Revenue)（在总队伍年营销收入中占据的比例）列
    annual_revenue_proportion = calculate_proportion(team_data, 'Annual Revenue')
    team_data['Proportion(Annual Revenue)'] = annual_revenue_proportion

    # 添加Success Index（成功指数）列
    # 由问卷调查结果得到三个因素各自所占比重
    weight_titles = 0.4595
    weight_team_value = 0.3181
    weight_annual_revenue = 0.2224
    team_data['Success Index'] = (weight_titles * team_data['Proportion(Titles)'] +
                                  weight_team_value * team_data['Proportion(Team Value)'] +
                                  weight_annual_revenue * team_data['Proportion(Annual Revenue)'])

    # 保存为team_data.csv
    team_data.to_csv(dataset_path, index=False)


# 制作特定城市（至少拥有一支球队）信息数据集
def create_selected_city_dataset(raw_dataset_path, dataset_path):
    # 读取team_data.csv文件内容
    team_data = pd.read_csv(raw_dataset_path[-1])

    # 取team_data的City列，经过去重得到selected_city_data的City列
    selected_city_data = (team_data['City']).to_frame()
    selected_city_data = selected_city_data.drop_duplicates()
    selected_city_data = selected_city_data.reset_index(drop=True)

    # 读取US_2020_census_by_city_density.csv文件内容
    census_by_city_density = pd.read_csv(raw_dataset_path[2])

    # 更正部分数据
    selected_city_data.loc[(selected_city_data['City'] == 'Davie'), 'City'] = 'Davie[ad]'

    # 从census_by_city_density的state列、pop_density_km列中，取selected_city_data的City列中的城市的对应数据，
    # 得到selected_city_data的State列、City Population Density列
    flag = 0
    city_info = None
    for index, row in selected_city_data.iterrows():
        city = row['City']
        temp_city_info = census_by_city_density[(census_by_city_density['city'] == city)]
        if flag == 0:
            city_info = temp_city_info
            flag = 1
        else:
            city_info = pd.concat([city_info, temp_city_info])
            city_info = city_info.reset_index(drop=True)

    # 更正部分数据
    city_info = city_info.drop(city_info[(city_info['city'] == 'Kansas City') & (city_info['state'] == 'Kansas')].index)
    city_info = city_info.drop(city_info[(city_info['city'] == 'Glendale') & (city_info['state'] == 'California')].index)
    city_info = city_info.drop(city_info[(city_info['city'] == 'Columbus') & (city_info['state'] == 'Georgia')].index)
    city_info = city_info.reset_index(drop=True)

    selected_city_data['State'] = city_info['state']
    selected_city_data['City Population Density'] = city_info['pop_density_km']
    selected_city_data['City Population Density'] = selected_city_data['City Population Density'].astype('float')

    # 读取US_2020_census_by_state.csv文件内容
    census_by_state = pd.read_csv(raw_dataset_path[4])

    # 更正部分数据
    selected_city_data.loc[(selected_city_data['City'] == 'Washington'), 'State'] = 'DC'

    # 从census_by_state的state_code列、2020_census列中，取selected_city_data的State列中的州的对应数据，
    # 得到selected_city_data的State Code列、State Population列
    flag = 0
    state_info = None
    for index, row in selected_city_data.iterrows():
        state = row['State']
        temp_state_info = census_by_state[(census_by_state['state'] == state)]
        if flag == 0:
            state_info = temp_state_info
            flag = 1
        else:
            state_info = pd.concat([state_info, temp_state_info])
            state_info = state_info.reset_index(drop=True)

    selected_city_data['State Code'] = state_info['state_code']
    selected_city_data['State Population'] = state_info['2020_census']
    selected_city_data['State Population'] = selected_city_data['State Population'].astype('float')

    # 读取US_2020_census_by_city_location.csv文件内容
    census_by_city_location = pd.read_csv(raw_dataset_path[3])

    # 更正部分数据
    selected_city_data.loc[(selected_city_data['City'] == 'Davie[ad]'), 'City'] = 'Davie'
    selected_city_data.loc[(selected_city_data['City'] == 'St. Louis'), 'City'] = 'St Louis'

    # 从census_by_city_location的Longitude列、Latitude列、Population列中，取selected_city_data的City列中的城市的对应数据，
    # 得到selected_city_data的Longitude列、Latitude列、City Population列
    flag = 0
    city_info = None
    for index, row in selected_city_data.iterrows():
        city = row['City']
        state_code = row['State Code']
        temp_city_info = census_by_city_location[(census_by_city_location['City'] == city) & (census_by_city_location['State'] == state_code)]
        if flag == 0:
            city_info = temp_city_info
            flag = 1
        else:
            city_info = pd.concat([city_info, temp_city_info])
            city_info = city_info.reset_index(drop=True)

    selected_city_data['Longitude'] = city_info['Longitude']
    selected_city_data['Longitude'] = selected_city_data['Longitude'].astype('float')
    selected_city_data['Latitude'] = city_info['Latitude']
    selected_city_data['Latitude'] = selected_city_data['Latitude'].astype('float')
    selected_city_data['City Population'] = city_info['Population']
    selected_city_data['City Population'] = selected_city_data['City Population'].astype('float')

    # 读取US_2019_GDP_by_state.csv文件内容
    GDP_by_state = pd.read_csv(raw_dataset_path[1])

    # 更正部分数据
    selected_city_data.loc[(selected_city_data['City'] == 'Washington'), 'State'] = 'District of Columbia'
    selected_city_data.loc[(selected_city_data['City'] == 'St Louis'), 'City'] = 'St. Louis'

    # 从GDP_by_state的2019列中，取selected_city_data的State列中的州的对应数据，
    # 得到selected_city_data的State GDP列
    flag = 0
    state_info = None
    for index, row in selected_city_data.iterrows():
        state = row['State']
        temp_state_info = GDP_by_state[(GDP_by_state['GeoName'] == state) & (GDP_by_state['LineCode'] == 1)]
        if flag == 0:
            state_info = temp_state_info
            flag = 1
        else:
            state_info = pd.concat([state_info, temp_state_info])
            state_info = state_info.reset_index(drop=True)

    selected_city_data['State GDP'] = state_info['2019']
    selected_city_data['State GDP'] = selected_city_data['State GDP'].astype('float')

    # 利用selected_city_data的City Population列除以State Population列，得到Population Proportion(City in State)列，并将单位转换为百分比
    selected_city_data['Population Proportion(City in State)'] = (
            selected_city_data['City Population'] / selected_city_data['State Population'] * 100)

    # 利用selected_city_data的State GDP列除以State Population列，得到State GDP Per Capita列，并将单位由百万美元转换为千美元
    selected_city_data['State GDP Per Capita'] = (
            selected_city_data['State GDP'] / selected_city_data['State Population'] * 1000)

    # 重排列索引
    selected_city_data = selected_city_data.reindex(
        columns=['City', 'State', 'State Code', 'Longitude', 'Latitude', 'City Population Density', 'City Population',
                 'State Population', 'Population Proportion(City in State)', 'State GDP', 'State GDP Per Capita'])

    # 添加NBA Team（NBA球队数）列、NFL Team（NFL球队数）列、NHL Team（NHL球队数）列、MLB Team（MLB球队数）列、MLS Team（MLS球队数）列、
    # Team Number（五大联盟球队总数）列、Success Index列
    nba_team = []
    nfl_team = []
    nhl_team = []
    mlb_team = []
    mls_team = []
    total_team = []
    success_index = []
    for row in selected_city_data.itertuples():
        city = getattr(row, 'City')
        city_info = team_data[team_data['City'] == city]

        sum_index = 0
        num_nba_team = 0
        num_nfl_team = 0
        num_nhl_team = 0
        num_mlb_team = 0
        num_mls_team = 0

        for index, r in city_info.iterrows():
            team_index = r['Success Index']
            sum_index += team_index
            if r['League'] == 'NBA':
                num_nba_team += 1
            elif r['League'] == 'NFL':
                num_nfl_team += 1
            if r['League'] == 'NHL':
                num_nhl_team += 1
            if r['League'] == 'MLB':
                num_mlb_team += 1
            if r['League'] == 'MLS':
                num_mls_team += 1

        nba_team.append(num_nba_team)
        nfl_team.append(num_nfl_team)
        nhl_team.append(num_nhl_team)
        mlb_team.append(num_mlb_team)
        mls_team.append(num_mls_team)
        num_team = num_nba_team + num_nfl_team + num_nhl_team + num_mlb_team + num_mls_team
        total_team.append(num_team)
        city_success_index = sum_index / num_team
        success_index.append(city_success_index)

    selected_city_data['NBA Team'] = nba_team
    selected_city_data['NFL Team'] = nfl_team
    selected_city_data['NHL Team'] = nhl_team
    selected_city_data['MLB Team'] = mlb_team
    selected_city_data['MLS Team'] = mls_team
    selected_city_data['Team Number'] = total_team
    selected_city_data['Success Index'] = success_index

    # 保存为selected_city_data.csv
    selected_city_data.to_csv(dataset_path, index=False)


# 制作所有城市信息数据集
def create_all_city_dataset(raw_dataset_path, dataset_path):
    all_city_data = pd.DataFrame()

    # 读取US_2020_census_by_city_density.csv文件内容
    census_by_city_density = pd.read_csv(raw_dataset_path[2])

    # 取census_by_city_density的city列、state列、pop_density_km列，得到all_city_data的City列、State列、City Population Density列
    all_city_data['City'] = census_by_city_density['city']
    all_city_data['State'] = census_by_city_density['state']
    all_city_data['City Population Density'] = census_by_city_density['pop_density_km']
    all_city_data['City Population Density'] = all_city_data['City Population Density'].astype('float')

    # 读取US_2020_census_by_state.csv文件内容
    census_by_state = pd.read_csv(raw_dataset_path[4])

    # 更正部分数据
    all_city_data.loc[(all_city_data['City'] == 'Washington'), 'State'] = 'DC'

    # 取census_by_state的state_code列、2020_census列，得到all_city_data的State Code列、State Population列
    flag = 0
    state_info = None
    for index, row in all_city_data.iterrows():
        state = row['State']
        temp_state_info = census_by_state[(census_by_state['state'] == state)]
        if flag == 0:
            state_info = temp_state_info
            flag = 1
        else:
            state_info = pd.concat([state_info, temp_state_info])
            state_info = state_info.reset_index(drop=True)

    all_city_data['State Code'] = state_info['state_code']
    all_city_data['State Population'] = state_info['2020_census']
    all_city_data['State Population'] = all_city_data['State Population'].astype('float')

    # 读取US_2020_census_by_city_location.csv文件内容
    census_by_city_location = pd.read_csv(raw_dataset_path[3])

    # 更正部分数据
    all_city_data.loc[(all_city_data['City'] == 'Davie[ad]'), 'City'] = 'Davie'
    all_city_data.loc[(all_city_data['City'] == 'St. Louis'), 'City'] = 'St Louis'
    all_city_data.loc[(all_city_data['City'] == "Lee's Summit"), 'City'] = 'Lees Summit'
    all_city_data.loc[(all_city_data['City'] == 'Jurupa Valley[ae]'), 'City'] = 'Jurupa Valley'
    all_city_data.loc[(all_city_data['City'] == 'Ventura[ab]'), 'City'] = 'Ventura'
    all_city_data.loc[(all_city_data['City'] == 'Winston-Salem'), 'City'] = 'Winston Salem'

    # 取census_by_city_location的Longitude列、Latitude列、Population列，得到all_city_data的Longitude列、Latitude列、City Population列
    # 两份文件中城市排列顺序一致
    all_city_data['Longitude'] = census_by_city_location.loc[0:325, 'Longitude']
    all_city_data['Longitude'] = all_city_data['Longitude'].astype('float')
    all_city_data['Latitude'] = census_by_city_location.loc[0:325, 'Latitude']
    all_city_data['Latitude'] = all_city_data['Latitude'].astype('float')
    all_city_data['City Population'] = census_by_city_location.loc[0:325, 'Population']
    all_city_data['City Population'] = all_city_data['City Population'].astype('float')

    # 读取US_2019_GDP_by_state.csv文件内容
    GDP_by_state = pd.read_csv(raw_dataset_path[1])

    # 更正部分数据
    all_city_data.loc[(all_city_data['City'] == 'Washington'), 'State'] = 'District of Columbia'
    all_city_data.loc[(all_city_data['City'] == 'St Louis'), 'City'] = 'St. Louis'
    all_city_data.loc[(all_city_data['City'] == 'Lees Summit'), 'City'] = "Lee's Summit"
    all_city_data.loc[(all_city_data['City'] == 'Winston Salem'), 'City'] = 'Winston-Salem'

    # 取GDP_by_state的2019列，得到all_city_data的State GDP列
    flag = 0
    state_info = None
    for index, row in all_city_data.iterrows():
        state = row['State']
        temp_state_info = GDP_by_state[(GDP_by_state['GeoName'] == state) & (GDP_by_state['LineCode'] == 1)]
        if flag == 0:
            state_info = temp_state_info
            flag = 1
        else:
            state_info = pd.concat([state_info, temp_state_info])
            state_info = state_info.reset_index(drop=True)
    all_city_data['State GDP'] = state_info['2019']
    all_city_data['State GDP'] = all_city_data['State GDP'].astype('float')

    # 利用all_city_data的City Population列除以State Population列，得到Population Proportion(City in State)列，并将单位转换为百分比
    all_city_data['Population Proportion(City in State)'] = (
            all_city_data['City Population'] / all_city_data['State Population'] * 100)

    # 利用all_city_data的State GDP列除以State Population列，得到State GDP Per Capita列，并将单位由百万美元转换为千美元
    all_city_data['State GDP Per Capita'] = all_city_data['State GDP'] / all_city_data['State Population'] * 1000

    # 重排列索引
    all_city_data = all_city_data.reindex(
        columns=['City', 'State', 'State Code', 'Longitude', 'Latitude', 'City Population Density', 'City Population',
                 'State Population', 'Population Proportion(City in State)', 'State GDP', 'State GDP Per Capita'])

    # 读取selected_city_data.csv文件内容
    selected_city_data = pd.read_csv(raw_dataset_path[-1])

    # 添加NBA Team（NBA球队数）列、NFL Team（NFL球队数）列、NHL Team（NHL球队数）列、MLB Team（MLB球队数）列、MLS Team（MLS球队数）列、Team Number（五大联盟球队总数）列
    all_city_data['NBA Team'] = 0
    all_city_data['NFL Team'] = 0
    all_city_data['NHL Team'] = 0
    all_city_data['MLB Team'] = 0
    all_city_data['MLS Team'] = 0
    all_city_data['Team Number'] = 0
    for index, row in selected_city_data.iterrows():
        city = row['City']
        state_code = row['State Code']
        all_city_data.loc[(all_city_data['City'] == city) & (all_city_data['State Code'] == state_code), 'NBA Team'] = row['NBA Team']
        all_city_data.loc[(all_city_data['City'] == city) & (all_city_data['State Code'] == state_code), 'NFL Team'] = row['NFL Team']
        all_city_data.loc[(all_city_data['City'] == city) & (all_city_data['State Code'] == state_code), 'NHL Team'] = row['NHL Team']
        all_city_data.loc[(all_city_data['City'] == city) & (all_city_data['State Code'] == state_code), 'MLB Team'] = row['MLB Team']
        all_city_data.loc[(all_city_data['City'] == city) & (all_city_data['State Code'] == state_code), 'MLS Team'] = row['MLS Team']
        all_city_data.loc[(all_city_data['City'] == city) & (all_city_data['State Code'] == state_code), 'Team Number'] = row['Team Number']

    # 保存为all_city_data.csv
    all_city_data.to_csv(dataset_path, index=False)


if __name__ == "__main__":
    raw_dataset_paths = ['raw_dataset/US_teams.csv',
                         'raw_dataset/US_2019_GDP_by_state.csv',
                         'raw_dataset/US_2020_census_by_city_density.csv',
                         'raw_dataset/US_2020_census_by_city_location.csv',
                         'raw_dataset/US_2020_census_by_state.csv']

    dataset_paths = ['dataset/team_data.csv', 'dataset/selected_city_data.csv', 'dataset/all_city_data.csv']

    initialize()

    create_team_dataset(raw_dataset_paths[0], dataset_paths[0])
    print("File 'team_data.csv' has been created.")

    create_selected_city_dataset(raw_dataset_paths + [dataset_paths[0]], dataset_paths[1])
    print("File 'selected_city_data.csv' has been created.")

    create_all_city_dataset(raw_dataset_paths + [dataset_paths[1]], dataset_paths[2])
    print("File 'all_city_data.csv' has been created.")
