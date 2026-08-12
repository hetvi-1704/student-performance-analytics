import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD DATA
# ============================================================

data = pd.read_csv(
    "student-mat.csv",
    sep=";"
)


# ============================================================
# DARK DASHBOARD CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       MAIN BACKGROUND
       ======================================================== */

    .stApp {
        background-color: #0f1117 !important;
        color: #f8fafc !important;
    }

    [data-testid="stAppViewContainer"] {
        background-color: #0f1117 !important;
    }

    [data-testid="stHeader"] {
        background-color: #0f1117 !important;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {
        background-color: #171a23 !important;
        border-right: 1px solid #292e3a !important;
    }

    [data-testid="stSidebar"] * {
        color: #e5e7eb !important;
    }

    [data-testid="stSidebar"] h1 {
        color: #ffffff !important;
    }

    [data-testid="stSidebar"] p {
        color: #aeb6c5 !important;
    }

    [data-testid="stSidebar"] label {
        color: #dbe3ef !important;
    }


    /* ========================================================
       SELECTBOX
       ======================================================== */

    [data-testid="stSelectbox"] {
        background-color: transparent !important;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] {
        background-color: #0b0e13 !important;
        border-radius: 10px !important;
    }

    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background-color: #0b0e13 !important;
        color: #ffffff !important;
        border: 1px solid #343a48 !important;
        border-radius: 10px !important;
    }

    [data-testid="stSelectbox"] span {
        color: #ffffff !important;
        background-color: transparent !important;
    }

    [data-testid="stSelectbox"] svg {
        color: #94a3b8 !important;
        fill: #94a3b8 !important;
    }


    /* ========================================================
       DROPDOWN MENU
       ======================================================== */

    [data-baseweb="popover"] {
        background-color: #171a23 !important;
        border: 1px solid #343a48 !important;
    }

    [data-baseweb="popover"] ul {
        background-color: #171a23 !important;
    }

    [data-baseweb="popover"] li {
        background-color: #171a23 !important;
        color: #ffffff !important;
    }

    [data-baseweb="popover"] [role="option"] {
        background-color: #171a23 !important;
        color: #ffffff !important;
    }

    [data-baseweb="popover"] [role="option"]:hover {
        background-color: #252b38 !important;
        color: #60a5fa !important;
    }


    /* ========================================================
       TITLE
       ======================================================== */

    .dashboard-title {
        font-size: 44px;
        font-weight: 750;
        color: #f8fafc;
        margin-bottom: 5px;
    }

    .dashboard-subtitle {
        font-size: 18px;
        color: #94a3b8;
        margin-bottom: 35px;
    }


    /* ========================================================
       SECTION TITLE
       ======================================================== */

    .section-title {
        font-size: 27px;
        font-weight: 650;
        color: #f1f5f9;
        margin-top: 25px;
        margin-bottom: 15px;
    }


    /* ========================================================
       OVERVIEW CARD
       ======================================================== */

    .overview-box {
        background-color: #171a23;
        border-left: 5px solid #3b82f6;
        padding: 18px 22px;
        border-radius: 12px;
        color: #aeb6c5;
        font-size: 17px;
        border: 1px solid #292e3a;
        margin-bottom: 20px;
    }


    /* ========================================================
       FILTER STATUS
       ======================================================== */

    .filter-status {
        background-color: #111827;
        border: 1px solid #263a5c;
        padding: 13px 17px;
        border-radius: 10px;
        color: #93c5fd;
        font-size: 15px;
        margin-bottom: 20px;
    }


    /* ========================================================
       KPI CARDS
       ======================================================== */

    .kpi-card {
        background-color: #171a23;
        padding: 22px;
        border-radius: 15px;
        min-height: 130px;
        border: 1px solid #292e3a;
        box-shadow: 0 5px 20px rgba(0,0,0,0.20);
    }


    /* CARD TOP COLORS */

    .blue-card {
        border-top: 5px solid #3b82f6;
    }

    .purple-card {
        border-top: 5px solid #8b5cf6;
    }

    .green-card {
        border-top: 5px solid #22c55e;
    }

    .orange-card {
        border-top: 5px solid #f97316;
    }


    /* ========================================================
       KPI LABELS
       ======================================================== */

    .kpi-label {
        font-size: 15px;
        color: #94a3b8;
        margin-bottom: 10px;
    }


    /* ========================================================
       KPI VALUES
       ======================================================== */

    .blue-value {
        font-size: 34px;
        font-weight: 750;
        color: #60a5fa;
    }

    .purple-value {
        font-size: 34px;
        font-weight: 750;
        color: #a78bfa;
    }

    .green-value {
        font-size: 34px;
        font-weight: 750;
        color: #4ade80;
    }

    .orange-value {
        font-size: 34px;
        font-weight: 750;
        color: #fb923c;
    }


    /* ========================================================
       CHART CONTAINERS
       ======================================================== */

    .chart-heading {
        font-size: 20px;
        font-weight: 600;
        color: #f1f5f9;
        margin-bottom: 5px;
    }


    /* ========================================================
       SIDEBAR INFO BOX
       ======================================================== */

    [data-testid="stSidebar"] [data-testid="stAlert"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
    }


    /* ========================================================
       DIVIDER
       ======================================================== */

    hr {
        border: none;
        border-top: 1px solid #292e3a;
        margin: 30px 0;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        text-align: center;
        color: #64748b;
        padding: 20px;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Filters")

st.sidebar.write(
    "Use the filters below to explore student performance."
)

st.sidebar.markdown("---")


# ============================================================
# SCHOOL FILTER
# ============================================================

school_options = ["All"] + sorted(
    data["school"].unique().tolist()
)

school_filter = st.sidebar.selectbox(
    "🏫 School",
    school_options
)


# ============================================================
# GENDER FILTER
# ============================================================

gender_options = ["All"] + sorted(
    data["sex"].unique().tolist()
)

gender_filter = st.sidebar.selectbox(
    "👤 Gender",
    gender_options
)


# ============================================================
# STUDY TIME FILTER
# ============================================================

studytime_options = ["All"] + sorted(
    data["studytime"].unique().tolist()
)

studytime_filter = st.sidebar.selectbox(
    "📚 Study Time",
    studytime_options
)


st.sidebar.markdown("---")

st.sidebar.info(
    "💡 Change any filter to update the dashboard."
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_data = data.copy()


if school_filter != "All":
    filtered_data = filtered_data[
        filtered_data["school"] == school_filter
    ]


if gender_filter != "All":
    filtered_data = filtered_data[
        filtered_data["sex"] == gender_filter
    ]


if studytime_filter != "All":
    filtered_data = filtered_data[
        filtered_data["studytime"] == studytime_filter
    ]


# ============================================================
# MAIN TITLE
# ============================================================

st.markdown(
    '<div class="dashboard-title">'
    '🎓 Student Performance Analytics'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Interactive dashboard for analyzing student academic performance.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DATASET OVERVIEW
# ============================================================

st.markdown(
    '<div class="section-title">'
    'Dataset Overview'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="overview-box">'
    'This dataset contains information about '
    '<b>395 students</b> across '
    '<b>33 different features</b>. '
    'Use the filters to explore different student groups.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# FILTER STATUS
# ============================================================

filter_status = (
    "🔎 Current filters: "
    "School = " + str(school_filter) +
    " | Gender = " + str(gender_filter) +
    " | Study Time = " + str(studytime_filter)
)

st.markdown(
    '<div class="filter-status">'
    + filter_status +
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_students = len(filtered_data)

average_grade = filtered_data["G3"].mean()

highest_grade = filtered_data["G3"].max()

average_absences = filtered_data["absences"].mean()


# ============================================================
# KPI SECTION
# ============================================================

st.markdown(
    '<div class="section-title">'
    'Key Performance Indicators'
    '</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


# ============================================================
# KPI 1
# ============================================================

with col1:

    st.markdown(
        '<div class="kpi-card blue-card">'
        '<div class="kpi-label">👥 Total Students</div>'
        '<div class="blue-value">'
        + str(total_students) +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI 2
# ============================================================

with col2:

    st.markdown(
        '<div class="kpi-card purple-card">'
        '<div class="kpi-label">📊 Average Final Grade</div>'
        '<div class="purple-value">'
        + str(round(average_grade, 2)) +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI 3
# ============================================================

with col3:

    st.markdown(
        '<div class="kpi-card green-card">'
        '<div class="kpi-label">🏆 Highest Final Grade</div>'
        '<div class="green-value">'
        + str(highest_grade) +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# KPI 4
# ============================================================

with col4:

    st.markdown(
        '<div class="kpi-card orange-card">'
        '<div class="kpi-label">📅 Average Absences</div>'
        '<div class="orange-value">'
        + str(round(average_absences, 2)) +
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )





# ============================================================
# PERFORMANCE ANALYSIS
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">'
    '📊 Performance Analysis'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# CHART 1 + CHART 2
# ============================================================

chart1, chart2 = st.columns(2)


# ============================================================
# CHART 1 - FINAL GRADE DISTRIBUTION
# ============================================================

with chart1:

    st.markdown(
        '<div class="chart-heading">'
        '🎯 Final Grade Distribution'
        '</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(7, 4))

    fig.patch.set_facecolor("#171a23")
    ax.set_facecolor("#171a23")

    ax.hist(
        filtered_data["G3"],
        bins=10,
        color="#3b82f6",
        edgecolor="#0f1117",
        alpha=0.9
    )

    ax.set_xlabel(
        "Final Grade",
        color="#cbd5e1"
    )

    ax.set_ylabel(
        "Number of Students",
        color="#cbd5e1"
    )

    ax.set_title(
        "Final Grade Distribution",
        color="#f8fafc"
    )

    ax.tick_params(colors="#94a3b8")

    ax.grid(
        axis="y",
        alpha=0.15
    )

    for spine in ax.spines.values():
        spine.set_color("#334155")

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# ============================================================
# CHART 2 - STUDY TIME
# ============================================================

with chart2:

    st.markdown(
        '<div class="chart-heading">'
        '📚 Study Time vs Final Grade'
        '</div>',
        unsafe_allow_html=True
    )

    study_analysis = (
        filtered_data
        .groupby("studytime")["G3"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(7, 4))

    fig.patch.set_facecolor("#171a23")
    ax.set_facecolor("#171a23")

    ax.bar(
        study_analysis.index.astype(str),
        study_analysis.values,
        color="#8b5cf6",
        alpha=0.9
    )

    ax.set_xlabel(
        "Study Time Category",
        color="#cbd5e1"
    )

    ax.set_ylabel(
        "Average Final Grade",
        color="#cbd5e1"
    )

    ax.set_title(
        "Study Time vs Average Final Grade",
        color="#f8fafc"
    )

    ax.tick_params(colors="#94a3b8")

    ax.grid(
        axis="y",
        alpha=0.15
    )

    for spine in ax.spines.values():
        spine.set_color("#334155")

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# ============================================================
# CHART 3 + CHART 4
# ============================================================

chart3, chart4 = st.columns(2)


# ============================================================
# CHART 3 - ABSENCES
# ============================================================

with chart3:

    st.markdown(
        '<div class="chart-heading">'
        '📅 Absences vs Final Grade'
        '</div>',
        unsafe_allow_html=True
    )

    fig, ax = plt.subplots(figsize=(7, 4))

    fig.patch.set_facecolor("#171a23")
    ax.set_facecolor("#171a23")

    ax.scatter(
        filtered_data["absences"],
        filtered_data["G3"],
        color="#f97316",
        alpha=0.65
    )

    ax.set_xlabel(
        "Number of Absences",
        color="#cbd5e1"
    )

    ax.set_ylabel(
        "Final Grade",
        color="#cbd5e1"
    )

    ax.set_title(
        "Absences vs Final Grade",
        color="#f8fafc"
    )

    ax.tick_params(colors="#94a3b8")

    ax.grid(
        alpha=0.15
    )

    for spine in ax.spines.values():
        spine.set_color("#334155")

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# ============================================================
# CHART 4 - FAILURES
# ============================================================

with chart4:

    st.markdown(
        '<div class="chart-heading">'
        '⚠️ Previous Failures vs Final Grade'
        '</div>',
        unsafe_allow_html=True
    )

    failure_analysis = (
        filtered_data
        .groupby("failures")["G3"]
        .mean()
    )

    fig, ax = plt.subplots(figsize=(7, 4))

    fig.patch.set_facecolor("#171a23")
    ax.set_facecolor("#171a23")

    ax.bar(
        failure_analysis.index.astype(str),
        failure_analysis.values,
        color="#ef4444",
        alpha=0.9
    )

    ax.set_xlabel(
        "Previous Failures",
        color="#cbd5e1"
    )

    ax.set_ylabel(
        "Average Final Grade",
        color="#cbd5e1"
    )

    ax.set_title(
        "Previous Failures vs Average Final Grade",
        color="#f8fafc"
    )

    ax.tick_params(colors="#94a3b8")

    ax.grid(
        axis="y",
        alpha=0.15
    )

    for spine in ax.spines.values():
        spine.set_color("#334155")

    st.pyplot(
        fig,
        use_container_width=True
    )

    plt.close(fig)


# ============================================================
# CORRELATION ANALYSIS
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">'
    '🔥 Correlation Analysis'
    '</div>',
    unsafe_allow_html=True
)


correlation = filtered_data[
    [
        "studytime",
        "failures",
        "absences",
        "G1",
        "G2",
        "G3"
    ]
].corr()


# ============================================================
# CORRELATION HEATMAP
# ============================================================

fig, ax = plt.subplots(figsize=(9, 6))

fig.patch.set_facecolor("#171a23")
ax.set_facecolor("#171a23")


heatmap = ax.imshow(
    correlation,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)


# Axis labels

ax.set_xticks(
    range(len(correlation.columns))
)

ax.set_yticks(
    range(len(correlation.columns))
)

ax.set_xticklabels(
    correlation.columns,
    color="#cbd5e1"
)

ax.set_yticklabels(
    correlation.columns,
    color="#cbd5e1"
)


# Add correlation values

for i in range(len(correlation.columns)):

    for j in range(len(correlation.columns)):

        value = correlation.iloc[i, j]

        ax.text(
            j,
            i,
            f"{value:.2f}",
            ha="center",
            va="center",
            color="white" if abs(value) > 0.45 else "#111827",
            fontsize=11
        )


ax.set_title(
    "Correlation Heatmap",
    color="#f8fafc",
    fontsize=16
)


# Color bar

cbar = fig.colorbar(
    heatmap,
    ax=ax
)

cbar.ax.tick_params(
    colors="#cbd5e1"
)


st.pyplot(
    fig,
    use_container_width=True
)

plt.close(fig)


# ============================================================
# KEY INSIGHTS
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">'
    '🧠 Key Insights'
    '</div>',
    unsafe_allow_html=True
)


# Get correlations with final grade

g3_correlation = (
    correlation["G3"]
    .drop("G3")
    .sort_values(
        ascending=False
    )
)


# Strongest positive relationship

strongest_positive = g3_correlation.idxmax()

positive_value = g3_correlation.max()


# Strongest negative relationship

strongest_negative = g3_correlation.idxmin()

negative_value = g3_correlation.min()


# Study time average

study_average = (
    filtered_data
    .groupby("studytime")["G3"]
    .mean()
)


highest_study_category = study_average.idxmax()

highest_study_grade = study_average.max()


# Failure comparison

failure_average = (
    filtered_data
    .groupby("failures")["G3"]
    .mean()
)


highest_failure_grade = failure_average.max()

lowest_failure_grade = failure_average.min()


# ============================================================
# INSIGHT CARDS
# ============================================================

insight1, insight2 = st.columns(2)


with insight1:

    st.info(
        f"📈 **Strongest positive relationship:** "
        f"{strongest_positive} has a correlation of "
        f"**{positive_value:.2f}** with the final grade (G3)."
    )


with insight2:

    st.warning(
        f"📉 **Strongest negative relationship:** "
        f"{strongest_negative} has a correlation of "
        f"**{negative_value:.2f}** with the final grade (G3)."
    )


insight3, insight4 = st.columns(2)


with insight3:

    st.success(
        f"📚 Students in study-time category "
        f"**{highest_study_category}** have the highest "
        f"average final grade of approximately "
        f"**{highest_study_grade:.2f}**."
    )


with insight4:

    highest_failure_group = failure_average.idxmax()
    lowest_failure_group = failure_average.idxmin()

    st.error(
        f"⚠️ Students with {highest_failure_group} previous "
        f"failure(s) have the highest average grade "
        f"({highest_failure_grade:.2f}), while students with "
        f"{lowest_failure_group} previous failure(s) have the "
        f"lowest ({lowest_failure_grade:.2f})."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    '🎓 Student Performance Analytics &nbsp;|&nbsp; '
    'Python • Pandas • Matplotlib • Streamlit'
    '</div>',
    unsafe_allow_html=True
)

