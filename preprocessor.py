import re
import pandas as pd

def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}(?:\u202F|\u00A0| )?(?:am|pm) - '
    messages = re.split(pattern,data)[1:]

    def clean_m():
        cleaned = [d.replace("\u202f", " ").replace("\u00A0", " ").strip() for d in messages]
        return cleaned
    clean_messages = clean_m()

    dates = re.findall(pattern,data)

    def clean_d():
        cleaned = [d.replace("\u202f", " ").replace("\u00A0", " ").strip() for d in dates]
        return cleaned
    clean_dates = clean_d()

    df = pd.DataFrame({'user_message':clean_messages, 'message_date':clean_dates})

    df['message_date'] = df['message_date'].str.replace(r'\s*-\s*$', '', regex=True)
    df['message_date'] = pd.to_datetime(
    df['message_date'].str.replace(r'\s*-\s*$', '', regex=True),
    format='%m/%d/%y, %I:%M %p'
    )

    df.rename(columns={'message_date': 'date'}, inplace= True)
    df['date'] = df['date'].dt.strftime(r'%m/%d/%y, %I:%M %p')

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'^(.*?):\s', message, maxsplit=1)
        if len(entry) >= 3:  
            users.append(entry[1])     
            messages.append(entry[2])  
        else:  
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages

    df.drop(columns=['user_message'], inplace= True)

    df['date'] = pd.to_datetime(df['date'],format='%m/%d/%y, %I:%M %p')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    return df
