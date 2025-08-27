import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")
st.sidebar.markdown("Developed by  \n[**Saiful Islam Rupom**](https://www.linkedin.com/in/saiful-islam-rupom/)")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)

    # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort(reverse=True)
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis with respect to:",user_list)

    if st.sidebar.button("Show Analysis"):
        # Stats area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user,df)
        st.title("Quick Stats")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Messages", num_messages)
        with col2:
            st.metric("Total Words", words)
        with col3:
            st.metric("Total Media Shared", num_media_messages)
        with col4:
            st.metric("Total Links Shared", num_links)

        # monthly timeline
        st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user,df)
        fig,ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message_count'], color='green')
        ax.set_xlabel("Months")
        ax.set_ylabel("Number of Messages")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        ax.set_ylabel("Message Count")
        st.pyplot(fig)

        # activity map
        st.title('Activity Map')
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values,color='purple')
            plt.xticks(rotation='vertical')
            ax.set_ylabel("Total Message Count")
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values,color='orange')
            plt.xticks(rotation='vertical')
            ax.set_ylabel("Total Message Count")
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user,df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)

        # finding the busiest users in the group(group level)
        if selected_user == 'Overall':
            st.title('Most Active Users')
            x,new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                ax.set_xlabel("Users")
                ax.set_ylabel("Total Message Count")
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df.rename(columns={'percent': 'Person', 'count': 'Percentage'}))

        # wordCloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user,df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()
        ax.barh(most_common_df[0][::-1], most_common_df[1][::-1])
        ax.set_xlabel("Count")
        plt.xticks(rotation='vertical')
        st.title('Most common words')
        st.pyplot(fig)

        # emoji analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)

        with col2:
            plt.rcParams['font.family'] = 'Noto Color Emoji'  # works for linux
            fig, ax = plt.subplots()
            ax.pie(
                emoji_df["Count"].head(10),
                labels=emoji_df["Emoji"].head(10),
                autopct=lambda p: f"{p:.1f}%"
            )
            ax.set_title("Percentages of Top 10 used Emojies")
            st.pyplot(fig)

        st.title("Thank you for exploring your chats with this tool.")
    else:
        st.title('Select "Overall" to see group level analysis (or choose a user to see analysis for the individual) and press "Show Analysis" button.')
else:
    st.title("Hi there! Please browse and upload you whatsapp chat(.txt file)")

