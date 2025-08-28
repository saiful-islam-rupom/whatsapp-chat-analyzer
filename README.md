![Poster](images/banner.jpg)
# WhatsApp Chat Analyzer
**Live App**: [Click to Try the App](https://saiful-islam-rupom-whatsapp-chat-analyzer.streamlit.app/)

# 📊 WhatsApp Chat Analyzer  

**Live App:** <a href="https://saiful-islam-rupom-whatsapp-chat-analyzer.streamlit.app/" target="_blank">Click to Try the App</a>  




## Project Overview
A data analysis-based web application built with Streamlit that enables users to explore and visualize their WhatsApp chat history in detail. The tool provides interactive statistics, timelines, activity heatmaps, most common words, emoji usage, and other different informations to give users meaningful insights into their personal or group conversations.

## Objective
The objective of this project is to build an interactive web app that helps WhatsApp users analyze their chats, uncover messaging patterns, and visualize engagement. By leveraging data analysis and visualization techniques in Python, this project transforms raw .txt WhatsApp exports into an easy-to-understand analytical dashboard.

## Project Features
- **Quick Stats**
  - Get instant metrics such as total messages, word count, media shared, and links.
- **Timelines**
  - Monthly message activity trend
  - Daily message activity trend
- **Activity Maps**
  - Most busy days of the week
  - Most busy months
  - Weekly activity heatmap
- **Most Active Users**
  - Identify the most active participants in group chats with bar charts and tables.
- **WordCloud & Most Common Words**
  - Generate a wordcloud and bar chart of the most used words in chats.
- **Emoji Analysis**
  - See the most frequently used emojis along with their percentage shares.
- **User-level & Group-level Analysis**
  - Select an individual user for personalized stats or choose “Overall” for group-level insights.

## Project Workflow
### 1. Data Collection
- Exported .txt chat data directly from WhatsApp.
### 2. Data Preprocessing
Using a custom preprocessor.py, chat logs were cleaned and structured into a dataframe:
- Extracted user names, messages, timestamps
- Removed system messages (group_notification)
### 3. Statistical Analysis
- Implemented helper functions (helper.py) to compute metrics such as message counts, word counts, links, and media.
### 4. Visualization
- Matplotlib & Seaborn used for bar charts, timelines, and heatmaps
- WordCloud for generating most frequent word visualization
- Emoji library for emoji extraction and analysis
### 5. Frontend Development
- Streamlit used to build an interactive dashboard
- Sidebar for file upload & user selection
- Main dashboard area for charts, tables, and metrics

## How to Export WhatsApp Chat?
1. Open a WhatsApp chat (individual or group).
2. Tap the three-dot menu → More → Export Chat.
3. Select Without Media.
4. It maybe saved as zip file.
5. Extract the zip file and save it as .txt file to device.
6. Upload it into the app using the sidebar uploader.

## App Snapshot
![Snapshot](images/snapshot.jpg)

## Future Enhancements
- Sentiment analysis of chats (positive/negative/neutral).
- Topic modeling for identifying themes in conversations.
- Network graph visualization of group interactions.
- Export insights as PDF/CSV reports.

## License
This project is licensed under the [MIT License](LICENSE)

## Author
[Saiful Islam Rupom](https://www.linkedin.com/in/saiful-islam-rupom/); Email: saifulislam558855@gmail.com
