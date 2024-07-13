'''我的主页'''
import streamlit as st
import time
from PIL import Image


page = st.sidebar.radio('我的首页', ['对比False', '对比True', '对齐False', '对齐True','亲疏False','亲疏True','重复False','重复True'])

def page_1():
    '''阿短的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        # 输出查询的单词内容
        cixing, ciyi = words_dict[word][1].split('.')
        st.write('单词的意思是：', ciyi)
        st.write('单词的词性是：' + cixing + '.')
        st.write('这是词典中的第' + str(words_dict[word][0]) + '个单词')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('单词被查询次数为：' + str(times_dict[n]))
def page_2():
    '''阿短的智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        # 输出查询的单词内容
        cixing, ciyi = words_dict[word][1].split('.')
        st.markdown(f'##### 中文意思：:blue[{ciyi}]')
        st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.text('单词被查询次数为：' + str(times_dict[n]))
def page_3():
    '''阿短的兴趣推荐'''
    st.subheader(':blue[阿短的世界之旅]')
    st.write('我在各种假期中可没闲着，而是在世界各地留下自己的足迹，如果你也喜欢游览名胜古迹、到网红点打卡、亲近大自然……那么就来看看我的丰富流程，参考一下吧！')
    st.write('')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.image('去海边游泳.png')
        st.write('去海边游泳')
        st.write('在海边游泳和在游泳池游泳感觉完全不同，海面有波浪，脚下是软软的沙子，在水里什么都看不清，而且，海水咸得发苦，别问我是怎么知道的……')
    with col2:
        st.image('去森林里露营.png')
        st.write('去森林里露营')
        st.write('森林里的夏天真的出乎意料的凉爽，甚至晚上还得加衣服，和家人们一起来顿野炊也是别有一番风味，即使是蚊虫的骚扰也无法赶走好心情！~')
    with col3:
        st.image('去沙漠看金字塔.png')
        st.write('去沙漠看金字塔')
        st.write('沙漠的白天非常热，但是当地人都把自己裹得严严实实，我们在这里看到了金字塔，比想象中要大得多，真实太壮观了！')
    with col4:
        st.image('去雪山上滑雪.png')
        st.write('去雪山上滑雪')
        st.write('装备多到好半天才能穿上，飞吹在脸上就像刀割，人摔在雪上也非常狼狈，但当你掌握了技巧你会发现这一切都是值得的，太刺激了！')
def page_4():
    '''阿短的兴趣推荐'''
    st.subheader(':blue[阿短的世界之旅]')
    st.write('我在各种假期中可没闲着，而是在世界各地留下自己的足迹，如果你也喜欢游览名胜古迹、到网红点打卡、亲近大自然……那么就来看看我的丰富流程，参考一下吧！')
    st.write('')
    
    # 图片处理
    imgs_name_lst = ['去海边游泳.png', '去森林里露营.png', '去沙漠看金字塔.png', '去雪山上滑雪.png']
    imgs_lst = []
    for i in imgs_name_lst:
        img = Image.open(i)
        img = img.resize((400, 300))
        imgs_lst.append(img)
    
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.image(imgs_lst[0])
        st.markdown('##### 去海边游泳')
        st.write('在海边游泳和在游泳池游泳感觉完全不同，海面有波浪，脚下是软软的沙子，在水里什么都看不清，而且，海水咸得发苦，别问我是怎么知道的……')
    with col2:
        st.image(imgs_lst[1])
        st.markdown('##### 去森林里露营')
        st.write('森林里的夏天真的出乎意料的凉爽，甚至晚上还得加衣服，和家人们一起来顿野炊也是别有一番风味，即使是蚊虫的骚扰也无法赶走好心情！~')
    with col3:
        st.image(imgs_lst[2])
        st.markdown('##### 去沙漠看金字塔')
        st.write('沙漠的白天非常热，但是当地人都把自己裹得严严实实，我们在这里看到了金字塔，比想象中要大得多，真实太壮观了！')
    with col4:
        st.image(imgs_lst[3])
        st.markdown('##### 去雪山上滑雪')
        st.write('装备多到好半天才能穿上，飞吹在脸上就像刀割，人摔在雪上也非常狼狈，但当你掌握了技巧你会发现这一切都是值得的，太刺激了！')
def page_5():
    '''阿短的互联网知识科普'''
    st.write('阿短的互联网知识科普大讲堂')
    st.write('先来做两个测试题吧，看看你对互联网了解多少')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    col1_1, col1_2, col1_3, col1_4 = st.columns([1, 1, 1, 1])
    with col1_1:
        cb1_1 = st.checkbox('易于管理')
    with col1_2:
        cb1_2 = st.checkbox('效率高')
    with col1_3:
        cb1_3 = st.checkbox('网速快')
    with col1_4:
        cb1_4 = st.checkbox('安全性好')

    st.write('你了解吗：可以通过哪些地址找到一个网站？')
    col2_1, col2_2, col2_3, col2_4 = st.columns([1, 1, 1, 1])
    with col2_1:
        cb2_1 = st.checkbox('IPv4地址')
    with col2_2:
        cb2_2 = st.checkbox('IPv6地址')
    with col2_3:
        cb2_3 = st.checkbox('域名地址')
    with col2_4:
        cb2_4 = st.checkbox('经纬度地址')
def page_6():
    '''阿短的互联网知识科普'''
    st.write('阿短的互联网知识科普大讲堂')
    st.write('先来做两个测试题吧，看看你对互联网了解多少')
    st.write('')
    st.write('')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    col1_1, col1_2, col1_3, col1_4 = st.columns([1, 1, 1, 1])
    with col1_1:
        cb1_1 = st.checkbox('易于管理')
    with col1_2:
        cb1_2 = st.checkbox('效率高')
    with col1_3:
        cb1_3 = st.checkbox('网速快')
    with col1_4:
        cb1_4 = st.checkbox('安全性好')
    st.write('')
    st.write('')
    st.write('你了解吗：可以通过哪些地址找到一个网站？')
    col2_1, col2_2, col2_3, col2_4 = st.columns([1, 1, 1, 1])
    with col2_1:
        cb2_1 = st.checkbox('IPv4地址')
    with col2_2:
        cb2_2 = st.checkbox('IPv6地址')
    with col2_3:
        cb2_3 = st.checkbox('域名地址')
    with col2_4:
        cb2_4 = st.checkbox('经纬度地址')
def page_7():
    '''阿短的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 显示图片处理界面
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.checkbox('增强对比度')
            bw = st.button('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)
def page_8():
    '''阿短的图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # 显示图片处理界面
        col1, col2, col3 = st.columns([3, 2, 4])
        with col1:
            st.image(img)
        with col2:
            ch = st.toggle('反色滤镜')
            co = st.toggle('增强对比度')
            bw = st.toggle('黑白滤镜')
        with col3:
            st.write('对图片进行反色处理')
            st.write('让图片颜色更加鲜艳')
            st.write('将图片变为灰度图')
        # 点击按钮处理图片
        b = st.button('开始处理')
        if b:
            if ch:
                img = img_change_ch(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键"另存为"保存图片')
            st.image(img)
            
#'''-------------功能函数区------------'''
def img_change_ch(img):
    '''图片反色滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值，反色处理
            r = 255 - img_array[x, y][0]
            g = 255 - img_array[x, y][1]
            b = 255 - img_array[x, y][2]
            img_array[x, y] = (r, g, b)
    return img

def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img
    
if page == '对比False':
    page_1()
elif page == '对比True':
    page_2()
elif page == '对齐False':
    page_3()
elif page == '对齐True':
    page_4()
elif page == '亲疏False':
    page_5()
elif page == '亲疏True':
    page_6()
elif page == '重复False':
    page_7()
elif page == '重复True':
    page_8()
