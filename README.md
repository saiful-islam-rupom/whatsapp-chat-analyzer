![Banner](images/banner.jpg)
# WhatsApp Chat Analyzer
**Live App**: [Click to Try the App](https://saiful-islam-rupom-whatsapp-chat-analyzer.streamlit.app/)
(Make sure Desktop-site is Turned-on for better user experience.)

## Project Overview
A data analysis-based web application built with Streamlit that enables users to explore and visualize their WhatsApp chat history in detail. The tool provides interactive statistics, timelines, activity heatmaps, most common words, emoji usage, and other different informations to give users meaningful insights into their personal or group conversations.

## Objective
The objective of this project is to build an interactive web app that helps WhatsApp users analyze their chats, uncover messaging patterns, and visualize engagement. By leveraging data analysis and visualization techniques in Python, this project transforms raw .txt WhatsApp exports into an easy-to-understand analytical dashboard.

## Project Features
- **Quick Stats**
-- Get instant metrics such as total messages, word count, media shared, and links.
- **Timelines**
- **Activity Maps**
- **Most Active Users**
- **WordCloud & Most Common Words**
- **Emoji Analysis**
- **User-level & Group-level Analysis**

## Project Workflow
This project follows a structured workflow combining data preprocessing, machine learning, natural language processing (NLP), vector similarity modeling, API integration, and frontend deployment using Streamlit.

### 1. Data Collection & Preprocessing
- The datasets are collected from online source- MovieLens where two million tag applications applied to 87,585 movies by 200,948 users. (Collected 10/2023 Released 05/2024)
- There are three datasets- 'movies.csv', 'tags.csv' & 'links.csv' containing movie metadata was including: movieId, title, genres, tags, imdbId, tmdbId etc.
- These datasets were cleaned and merged into a single dataset
- Basic NLP techniques were applied to normalize the text.

### 2. Natural Language Processing with NLTK
The Natural Language Toolkit (NLTK) was used for:
- Text normalization (e.g., converting to lowercase)
- Stopword removal — removing common non-informative words like “the”, “and”, “in”
- Stemming — reducing words to their root form using PorterStemmer (e.g., "playing" → "play")
This step ensures better vector representation by eliminating noise from the textual data.

### 3. Feature Extraction with CountVectorizer
- CountVectorizer was applied to the processed tags column to convert it into a numerical vector space.
- Resulting vectors were integer counts of keywords for each movie.
- To optimize deployment, these vectors were converted to float32 to reduce memory usage. (With 0% data loss)

### 4. Model Training using Nearest Neighbors
- A K-Nearest Neighbors (KNN) model was trained using cosine similarity to find movies with similar feature vectors.
- The model computes the top 5 most similar movies based on content.
- Trained model was saved using joblib with compression (compress=3) for efficient deployment.

### 5. Model Serialization
Serialized artifacts:
- df.pkl: Preprocessed movie dataframe with TMDb IDs
- cv.pkl: Fitted CountVectorizer object
- nn_model_compressed.pkl: Compressed trained Nearest Neighbors model

### 6. Frontend Web App with Streamlit
A Streamlit web app was developed to:
- Let users select any movie
- Show movie poster, description, and top actors
- Display clickable recommendations
- Auto-refresh and update the page on new selections

### 7. TMDb API Integration
The app fetches:
- Posters
- Descriptions
- Actor names and profile images
All using the TMDb API key.

### 8. Model Optimization for Deployment
Original 0.47GB model was reduced to 2.7 MB (With 0% data loss) by:
- Using float32 instead of float64 or int64
- Compressing with joblib
This ensures fast loading on free-tier cloud platforms.

### 9. Deployment on Streamlit Cloud
- All code and assets pushed to GitHub
- App deployed at no cost using Streamlit Community Cloud
- App is fully public, fast, and ready for user interaction

## App Snapshot
![Snapshot](images/snapshot.jpg)

## Future Enhancements
- Add collaborative filtering using user ratings and behavior
- Introduce user profiles for real-time personalized recommendations
- Replace static dataset with real-time updates from TMDb API
- Build a hybrid model combining content-based + collaborative filtering
- Incorporate movie popularity and ratings into recommendation ranking
- Support multiple languages and regional content via TMDb internationalization
- Implement fuzzy search and autocomplete for better movie selection
- Allow filtering of recommendations by genre or mood
- Enable filtering of movies by specific actors
- Improve UI/UX with loading animations and mobile responsiveness
- Deploy as a scalable REST API using FastAPI or Flask + React frontend

## License
This project is licensed under the [MIT License](LICENSE)

## Author
[Saiful Islam Rupom](https://www.linkedin.com/in/saiful-islam-rupom/); Email: saifulislam558855@gmail.com
