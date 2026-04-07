import requests
import pandas as pd
import streamlit as st
import plotly.express as px

# 1. Konfiguracja strony
st.set_page_config(page_title="Analityka API", layout="wide")

# 2. Stylizacja CSS 
st.markdown("""
    <style>
    [data-testid="stMetric"] {
        background-color: #1e2130;
        border: 1px solid #3e445e;
        padding: 15px;
        border-radius: 10px;
    }
    [data-testid="stMetricValue"] { color: #00d4ff !important; }
    [data-testid="stMetricLabel"] { color: #ffffff !important; }
    h1, h2, h3 { color: white; }
    </style>
    """, unsafe_allow_html=True)

# 3. Pobieranie danych
@st.cache_data
def load_data():
    base = "https://jsonplaceholder.typicode.com"
    u = pd.DataFrame(requests.get(f"{base}/users").json())
    p = pd.DataFrame(requests.get(f"{base}/posts").json())
    c = pd.DataFrame(requests.get(f"{base}/comments").json())
    t = pd.DataFrame(requests.get(f"{base}/todos").json())
    return u, p, c, t

users, posts, comments, todos = load_data()

# --- NAGŁÓWEK ---
st.title("📊 Statystyki")
st.write("Analiza danych z serwisu JSONPlaceholder")
st.divider()

# --- SEKCJA 1: METRYKI ---
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("Użytkownicy", len(users))
with c2:
    st.metric("Wszystkie posty", len(posts))
with c3:
    st.metric("Suma komentarzy", len(comments))
with c4:
    done_pct = (todos['completed'].mean() * 100)
    st.metric("Ukończone zadania", f"{round(done_pct, 1)}%")

st.markdown("###")

# --- SEKCJA 2: WYKRESY ---
col_l, col_r = st.columns(2)

with col_l:
    st.subheader("💬 Liczba komentarzy na użytkownika")
    # Liczymy po prostu ile komentarzy zebrał dany user (wiemy, że każdy ma 50)
    # Łączymy komentarze z postami, żeby wiedzieć, czyj to post
    comments_with_user = comments.merge(posts[['id', 'userId']], left_on='postId', right_on='id')
    user_comm_count = comments_with_user.groupby('userId').size().reset_index(name='Ilość')
    user_comm_count['Użytkownik'] = "User " + user_comm_count['userId'].astype(str)

    # Prosty, czysty wykres słupkowy bez zbędnej legendy kolorów
    fig_bar = px.bar(
        user_comm_count, 
        x='Użytkownik', 
        y='Ilość',
        text_auto=True,
        color_discrete_sequence=['#58a6ff'] # Jeden solidny kolor
    )
    fig_bar.update_layout(
        template="plotly_dark", 
        yaxis_range=[0, 60], # Stały zakres, żeby nie "skakało"
        showlegend=False
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_r:
    st.subheader("🎯 Status zadań TODO (Globalnie)")
    todo_status = todos['completed'].value_counts().reset_index()
    todo_status.columns = ['Status', 'Ilość']
    todo_status['Status'] = todo_status['Status'].map({True: 'Wykonane', False: 'W toku'})

    fig_pie = px.pie(
        todo_status, 
        values='Ilość', 
        names='Status',
        hole=0.4,
        color_discrete_sequence=['#238636', '#da3633']
    )
    fig_pie.update_layout(template="plotly_dark")
    st.plotly_chart(fig_pie, use_container_width=True)

# --- SEKCJA 3: TABELA ---
st.divider()
st.subheader("🏆 Najpopularniejsze posty (Top 5)")
top_5_ids = comments.groupby('postId').size().nlargest(5).reset_index(name='Komentarze')
top_5_data = top_5_ids.merge(posts[['id', 'title']], left_on='postId', right_on='id')

st.table(top_5_data[['title', 'Komentarze']].rename(columns={'title': 'Tytuł posta'}))

st.caption("Projekt wykonany na potrzeby zadania rekrutacyjnego | 2026")