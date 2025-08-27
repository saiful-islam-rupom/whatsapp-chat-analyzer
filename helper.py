import re
from urlextract import URLExtract
import os
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()

def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch number of messages
    num_messages = df.shape[0]

    # fetch total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]

    # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.strftime("%B")  

    timeline = df.groupby(['year', 'month_num', 'month']).size().reset_index(name='message_count')
    timeline['time'] = timeline['month'] + "-" + timeline['year'].astype(str)
    timeline = timeline.sort_values(['year', 'month_num']).reset_index(drop=True)

    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    if 'only_date' not in df.columns:
        df['only_date'] = pd.to_datetime(df['date']).dt.date  

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    if 'day_name' not in df.columns:
        if 'only_date' in df.columns:
            df['day_name'] = pd.to_datetime(df['only_date']).dt.day_name()
        else:
            df['day_name'] = pd.to_datetime(df['date']).dt.day_name()

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    if 'day_name' not in df.columns:
        df['day_name'] = pd.to_datetime(df['date']).dt.day_name()

    if 'period' not in df.columns:
        df['period'] = pd.to_datetime(df['date']).dt.hour.apply(lambda x: f"{x:02d}-{(x+1)%24:02d}")

    user_heatmap = df.pivot_table(
        index='day_name',
        columns='period',
        values='message',
        aggfunc='count'
    ).fillna(0)

    return user_heatmap

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df

def create_wordcloud(selected_user, df, stopwords_file='stop_hinglish.txt'):
    if os.path.exists(stopwords_file):
        with open(stopwords_file, 'r', encoding='utf-8') as f:
            stop_words = f.read().splitlines()
    else:
        print(f"Warning: {stopwords_file} not found. Proceeding without custom stopwords.")
        stop_words = []

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>']

    def clean_message(msg):
        return re.sub(r'[^A-Za-z ]+', '', msg)   

    def remove_stop_words(message):
        return " ".join([word for word in message.lower().split() if word not in stop_words])

    temp['message'] = temp['message'].apply(clean_message)
    temp['message'] = temp['message'].apply(remove_stop_words)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc

def most_common_words(selected_user,df):
    f = open('stop_words.txt','r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))

    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))),
                            columns=['Emoji', 'Count'])

    return emoji_df
