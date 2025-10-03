import streamlit as st
import matplotlib.pyplot as plt
from youtube_api_fake import get_comments
from sentiment_analysis import analyze_comments

st.set_page_config(page_title="YouTube Sentiment Analyzer 🎬", page_icon="📊")

st.title("🎬 YouTube Comment Sentiment Analyzer 📊")
st.write("Analyze and compare the **sentiments of two YouTube videos** using NLP, emojis, and visualizations 🚀")

# Input video IDs (mocked)
video1 = st.text_input("🔗 Enter Video 1 ID (try 'video1')", "video1")
video2 = st.text_input("🔗 Enter Video 2 ID (try 'video2')", "video2")

if st.button("🔍 Analyze Videos"):
    # Fetch comments
    comments1 = get_comments(video1)
    comments2 = get_comments(video2)

    # Analyze sentiments
    analysis1 = analyze_comments(comments1)
    analysis2 = analyze_comments(comments2)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📹 Video 1 Sentiment Results")
        st.write("### Sentiment Distribution (%)")
        st.write(analysis1["percentages"])

        fig1, ax1 = plt.subplots()
        ax1.pie(
            analysis1["percentages"].values(),
            labels=analysis1["percentages"].keys(),
            autopct='%1.1f%%'
        )
        st.pyplot(fig1)

        st.write("### Comments Analyzed")
        for r in analysis1["results"]:
            st.write(f"{r['comment']} → {r['sentiment']} ({r['polarity']:.2f})")

    with col2:
        st.subheader("📹 Video 2 Sentiment Results")
        st.write("### Sentiment Distribution (%)")
        st.write(analysis2["percentages"])

        fig2, ax2 = plt.subplots()
        ax2.pie(
            analysis2["percentages"].values(),
            labels=analysis2["percentages"].keys(),
            autopct='%1.1f%%'
        )
        st.pyplot(fig2)

        st.write("### Comments Analyzed")
        for r in analysis2["results"]:
            st.write(f"{r['comment']} → {r['sentiment']} ({r['polarity']:.2f})")

    # Comparison Result
    st.subheader("🏆 Comparison Result")
    avg1 = analysis1["percentages"]["Positive 😀"]
    avg2 = analysis2["percentages"]["Positive 😀"]

    if avg1 > avg2:
        st.success(f"🎉 Video 1 has more positive reception! ({avg1:.1f}% vs {avg2:.1f}%)")
    elif avg2 > avg1:
        st.success(f"🎉 Video 2 has more positive reception! ({avg2:.1f}% vs {avg1:.1f}%)")
    else:
        st.info("🤝 Both videos have equal positive reception!")
