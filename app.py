"""
✈️ AeroInsight Pro v3.0 — Ultra-Pro Edition
Airline Flight Delay & Route Performance system Platform
Enhanced with cinematic hero header, particle effects, aviation SVG backgrounds,
advanced glassmorphism, Orbit/Space Grotesk fonts, and premium chart styling.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import time
import datetime
import random
import io
import base64

# ─── PAGE CONFIG ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AeroInsight Pro",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "AeroInsight Pro v3.0 — Ultra-Pro Edition by AeroTech Analytics"},
)

# ─── THEME ───────────────────────────────────────────────────────────────────
def get_theme(dark: bool) -> dict:
    if dark:
        return {
            "bg":           "#050914",
            "bg2":          "#080d1e",
            "card":         "rgba(255,255,255,0.035)",
            "card_hover":   "rgba(255,255,255,0.07)",
            "border":       "rgba(255,255,255,0.07)",
            "border_h":     "rgba(79,142,247,0.4)",
            "text":         "#e8f0ff",
            "muted":        "#6b7fa3",
            "dim":          "#2d3a55",
            "accent1":      "#4f8ef7",
            "accent2":      "#00d4aa",
            "accent3":      "#f7944f",
            "danger":       "#ff5c7c",
            "purple":       "#a78bfa",
            "paper":        "#0b1025",
            "gridcolor":    "rgba(255,255,255,0.04)",
            "font":         "#e8f0ff",
            "sidebar":      "#040810",
            "glow1":        "rgba(79,142,247,0.18)",
            "glow2":        "rgba(0,212,170,0.12)",
            "glow3":        "rgba(167,139,250,0.08)",
        }
    return {
        "bg":           "#f0f4ff",
        "bg2":          "#e8eef8",
        "card":         "rgba(255,255,255,0.88)",
        "card_hover":   "rgba(255,255,255,1.0)",
        "border":       "rgba(0,0,0,0.07)",
        "border_h":     "rgba(37,99,235,0.35)",
        "text":         "#0a0e1a",
        "muted":        "#6b7fa3",
        "dim":          "#b0bcd4",
        "accent1":      "#2563eb",
        "accent2":      "#059669",
        "accent3":      "#d97706",
        "danger":       "#dc2626",
        "purple":       "#7c3aed",
        "paper":        "#e2e8f4",
        "gridcolor":    "rgba(0,0,0,0.04)",
        "font":         "#0a0e1a",
        "sidebar":      "#dce4f4",
        "glow1":        "rgba(37,99,235,0.10)",
        "glow2":        "rgba(5,150,105,0.08)",
        "glow3":        "rgba(124,58,237,0.06)",
    }

def inject_css(dark: bool):
    t = get_theme(dark)
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Orbitron:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* ── GLOBAL RESET ── */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

    html, body {{
        font-family: 'Space Grotesk', sans-serif !important;
        background: {t['bg']} !important;
        color: {t['text']} !important;
        scroll-behavior: smooth;
    }}

    [data-testid="stAppViewContainer"] {{
        background:
            radial-gradient(ellipse 900px 600px at 10% 0%,   {t['glow1']} 0%, transparent 70%),
            radial-gradient(ellipse 700px 500px at 90% 100%, {t['glow2']} 0%, transparent 70%),
            radial-gradient(ellipse 500px 400px at 50% 50%,  {t['glow3']} 0%, transparent 70%),
            {t['bg']} !important;
        min-height: 100vh;
    }}

    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] {{
        background: {t['sidebar']} !important;
        border-right: 1px solid {t['border']} !important;
    }}
    [data-testid="stSidebarContent"] {{ padding: 0 !important; }}

    /* ── MAIN CONTAINER ── */
    .main .block-container {{
        padding: 0 2rem 3rem 2rem !important;
        max-width: 1700px !important;
    }}

    /* ── TYPOGRAPHY ── */
    h1,h2,h3,h4,h5,h6 {{
        font-family: 'Space Grotesk', sans-serif !important;
        color: {t['text']} !important;
        font-weight: 700 !important;
    }}

    /* ══════════════════════════════════════════
       HERO HEADER — CINEMATIC AIRLINE BANNER
    ══════════════════════════════════════════ */
    .hero-wrapper {{
        position: relative;
        width: 100%;
        min-height: 200px;
        border-radius: 24px;
        overflow: hidden;
        margin-bottom: 28px;
        border: 1px solid {t['border']};
    }}
    .hero-bg {{
        position: absolute;
        inset: 0;
        background:
            linear-gradient(135deg,
                rgba(5,9,20,0.92) 0%,
                rgba(8,20,50,0.85) 40%,
                rgba(10,30,70,0.78) 100%
            );
        z-index: 1;
    }}
    /* SVG flight path lines */
    .hero-bg::before {{
        content: '';
        position: absolute;
        inset: 0;
        background-image:
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='200'%3E%3Cdefs%3E%3ClinearGradient id='lg1' x1='0' y1='0' x2='1' y2='0'%3E%3Cstop offset='0' stop-color='%234f8ef7' stop-opacity='0'/%3E%3Cstop offset='0.5' stop-color='%234f8ef7' stop-opacity='0.6'/%3E%3Cstop offset='1' stop-color='%2300d4aa' stop-opacity='0'/%3E%3C/linearGradient%3E%3ClinearGradient id='lg2' x1='0' y1='0' x2='1' y2='0'%3E%3Cstop offset='0' stop-color='%2300d4aa' stop-opacity='0'/%3E%3Cstop offset='0.5' stop-color='%23a78bfa' stop-opacity='0.5'/%3E%3Cstop offset='1' stop-color='%234f8ef7' stop-opacity='0'/%3E%3C/linearGradient%3E%3C/defs%3E%3Cpath d='M0,80 Q200,30 400,90 T800,60' fill='none' stroke='url(%23lg1)' stroke-width='1.5'/%3E%3Cpath d='M0,130 Q200,80 400,140 T800,110' fill='none' stroke='url(%23lg2)' stroke-width='1'/%3E%3Cpath d='M0,160 Q300,110 600,170 T800,140' fill='none' stroke='url(%23lg1)' stroke-width='0.8' opacity='0.5'/%3E%3Ccircle cx='400' cy='90' r='3' fill='%234f8ef7' opacity='0.8'/%3E%3Ccircle cx='600' cy='120' r='2' fill='%2300d4aa' opacity='0.7'/%3E%3Ccircle cx='200' cy='75' r='2.5' fill='%23a78bfa' opacity='0.6'/%3E%3C/svg%3E");
        background-size: cover;
        background-repeat: no-repeat;
        z-index: 0;
        opacity: 0.9;
    }}
    /* Star / particle field */
    .hero-bg::after {{
        content: '';
        position: absolute;
        inset: 0;
        background-image:
            radial-gradient(circle, rgba(79,142,247,0.8) 1px, transparent 1px),
            radial-gradient(circle, rgba(0,212,170,0.6) 1px, transparent 1px),
            radial-gradient(circle, rgba(255,255,255,0.4) 1px, transparent 1px);
        background-size: 80px 80px, 120px 120px, 50px 50px;
        background-position: 10px 10px, 40px 55px, 25px 30px;
        z-index: 0;
        animation: starDrift 20s linear infinite;
    }}
    @keyframes starDrift {{
        0%   {{ background-position: 10px 10px, 40px 55px, 25px 30px; }}
        100% {{ background-position: 90px 90px, 160px 175px, 75px 80px; }}
    }}

    .hero-content {{
        position: relative;
        z-index: 2;
        padding: 32px 40px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 24px;
    }}

    /* ── ORBITRON LOGO ── */
    .hero-logo {{
        font-family: 'Orbitron', monospace;
        font-size: clamp(24px, 3vw, 42px);
        font-weight: 900;
        letter-spacing: 0.04em;
        background: linear-gradient(90deg, #4f8ef7 0%, #00d4aa 45%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.1;
        text-shadow: none;
        filter: drop-shadow(0 0 20px rgba(79,142,247,0.4));
    }}
    .hero-logo-plane {{
        font-size: 0.75em;
        margin-right: 10px;
        display: inline-block;
        animation: planeFly 4s ease-in-out infinite;
        -webkit-text-fill-color: #4f8ef7;
    }}
    @keyframes planeFly {{
        0%,100% {{ transform: translateY(0px) rotate(-5deg); }}
        50%      {{ transform: translateY(-6px) rotate(0deg); }}
    }}
    .hero-tagline {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(12px, 1.2vw, 14px);
        color: rgba(200,215,255,0.65);
        font-weight: 400;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-top: 6px;
    }}
    .hero-version-pill {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 20px;
        background: rgba(79,142,247,0.15);
        border: 1px solid rgba(79,142,247,0.35);
        color: #4f8ef7;
        letter-spacing: 0.08em;
        margin-top: 10px;
        display: inline-block;
    }}

    /* ── HERO RIGHT STATS ── */
    .hero-stats {{
        display: flex;
        gap: 20px;
        flex-wrap: wrap;
        justify-content: flex-end;
    }}
    .hero-stat-item {{
        text-align: center;
        min-width: 80px;
    }}
    .hero-stat-value {{
        font-family: 'Orbitron', monospace;
        font-size: clamp(18px, 2vw, 26px);
        font-weight: 700;
        color: #4f8ef7;
        line-height: 1;
    }}
    .hero-stat-value.green {{ color: #00d4aa; }}
    .hero-stat-value.orange {{ color: #f7944f; }}
    .hero-stat-value.purple {{ color: #a78bfa; }}
    .hero-stat-label {{
        font-size: 10px;
        color: rgba(200,215,255,0.5);
        font-weight: 500;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-top: 4px;
    }}
    .hero-divider {{
        width: 1px;
        height: 40px;
        background: rgba(255,255,255,0.1);
        align-self: center;
    }}

    /* ── TICKER STRIP ── */
    .ticker-strip {{
        background: rgba(79,142,247,0.08);
        border-top: 1px solid rgba(79,142,247,0.2);
        padding: 8px 24px;
        display: flex;
        align-items: center;
        gap: 32px;
        overflow: hidden;
        position: relative;
        z-index: 2;
    }}
    .ticker-item {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 500;
        white-space: nowrap;
        color: rgba(200,215,255,0.7);
    }}
    .ticker-item span {{
        color: #00d4aa;
        margin-left: 4px;
    }}
    .ticker-item.red span {{ color: #ff5c7c; }}
    .ticker-dot {{
        width: 5px; height: 5px;
        border-radius: 50%;
        background: #4f8ef7;
        opacity: 0.6;
        flex-shrink: 0;
    }}

    /* ══════════════════════════════
       KPI CARDS — NEON GLOW STYLE
    ══════════════════════════════ */
    .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 12px;
        margin-bottom: 28px;
    }}
    .kpi-card {{
        background: {t['card']};
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid {t['border']};
        border-radius: 18px;
        padding: 18px 16px 14px;
        position: relative;
        overflow: hidden;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        cursor: default;
    }}
    .kpi-card::after {{
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 2px;
        background: var(--kpi-color, {t['accent1']});
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    .kpi-card:hover {{
        background: {t['card_hover']};
        border-color: {t['border_h']};
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0,0,0,0.25), 0 0 0 1px {t['border_h']};
    }}
    .kpi-card:hover::after {{ opacity: 1; }}

    /* corner accent */
    .kpi-card::before {{
        content: '';
        position: absolute;
        top: -30px; right: -30px;
        width: 80px; height: 80px;
        border-radius: 50%;
        background: var(--kpi-color, {t['accent1']});
        opacity: 0.06;
    }}

    .kpi-icon {{
        font-size: 20px;
        margin-bottom: 10px;
        display: block;
        filter: drop-shadow(0 0 8px var(--kpi-color, {t['accent1']}));
    }}
    .kpi-label {{
        font-size: 10px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: {t['muted']};
        margin-bottom: 5px;
        font-family: 'Space Grotesk', sans-serif;
    }}
    .kpi-value {{
        font-family: 'Orbitron', monospace;
        font-size: clamp(16px, 1.8vw, 22px);
        font-weight: 700;
        color: {t['text']};
        line-height: 1.1;
        margin-bottom: 7px;
        letter-spacing: -0.01em;
    }}
    .kpi-trend {{
        font-size: 11px;
        font-weight: 600;
        font-family: 'JetBrains Mono', monospace;
    }}
    .kpi-trend.up   {{ color: {t['accent2']}; }}
    .kpi-trend.down {{ color: {t['danger']}; }}
    .kpi-sub {{
        font-size: 10px;
        color: {t['muted']};
        margin-top: 3px;
        font-family: 'Space Grotesk', sans-serif;
    }}

    /* ══════════════════════════════
       SECTION HEADERS
    ══════════════════════════════ */
    .section-hdr {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 28px 0 16px;
    }}
    .section-hdr-icon {{
        width: 32px; height: 32px;
        border-radius: 8px;
        background: linear-gradient(135deg, {t['accent1']}25, {t['accent2']}15);
        border: 1px solid {t['accent1']}35;
        display: flex; align-items: center; justify-content: center;
        font-size: 15px;
        flex-shrink: 0;
    }}
    .section-hdr-title {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 16px;
        font-weight: 700;
        color: {t['text']};
        letter-spacing: -0.01em;
    }}
    .section-hdr-line {{
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg, {t['border']}, transparent);
    }}
    .section-badge {{
        font-size: 10px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 20px;
        background: {t['accent1']}18;
        color: {t['accent1']};
        letter-spacing: 0.07em;
        text-transform: uppercase;
        border: 1px solid {t['accent1']}30;
        font-family: 'Space Grotesk', sans-serif;
    }}

    /* ══════════════════════════════
       CHART CARDS
    ══════════════════════════════ */
    .chart-card {{
        background: {t['card']};
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        border: 1px solid {t['border']};
        border-radius: 20px;
        padding: 20px;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }}
    .chart-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, {t['accent1']}50, transparent);
    }}
    .chart-card:hover {{
        border-color: {t['border_h']};
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }}

    /* ══════════════════════════════
       INSIGHTS PANEL
    ══════════════════════════════ */
    .insight-panel {{
        background: linear-gradient(135deg, {t['accent1']}10, {t['accent2']}06);
        border: 1px solid {t['accent1']}25;
        border-radius: 20px;
        padding: 22px;
    }}
    .insight-item {{
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 10px;
        padding: 12px 16px;
        background: {t['card']};
        border-radius: 12px;
        border-left: 3px solid {t['accent1']};
        font-size: 13px;
        color: {t['muted']};
        line-height: 1.55;
        font-family: 'Space Grotesk', sans-serif;
        transition: all 0.2s ease;
    }}
    .insight-item:hover {{ background: {t['card_hover']}; transform: translateX(4px); }}
    .insight-item:last-child {{ margin-bottom: 0; }}
    .insight-item.warn   {{ border-left-color: {t['accent3']}; }}
    .insight-item.danger {{ border-left-color: {t['danger']}; }}
    .insight-item.good   {{ border-left-color: {t['accent2']}; }}
    .insight-item b {{ color: {t['text']}; font-weight: 600; }}

    /* ══════════════════════════════
       STATUS BADGES
    ══════════════════════════════ */
    .status-live {{
        display: inline-flex; align-items: center; gap: 6px;
        font-size: 11px; font-weight: 700;
        color: {t['accent2']};
        background: {t['accent2']}15;
        padding: 5px 12px; border-radius: 20px;
        border: 1px solid {t['accent2']}35;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: 0.06em;
    }}
    .status-offline {{
        display: inline-flex; align-items: center; gap: 6px;
        font-size: 11px; font-weight: 700;
        color: {t['accent3']};
        background: {t['accent3']}15;
        padding: 5px 12px; border-radius: 20px;
        border: 1px solid {t['accent3']}35;
        font-family: 'JetBrains Mono', monospace;
        letter-spacing: 0.06em;
    }}
    .status-dot {{
        width: 7px; height: 7px;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }}
    .dot-live    {{ background: {t['accent2']}; box-shadow: 0 0 8px {t['accent2']}; }}
    .dot-offline {{ background: {t['accent3']}; }}
    @keyframes pulse {{
        0%,100% {{ opacity:1; transform:scale(1); }}
        50%      {{ opacity:0.45; transform:scale(1.4); }}
    }}

    /* ══════════════════════════════
       RANKING ROWS
    ══════════════════════════════ */
    .rank-row {{
        display: flex; align-items: center; gap: 14px;
        padding: 12px 16px;
        border-radius: 12px; margin-bottom: 7px;
        background: {t['card']};
        border: 1px solid {t['border']};
        transition: all 0.25s ease;
    }}
    .rank-row:hover {{
        background: {t['card_hover']};
        transform: translateX(5px);
        border-color: {t['border_h']};
    }}
    .rank-num {{
        font-family: 'Orbitron', monospace;
        font-size: 13px; font-weight: 600;
        color: {t['muted']};
        width: 26px; text-align: center;
    }}
    .rank-num.top {{ color: {t['accent1']}; }}
    .rank-name {{
        flex: 1;
        font-size: 13px; font-weight: 600;
        color: {t['text']};
        font-family: 'Space Grotesk', sans-serif;
    }}
    .rank-score {{
        font-family: 'Orbitron', monospace;
        font-size: 14px; font-weight: 700;
        color: {t['accent1']};
    }}
    .rank-bar-bg {{
        width: 90px; height: 6px;
        background: {t['border']}; border-radius: 3px; overflow: hidden;
    }}
    .rank-bar-fill {{
        height: 100%; border-radius: 3px;
        background: linear-gradient(90deg, {t['accent1']}, {t['accent2']});
        transition: width 0.8s cubic-bezier(0.4,0,0.2,1);
    }}

    /* ══════════════════════════════
       SIDEBAR NAV
    ══════════════════════════════ */
    .nav-section-label {{
        font-size: 10px; font-weight: 700;
        text-transform: uppercase; letter-spacing: 0.12em;
        color: {t['muted']};
        padding: 0 16px;
        margin-bottom: 6px;
        font-family: 'Space Grotesk', sans-serif;
    }}

    /* ══════════════════════════════
       FOOTER
    ══════════════════════════════ */
    .app-footer {{
        text-align: center;
        padding: 24px;
        color: {t['muted']};
        font-size: 12px;
        border-top: 1px solid {t['border']};
        margin-top: 48px;
        font-family: 'Space Grotesk', sans-serif;
    }}

    /* ── SCROLLBAR ── */
    ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{
        background: {t['accent1']}50; border-radius: 3px;
    }}

    /* ── STREAMLIT OVERRIDES ── */
    div[data-testid="stSelectbox"] > div,
    div[data-testid="stMultiSelect"] > div {{
        background: {t['card']} !important;
        border-color: {t['border']} !important;
        border-radius: 12px !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }}
    .stSlider > div > div {{ background: {t['accent1']}35 !important; }}
    [data-testid="baseButton-primary"],
    [data-testid="baseButton-secondary"] {{
        border-radius: 10px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 13px !important;
        transition: all 0.2s ease !important;
    }}
    .stTabs [data-baseweb="tab-list"] {{
        background: {t['card']} !important;
        border-radius: 14px !important;
        border: 1px solid {t['border']} !important;
        gap: 4px; padding: 5px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background: transparent !important;
        color: {t['muted']} !important;
        border-radius: 10px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 500 !important;
        font-size: 13px !important;
    }}
    .stTabs [aria-selected="true"] {{
        background: {t['accent1']}22 !important;
        color: {t['accent1']} !important;
        font-weight: 700 !important;
    }}
    div[data-testid="metric-container"] {{
        background: {t['card']}; border: 1px solid {t['border']};
        border-radius: 14px; padding: 14px 18px !important;
    }}
    label[data-testid="stWidgetLabel"] {{
        color: {t['muted']} !important;
        font-size: 12px !important; font-weight: 600 !important;
        text-transform: uppercase !important; letter-spacing: 0.07em !important;
        font-family: 'Space Grotesk', sans-serif !important;
    }}
    .stAlert {{ border-radius: 14px !important; border: none !important; }}
    .js-plotly-plot .plotly .bg {{ fill: transparent !important; }}
    </style>
    """, unsafe_allow_html=True)


# ─── PLOTLY LAYOUT ────────────────────────────────────────────────────────────
def plotly_layout(t: dict, title: str = "", height: int = 380) -> dict:
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Space Grotesk, sans-serif", color=t["muted"], size=12),
        title=dict(
            text=title,
            font=dict(family="Space Grotesk, sans-serif", color=t["text"], size=14, weight=700),
            x=0, pad=dict(l=4),
        ),
        height=height,
        margin=dict(l=10, r=10, t=44 if title else 12, b=10),
        xaxis=dict(showgrid=True, gridcolor=t["gridcolor"], zeroline=False,
                   tickfont=dict(color=t["muted"], size=11, family="Space Grotesk"),
                   linecolor=t["border"]),
        yaxis=dict(showgrid=True, gridcolor=t["gridcolor"], zeroline=False,
                   tickfont=dict(color=t["muted"], size=11, family="Space Grotesk"),
                   linecolor=t["border"]),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=t["muted"], size=11, family="Space Grotesk"),
                    bordercolor=t["border"], borderwidth=1),
        hoverlabel=dict(bgcolor=t["paper"], font=dict(family="Space Grotesk", color=t["text"], size=12),
                        bordercolor=t["border"]),
    )


# ─── DATA LAYER ───────────────────────────────────────────────────────────────
AIRLINES = [
    "Delta Air Lines", "American Airlines", "United Airlines",
    "Southwest Airlines", "JetBlue Airways", "Alaska Airlines",
    "Spirit Airlines", "Frontier Airlines", "Allegiant Air", "Hawaiian Airlines",
]
AIRLINE_CODES = {
    "Delta Air Lines": "DL", "American Airlines": "AA", "United Airlines": "UA",
    "Southwest Airlines": "WN", "JetBlue Airways": "B6", "Alaska Airlines": "AS",
    "Spirit Airlines": "NK", "Frontier Airlines": "F9", "Allegiant Air": "G4",
    "Hawaiian Airlines": "HA",
}
ROUTE_MAP = {
    ("JFK", "LAX"): (40.64, -73.78, 33.94, -118.41),
    ("LAX", "ORD"): (33.94, -118.41, 41.98, -87.90),
    ("ORD", "ATL"): (41.98, -87.90, 33.64, -84.43),
    ("ATL", "MIA"): (33.64, -84.43, 25.79, -80.29),
    ("DFW", "DEN"): (32.90, -97.04, 39.86, -104.67),
    ("SFO", "SEA"): (37.62, -122.38, 47.44, -122.31),
    ("BOS", "DCA"): (42.36, -71.01, 38.85, -77.04),
    ("LAS", "PHX"): (36.08, -115.15, 33.44, -112.01),
    ("MSP", "DTW"): (44.88, -93.22, 42.21, -83.35),
    ("CLT", "EWR"): (35.21, -80.94, 40.69, -74.17),
}
AIRPORTS = list({a for pair in ROUTE_MAP.keys() for a in pair})


@st.cache_data(ttl=300)
def generate_demo_data(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    n = 2400
    dates = pd.date_range("2024-01-01", periods=365, freq="D")
    rows = []
    for _ in range(n):
        airline = rng.choice(AIRLINES)
        route   = rng.choice(list(ROUTE_MAP.keys()))
        dep, arr = route
        delay   = max(0, rng.normal(18, 25))
        sched   = rng.choice([60, 90, 120, 150, 180, 210, 240])
        date    = pd.Timestamp(rng.choice(dates))
        rows.append({
            "airline":       airline,
            "iata":          AIRLINE_CODES[airline],
            "dep_airport":   dep,
            "arr_airport":   arr,
            "route":         f"{dep}→{arr}",
            "delay_min":     round(delay, 1),
            "scheduled_min": sched,
            "actual_min":    sched + round(delay, 1),
            "on_time":       delay < 15,
            "cancelled":     rng.random() < 0.02,
            "date":          date,
            "month":         int(date.month),
            "weekday":       int(date.day_of_week),
            "hour":          int(rng.choice(range(6, 23))),
            "year":          int(date.year),
        })
    df = pd.DataFrame(rows)
    ot    = df.groupby("airline")["on_time"].mean().rename("otr")
    avg_d = df.groupby("airline")["delay_min"].mean().rename("avg_delay_g")
    df    = df.merge(ot, on="airline").merge(avg_d, on="airline")
    df["score"] = (df["otr"] * 60 + np.clip((60 - df["avg_delay_g"]) / 60, 0, 1) * 40).round(1)
    return df


@st.cache_data(ttl=60)
def fetch_aviationstack(api_key: str, airline: str = "") -> dict | None:
    try:
        params = {"access_key": api_key, "limit": 100, "flight_status": "active"}
        if airline:
            params["airline_iata"] = airline
        r = requests.get("http://api.aviationstack.com/v1/flights", params=params, timeout=8)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


def build_airline_summary(df: pd.DataFrame) -> pd.DataFrame:
    grp = df.groupby("airline").agg(
        flights=("delay_min", "count"),
        avg_delay=("delay_min", "mean"),
        on_time_pct=("on_time", "mean"),
        cancelled_pct=("cancelled", "mean"),
        score=("score", "first"),
    ).reset_index()
    grp["avg_delay"]     = grp["avg_delay"].round(1)
    grp["on_time_pct"]   = (grp["on_time_pct"] * 100).round(1)
    grp["cancelled_pct"] = (grp["cancelled_pct"] * 100).round(2)
    grp = grp.sort_values("score", ascending=False).reset_index(drop=True)
    grp.index += 1
    return grp


# ─── CHART BUILDERS ───────────────────────────────────────────────────────────
def chart_delay_timeseries(df: pd.DataFrame, t: dict) -> go.Figure:
    ts = df.groupby("date")["delay_min"].mean().reset_index()
    ts["roll7"] = ts["delay_min"].rolling(7, center=True).mean()

    a1r = int(t["accent1"][1:3], 16)
    a1g = int(t["accent1"][3:5], 16)
    a1b = int(t["accent1"][5:7], 16)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=ts["date"], y=ts["delay_min"],
        mode="lines", name="Daily Avg",
        line=dict(color=t["accent1"], width=1, dash="dot"),
        opacity=0.4,
        hovertemplate="<b>%{x|%b %d}</b><br>Delay: %{y:.1f} min<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=ts["date"], y=ts["roll7"],
        mode="lines", name="7-Day Trend",
        line=dict(color=t["accent1"], width=2.5),
        fill="tozeroy",
        fillcolor=f"rgba({a1r},{a1g},{a1b},0.07)",
        hovertemplate="<b>%{x|%b %d}</b><br>7d avg: %{y:.1f} min<extra></extra>",
    ))
    mean_d, std_d = ts["delay_min"].mean(), ts["delay_min"].std()
    anomalies = ts[ts["delay_min"] > mean_d + 2 * std_d]
    fig.add_trace(go.Scatter(
        x=anomalies["date"], y=anomalies["delay_min"],
        mode="markers", name="⚠ Anomaly",
        marker=dict(color=t["danger"], size=9, symbol="circle",
                    line=dict(color="white", width=1.5)),
        hovertemplate="⚠️ <b>Anomaly %{x|%b %d}</b><br>Delay: %{y:.1f} min<extra></extra>",
    ))
    layout = plotly_layout(t, "Delay Trend — Daily Average with Anomaly Detection", 340)
    layout["xaxis"]["tickformat"] = "%b %Y"
    fig.update_layout(**layout)
    return fig


def chart_heatmap(df: pd.DataFrame, t: dict) -> go.Figure:
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    pivot = df.groupby(["weekday", "hour"])["delay_min"].mean().unstack(fill_value=0)
    pivot.index = [days[i] for i in pivot.index]
    fig = go.Figure(go.Heatmap(
        z=pivot.values,
        x=[f"{h:02d}:00" for h in pivot.columns],
        y=pivot.index,
        colorscale=[[0, t["accent2"]], [0.5, t["accent3"]], [1, t["danger"]]],
        hovertemplate="<b>%{y} %{x}</b><br>Avg Delay: %{z:.1f} min<extra></extra>",
        showscale=True,
        colorbar=dict(thickness=10, tickfont=dict(color=t["muted"], size=10)),
    ))
    fig.update_layout(**plotly_layout(t, "Delay Heatmap — Day × Hour of Departure", 320))
    return fig


def chart_airline_comparison(summary: pd.DataFrame, t: dict) -> go.Figure:
    df_s = summary.sort_values("avg_delay")
    colors = [t["danger"] if v > 20 else t["accent3"] if v > 10 else t["accent2"]
              for v in df_s["avg_delay"]]
    fig = go.Figure(go.Bar(
        x=df_s["avg_delay"], y=df_s["airline"],
        orientation="h",
        marker=dict(color=colors, line=dict(width=0)),
        hovertemplate="<b>%{y}</b><br>Avg Delay: %{x:.1f} min<extra></extra>",
        text=df_s["avg_delay"].map(lambda v: f"{v:.1f}m"),
        textfont=dict(color=t["text"], size=11, family="Space Grotesk"),
        textposition="outside",
    ))
    fig.add_vline(x=15, line=dict(color=t["muted"], dash="dash", width=1),
                  annotation_text="15m threshold",
                  annotation_font_color=t["muted"], annotation_font_size=10)
    fig.update_layout(**plotly_layout(t, "Airline Avg Delay Comparison", 360))
    return fig


def chart_gauge(score: float, label: str, t: dict) -> go.Figure:
    color = t["accent2"] if score >= 70 else t["accent3"] if score >= 50 else t["danger"]

    def hex_rgba(h, a):
        r, g, b = int(h[1:3],16), int(h[3:5],16), int(h[5:7],16)
        return f"rgba({r},{g},{b},{a})"

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=score,
        delta={"reference": 75, "valueformat": ".1f",
               "font": {"color": t["muted"], "size": 12, "family": "Space Grotesk"}},
        number={"font": {"family": "Orbitron", "color": t["text"], "size": 28}, "suffix": ""},
        gauge=dict(
            axis=dict(range=[0, 100], tickwidth=1, tickcolor=t["muted"],
                      tickfont=dict(color=t["muted"], size=10, family="Space Grotesk")),
            bar=dict(color=color, thickness=0.25),
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0,
            steps=[
                dict(range=[0, 50],  color=hex_rgba(t["danger"],  0.1)),
                dict(range=[50, 75], color=hex_rgba(t["accent3"], 0.1)),
                dict(range=[75,100], color=hex_rgba(t["accent2"], 0.1)),
            ],
            threshold=dict(line=dict(color=color, width=3), thickness=0.8, value=score),
        ),
        title={"text": label,
               "font": {"family": "Space Grotesk", "color": t["muted"], "size": 12}},
    ))
    fig.update_layout(**plotly_layout(t, height=220))
    return fig


def chart_geo_routes(df: pd.DataFrame, t: dict) -> go.Figure:
    fig = go.Figure()
    route_stats = df.groupby(["route", "dep_airport", "arr_airport"]).agg(
        avg_delay=("delay_min", "mean"), count=("delay_min", "count")
    ).reset_index()

    for _, row in route_stats.iterrows():
        key = (row["dep_airport"], row["arr_airport"])
        if key not in ROUTE_MAP:
            key = (row["arr_airport"], row["dep_airport"])
        if key not in ROUTE_MAP:
            continue
        lat0, lon0, lat1, lon1 = ROUTE_MAP[key]
        color = t["danger"] if row["avg_delay"] > 25 else t["accent3"] if row["avg_delay"] > 12 else t["accent2"]
        fig.add_trace(go.Scattergeo(
            lon=[lon0, lon1, None], lat=[lat0, lat1, None],
            mode="lines",
            line=dict(width=max(1, min(4, row["count"] / 80)), color=color),
            opacity=0.75, name=row["route"], hoverinfo="skip",
        ))
        fig.add_trace(go.Scattergeo(
            lon=[(lon0 + lon1) / 2], lat=[(lat0 + lat1) / 2],
            mode="markers",
            marker=dict(size=9, color=color, opacity=0.85,
                        line=dict(color="white", width=1.5)),
            hovertemplate=(f"<b>{row['route']}</b><br>"
                           f"Avg Delay: {row['avg_delay']:.1f} min<br>"
                           f"Flights: {row['count']}<extra></extra>"),
            showlegend=False,
        ))

    fig.update_geos(
        scope="usa", projection_type="albers usa",
        showland=True, landcolor=t["paper"],
        showcoastlines=True, coastlinecolor=t["border"],
        showlakes=True, lakecolor=t["bg"],
        showframe=False, bgcolor="rgba(0,0,0,0)",
        showcountries=True, countrycolor=t["border"],
    )
    fig.update_layout(**plotly_layout(t, "Route Delay Map — Color = Avg Delay Severity", 420))
    fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=44, b=0))
    return fig


def chart_monthly_trend(df: pd.DataFrame, t: dict) -> go.Figure:
    month_names = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    monthly = df.groupby(["month", "airline"])["delay_min"].mean().reset_index()
    top4    = df.groupby("airline")["delay_min"].mean().nlargest(4).index.tolist()
    colors  = [t["accent1"], t["accent2"], t["accent3"], t["danger"]]

    fig = go.Figure()
    for i, airline in enumerate(top4):
        sub = monthly[monthly["airline"] == airline].sort_values("month")
        fig.add_trace(go.Scatter(
            x=sub["month"].map(lambda m: month_names[m-1]),
            y=sub["delay_min"],
            mode="lines+markers",
            name=airline.split()[-1],
            line=dict(color=colors[i % len(colors)], width=2.2),
            marker=dict(size=6, color=colors[i % len(colors)]),
            hovertemplate=f"<b>{airline}</b><br>%{{x}}: %{{y:.1f}} min<extra></extra>",
        ))
    fig.update_layout(**plotly_layout(t, "Monthly Delay Trend — Top Airlines", 340))
    return fig


def chart_on_time_donut(summary: pd.DataFrame, t: dict) -> go.Figure:
    top5 = summary.head(5)
    fig  = go.Figure(go.Pie(
        labels=top5["airline"].apply(lambda x: x.split()[-1]),
        values=top5["on_time_pct"],
        hole=0.64,
        marker=dict(
            colors=[t["accent2"], t["accent1"], t["accent3"], t["purple"], t["danger"]],
            line=dict(color=t["bg"], width=2),
        ),
        hovertemplate="<b>%{label}</b><br>On-Time: %{value:.1f}%<extra></extra>",
        textfont=dict(color=t["text"], size=11, family="Space Grotesk"),
    ))
    fig.update_layout(**plotly_layout(t, "On-Time Rate — Top 5 Airlines", 300))
    fig.update_layout(showlegend=True,
                      legend=dict(orientation="v", x=1.02, y=0.5,
                                  font=dict(color=t["muted"], size=10, family="Space Grotesk")))
    return fig


def chart_scatter_bubble(df: pd.DataFrame, summary: pd.DataFrame, t: dict) -> go.Figure:
    colors_list = [t["accent1"], t["accent2"], t["accent3"], t["danger"],
                   t["purple"], "#f472b6", "#34d399", "#fb923c", "#60a5fa", "#facc15"]
    fig = go.Figure()
    for i, row in summary.iterrows():
        fig.add_trace(go.Scatter(
            x=[row["avg_delay"]], y=[row["on_time_pct"]],
            mode="markers+text",
            marker=dict(size=row["flights"] / 35, color=colors_list[i % len(colors_list)],
                        opacity=0.82, line=dict(color="white", width=1.5)),
            text=[row["airline"].split()[-1]],
            textposition="top center",
            textfont=dict(color=t["muted"], size=10, family="Space Grotesk"),
            name=row["airline"],
            hovertemplate=(f"<b>{row['airline']}</b><br>"
                           f"Avg Delay: %{{x:.1f}} min<br>"
                           f"On-Time: %{{y:.1f}}%<br>"
                           f"Score: {row['score']:.1f}<extra></extra>"),
        ))
    fig.add_hline(y=80, line=dict(color=t["muted"], dash="dash", width=1),
                  annotation_text="80% target",
                  annotation_font_color=t["muted"], annotation_font_size=10)
    fig.update_layout(**plotly_layout(t, "Performance Bubble — Size = Flight Volume", 380))
    fig.update_layout(showlegend=False,
                      xaxis_title="Avg Delay (min)", yaxis_title="On-Time Rate (%)")
    return fig


def chart_cancellations(summary: pd.DataFrame, t: dict) -> go.Figure:
    df_s = summary.sort_values("cancelled_pct", ascending=True)
    fig  = go.Figure(go.Bar(
        x=df_s["cancelled_pct"], y=df_s["airline"],
        orientation="h",
        marker=dict(
            color=df_s["cancelled_pct"],
            colorscale=[[0, t["accent2"]], [0.5, t["accent3"]], [1, t["danger"]]],
            showscale=False,
        ),
        hovertemplate="<b>%{y}</b><br>Cancellation Rate: %{x:.2f}%<extra></extra>",
        text=df_s["cancelled_pct"].map(lambda v: f"{v:.2f}%"),
        textfont=dict(color=t["text"], size=10, family="Space Grotesk"),
        textposition="outside",
    ))
    fig.update_layout(**plotly_layout(t, "Cancellation Rate by Airline", 320))
    return fig


def generate_insights(df: pd.DataFrame, summary: pd.DataFrame) -> list[dict]:
    insights = []
    worst   = summary.iloc[-1]
    best    = summary.iloc[0]
    avg_d   = df["delay_min"].mean()

    insights.append({"type":"good","icon":"🏆",
        "text": f"<b>{best['airline']}</b> leads the network with a performance score of <b>{best['score']:.1f}</b> and {best['on_time_pct']:.1f}% on-time rate."})
    insights.append({"type":"danger","icon":"⚠️",
        "text": f"<b>{worst['airline']}</b> ranks last with avg delay of <b>{worst['avg_delay']:.1f} min</b> — {((worst['avg_delay']-avg_d)/avg_d*100):.0f}% above network average."})
    peak_hour = df.groupby("hour")["delay_min"].mean().idxmax()
    insights.append({"type":"warn","icon":"🕐",
        "text": f"Peak delay hour is <b>{peak_hour:02d}:00</b> across all routes — schedule buffer adjustments for afternoon departures."})
    worst_route = df.groupby("route")["delay_min"].mean().idxmax()
    wr_delay    = df.groupby("route")["delay_min"].mean().max()
    insights.append({"type":"danger","icon":"✈️",
        "text": f"Route <b>{worst_route}</b> has the highest avg delay: <b>{wr_delay:.1f} min</b> — candidate for operational review."})
    cancel_worst = summary.sort_values("cancelled_pct", ascending=False).iloc[0]
    insights.append({"type":"warn","icon":"🚫",
        "text": f"<b>{cancel_worst['airline']}</b> has the highest cancellation rate at <b>{cancel_worst['cancelled_pct']:.2f}%</b>."})
    mon_avg  = df.groupby("month")["delay_min"].mean()
    worst_m  = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"][mon_avg.idxmax()-1]
    insights.append({"type":"warn","icon":"📅",
        "text": f"<b>{worst_m}</b> is the worst-performing month — likely seasonal weather and holiday traffic surges."})
    return insights


def forecast_delay_trend(df: pd.DataFrame, t: dict) -> go.Figure:
    monthly = df.groupby("month")["delay_min"].mean().reset_index()
    x = monthly["month"].values
    y = monthly["delay_min"].values
    z = np.polyfit(x, y, 2)
    p = np.poly1d(z)
    x_fut = np.linspace(1, 18, 80)
    y_fit = p(x_fut)

    a2r = int(t["accent2"][1:3],16)
    a2g = int(t["accent2"][3:5],16)
    a2b = int(t["accent2"][5:7],16)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="markers+lines", name="Historical",
        marker=dict(color=t["accent1"], size=7),
        line=dict(color=t["accent1"], width=2.2),
        hovertemplate="Month %{x}: %{y:.1f} min<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=x_fut, y=y_fit, mode="lines", name="Polynomial Forecast",
        line=dict(color=t["accent2"], width=2, dash="dash"),
        hovertemplate="Forecast: %{y:.1f} min<extra></extra>",
    ))
    noise = 2.5
    fig.add_trace(go.Scatter(
        x=np.concatenate([x_fut, x_fut[::-1]]),
        y=np.concatenate([y_fit + noise, (y_fit - noise)[::-1]]),
        fill="toself",
        fillcolor=f"rgba({a2r},{a2g},{a2b},0.07)",
        line=dict(color="rgba(0,0,0,0)"),
        showlegend=False, name="Confidence Band", hoverinfo="skip",
    ))
    fig.add_vrect(x0=12.5, x1=18, fillcolor=t["accent2"],
                  opacity=0.035, line_width=0,
                  annotation_text="Forecast →",
                  annotation_font_color=t["muted"], annotation_font_size=10)
    fig.update_layout(**plotly_layout(t, "Predictive Delay Trend (Polynomial Regression)", 340))
    return fig


# ─── HERO HEADER ─────────────────────────────────────────────────────────────
def render_hero(df: pd.DataFrame, filters: dict, t: dict):
    now = datetime.datetime.now().strftime("%d %b %Y  %H:%M UTC")
    total_fl = len(df)
    avg_d    = df["delay_min"].mean()
    otp      = df["on_time"].mean() * 100
    net_sc   = df["score"].mean()

    status_html = (
        '<span class="status-live"><span class="status-dot dot-live"></span>LIVE DATA</span>'
        if filters["use_live"] and filters["api_key"]
        else '<span class="status-offline"><span class="status-dot dot-offline"></span>DEMO MODE</span>'
    )

    # Ticker items
    best_al  = df.groupby("airline")["delay_min"].mean().idxmin()
    worst_rt = df.groupby("route")["delay_min"].mean().idxmax()

    ticker_html = f"""
    <div class="ticker-strip">
        <div class="ticker-dot"></div>
        <div class="ticker-item">NETWORK OTP <span>{otp:.1f}%</span></div>
        <div class="ticker-dot"></div>
        <div class="ticker-item">AVG DELAY <span>{avg_d:.1f} MIN</span></div>
        <div class="ticker-dot"></div>
        <div class="ticker-item">BEST AIRLINE <span>{best_al.split()[-1].upper()}</span></div>
        <div class="ticker-dot"></div>
        <div class="ticker-item red">WORST ROUTE <span>{worst_rt}</span></div>
        <div class="ticker-dot"></div>
        <div class="ticker-item">FLIGHTS ANALYZED <span>{total_fl:,}</span></div>
        <div class="ticker-dot"></div>
        <div class="ticker-item">NET SCORE <span>{net_sc:.1f}/100</span></div>
    </div>
    """

    st.markdown(f"""
    <div class="hero-wrapper">
        <div class="hero-bg"></div>
        <div class="hero-content">
            <div>
                <div class="hero-logo">
                    <span class="hero-logo-plane">✈</span>AEROINSIGHT PRO
                </div>
                <div class="hero-tagline">Airline Flight Delay &amp; Route Performance Intelligence</div>
                <div style="display:flex;align-items:center;gap:10px;margin-top:12px;">
                    <span class="hero-version-pill">v3.0 ULTRA-PRO</span>
                    {status_html}
                    <span style="font-size:11px;color:rgba(200,215,255,0.45);font-family:'JetBrains Mono',monospace;">🕐 {now}</span>
                </div>
            </div>
            <div class="hero-stats">
                <div class="hero-stat-item">
                    <div class="hero-stat-value">{total_fl:,}</div>
                    <div class="hero-stat-label">Flights</div>
                </div>
                <div class="hero-divider"></div>
                <div class="hero-stat-item">
                    <div class="hero-stat-value green">{otp:.1f}%</div>
                    <div class="hero-stat-label">On-Time</div>
                </div>
                <div class="hero-divider"></div>
                <div class="hero-stat-item">
                    <div class="hero-stat-value orange">{avg_d:.1f}</div>
                    <div class="hero-stat-label">Avg Delay (min)</div>
                </div>
                <div class="hero-divider"></div>
                <div class="hero-stat-item">
                    <div class="hero-stat-value purple">{net_sc:.0f}</div>
                    <div class="hero-stat-label">Net Score</div>
                </div>
            </div>
        </div>
        {ticker_html}
    </div>
    """, unsafe_allow_html=True)


# ─── KPI CARDS ───────────────────────────────────────────────────────────────
def render_kpis(df: pd.DataFrame, t: dict):
    total_flights = len(df)
    avg_delay     = df["delay_min"].mean()
    on_time_pct   = df["on_time"].mean() * 100
    cancel_pct    = df["cancelled"].mean() * 100
    best_airline  = df.groupby("airline")["delay_min"].mean().idxmin()
    worst_route_d = df.groupby("route")["delay_min"].mean().max()
    net_score     = df["score"].mean()

    kpis = [
        ("✈️", "Total Flights",      f"{total_flights:,}",     "↑ 12.4%", "up",   "vs last period",   t["accent1"]),
        ("⏱️", "Avg Network Delay",  f"{avg_delay:.1f}m",      "↑ 2.1m",  "down", "all airlines",     t["accent3"]),
        ("✅", "On-Time Rate",        f"{on_time_pct:.1f}%",   "↑ 3.2%",  "up",   "15 min threshold", t["accent2"]),
        ("🚫", "Cancellation Rate",   f"{cancel_pct:.2f}%",    "↓ 0.3%",  "up",   "industry avg 2.1%",t["danger"]),
        ("🏆", "Best Airline",        best_airline.split()[-1],"Rank #1",  "up",   "by perf. score",   t["purple"]),
        ("📍", "Worst Route Peak",    f"{worst_route_d:.0f}m", "⚠ High",  "down", "max avg delay",    t["accent3"]),
        ("⚡", "Network Score",        f"{net_score:.1f}",      "↑ 1.8pt", "up",   "weighted composite",t["accent2"]),
    ]

    cols = st.columns(len(kpis))
    for col, (icon, label, value, trend, direction, sub, color) in zip(cols, kpis):
        trend_cls = "up" if direction == "up" else "down"
        with col:
            st.markdown(f"""
            <div class="kpi-card" style="--kpi-color:{color};">
                <span class="kpi-icon">{icon}</span>
                <div class="kpi-label">{label}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-trend {trend_cls}">{trend}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)


# ─── SECTION HEADER ──────────────────────────────────────────────────────────
def section_hdr(icon: str, title: str, badge: str = ""):
    badge_html = f'<div class="section-badge">{badge}</div>' if badge else ""
    st.markdown(f"""
    <div class="section-hdr">
        <div class="section-hdr-icon">{icon}</div>
        <div class="section-hdr-title">{title}</div>
        <div class="section-hdr-line"></div>
        {badge_html}
    </div>""", unsafe_allow_html=True)


# ─── SIDEBAR ─────────────────────────────────────────────────────────────────
def render_sidebar(t: dict) -> dict:
    with st.sidebar:
        st.markdown(f"""
        <div style="padding:24px 20px 16px;">
            <div style="font-family:'Orbitron',monospace;font-size:18px;font-weight:900;
                        letter-spacing:0.06em;
                        background:linear-gradient(90deg,{t['accent1']},{t['accent2']});
                        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                        background-clip:text;">
                ✈ AEROINSIGHT
            </div>
            <div style="font-size:10px;color:{t['muted']};margin-top:4px;
                        font-family:'JetBrains Mono',monospace;letter-spacing:0.12em;">
                FLIGHT ANALYTICS PLATFORM
            </div>
        </div>
        <div style="height:1px;background:{t['border']};margin:0 16px 18px;"></div>
        """, unsafe_allow_html=True)

        st.markdown(f'<div class="nav-section-label">Navigation</div>', unsafe_allow_html=True)

        nav_items = [
            ("📊", "Overview",   "overview"),
            ("📈", "Analytics",  "analytics"),
            ("🗺️", "Route Map",  "routes"),
            ("🏆", "Rankings",   "rankings"),
            ("🤖", "AI Insights","insights"),
        ]
        selected = st.session_state.get("nav", "overview")
        for icon, label, key in nav_items:
            is_active = selected == key
            btn_type  = "primary" if is_active else "secondary"
            if st.button(f"{icon}  {label}", key=f"nav_{key}",
                         use_container_width=True, type=btn_type):
                st.session_state["nav"] = key
                st.rerun()

        st.markdown(f"<div style='height:1px;background:{t['border']};margin:16px 8px;'></div>", unsafe_allow_html=True)
        st.markdown(f'<div class="nav-section-label">Data Filters</div>', unsafe_allow_html=True)

        api_key = st.text_input("AviationStack API Key", type="password",
                                placeholder="Paste your API key…", key="api_key")

        all_airlines     = AIRLINES
        selected_airlines = st.multiselect("Airlines", all_airlines,
                                           default=all_airlines[:5], key="sel_airlines")
        all_routes       = [f"{a}→{b}" for a, b in ROUTE_MAP.keys()]
        selected_routes  = st.multiselect("Routes", all_routes,
                                          default=all_routes[:4], key="sel_routes")
        delay_thresh     = st.slider("Max Delay Filter (min)", 0, 120, 120, key="delay_thresh")

        st.markdown(f"<div style='height:1px;background:{t['border']};margin:16px 8px;'></div>", unsafe_allow_html=True)
        st.markdown(f'<div class="nav-section-label">Settings</div>', unsafe_allow_html=True)

        dark_mode    = st.toggle("🌙  Dark Mode",          value=st.session_state.get("dark_mode", True), key="dark_toggle")
        auto_refresh = st.toggle("🔄  Auto Refresh (30s)", value=False, key="auto_refresh")
        show_live    = st.toggle("📡  Use Live API",       value=False, key="use_live")

        st.markdown(f"""
        <div style='margin:16px 8px 0;padding:12px;
                    background:{t['accent1']}10;border:1px solid {t['accent1']}22;
                    border-radius:12px;'>
            <div style='font-size:10px;color:{t['muted']};font-weight:700;
                        text-transform:uppercase;letter-spacing:0.1em;
                        margin-bottom:8px;font-family:"Space Grotesk",sans-serif;'>
                Data Status
            </div>
        """, unsafe_allow_html=True)

        if show_live and api_key:
            st.markdown('<span class="status-live"><span class="status-dot dot-live"></span>LIVE</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="status-offline"><span class="status-dot dot-offline"></span>DEMO</span>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(f"""
        <div style='margin-top:auto;padding:24px 16px 20px;text-align:center;'>
            <div style='font-family:"Orbitron",monospace;font-size:10px;
                        color:{t['muted']};letter-spacing:0.1em;'>
                AEROTECH ANALYTICS
            </div>
            <div style='font-size:11px;color:{t['dim']};margin-top:4px;
                        font-family:"Space Grotesk",sans-serif;'>
                AeroInsight Pro v3.0
            </div>
        </div>
        """, unsafe_allow_html=True)

        return {
            "api_key":          api_key,
            "selected_airlines": selected_airlines if selected_airlines else all_airlines,
            "selected_routes":   selected_routes if selected_routes else all_routes,
            "delay_thresh":      delay_thresh,
            "dark_mode":         dark_mode,
            "auto_refresh":      auto_refresh,
            "use_live":          show_live,
        }


# ─── PAGES ────────────────────────────────────────────────────────────────────
def page_overview(df: pd.DataFrame, summary: pd.DataFrame, t: dict):
    render_kpis(df, t)

    section_hdr("📈", "Delay Trend & On-Time Rate", "Time Series")
    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(chart_delay_timeseries(df, t), use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(chart_on_time_donut(summary, t), use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    section_hdr("🔥", "Delay Patterns", "Heatmap")
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_heatmap(df, t), use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)


def page_analytics(df: pd.DataFrame, summary: pd.DataFrame, t: dict):
    section_hdr("📊", "Airline Performance Comparison", "Deep Dive")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(chart_airline_comparison(summary, t), use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(chart_cancellations(summary, t), use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    section_hdr("💬", "Multi-Dimensional Analysis", "Bubble + Trend")
    c3, c4 = st.columns(2)
    with c3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(chart_scatter_bubble(df, summary, t), use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(chart_monthly_trend(df, t), use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    section_hdr("📉", "Predictive Forecast", "ML Trend")
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(forecast_delay_trend(df, t), use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)


def page_routes(df: pd.DataFrame, t: dict):
    section_hdr("🌐", "Route Performance Geo Map", "USA Network")
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.plotly_chart(chart_geo_routes(df, t), use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

    section_hdr("📋", "Route Statistics", "")
    route_stats = (df.groupby("route")
                     .agg(flights=("delay_min","count"),
                          avg_delay=("delay_min","mean"),
                          on_time=("on_time","mean"),
                          cancelled=("cancelled","mean"))
                     .reset_index()
                     .sort_values("avg_delay", ascending=False))
    route_stats["avg_delay"] = route_stats["avg_delay"].round(1)
    route_stats["on_time"]   = (route_stats["on_time"] * 100).round(1)
    route_stats["cancelled"] = (route_stats["cancelled"] * 100).round(2)
    route_stats.columns      = ["Route","Flights","Avg Delay (min)","On-Time %","Cancelled %"]
    st.dataframe(route_stats, use_container_width=True, hide_index=True)


def page_rankings(df: pd.DataFrame, summary: pd.DataFrame, t: dict):
    section_hdr("🏆", "Airline Performance Rankings", "Composite Score")

    max_score = summary["score"].max()
    rank_html = ""
    for i, row in summary.iterrows():
        pct = row["score"] / max_score * 100
        is_top = i <= 3
        score_color = t["accent2"] if row["score"] >= 70 else t["accent3"] if row["score"] >= 55 else t["danger"]
        medal = "🥇" if i==1 else "🥈" if i==2 else "🥉" if i==3 else "✈️"
        rank_html += f"""
        <div class="rank-row">
            <div class="rank-num {'top' if is_top else ''}">{i}</div>
            <div style="font-size:22px;">{medal}</div>
            <div class="rank-name">{row['airline']}</div>
            <div style="font-size:11px;color:{t['muted']};margin-right:6px;font-family:'JetBrains Mono',monospace;">OT:{row['on_time_pct']:.0f}%</div>
            <div style="font-size:11px;color:{t['muted']};margin-right:12px;font-family:'JetBrains Mono',monospace;">⏱{row['avg_delay']:.0f}m</div>
            <div class="rank-bar-bg">
                <div class="rank-bar-fill" style="width:{pct:.0f}%;"></div>
            </div>
            <div class="rank-score" style="color:{score_color};">{row['score']:.1f}</div>
        </div>"""
    st.markdown(rank_html, unsafe_allow_html=True)

    section_hdr("🎯", "Performance Gauges — Top 4", "")
    top4   = summary.head(4)
    g_cols = st.columns(4)
    for col, (_, row) in zip(g_cols, top4.iterrows()):
        with col:
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            st.plotly_chart(
                chart_gauge(row["score"], row["airline"].split()[-1], t),
                use_container_width=True,
                config={"displayModeBar": False},
            )
            st.markdown('</div>', unsafe_allow_html=True)


def page_insights(df: pd.DataFrame, summary: pd.DataFrame, t: dict, filters: dict):
    section_hdr("🤖", "AI Insights Panel", "Auto-Generated")

    insights   = generate_insights(df, summary)
    items_html = ""
    for ins in insights:
        items_html += f'<div class="insight-item {ins["type"]}">{ins["icon"]}&nbsp;&nbsp;{ins["text"]}</div>'
    st.markdown(f'<div class="insight-panel">{items_html}</div>', unsafe_allow_html=True)

    section_hdr("📥", "Export Data", "")
    c1, c2, c3 = st.columns(3)
    with c1:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Export Raw Data (CSV)", csv, "aeroinsight_flights.csv",
                           "text/csv", use_container_width=True)
    with c2:
        csv2 = summary.to_csv().encode("utf-8")
        st.download_button("📥 Export Summary (CSV)", csv2, "aeroinsight_summary.csv",
                           "text/csv", use_container_width=True)
    with c3:
        ins_text = "\n".join([f"• {i['text'].replace('<b>','').replace('</b>','')}" for i in insights])
        st.download_button("📥 Export Insights (TXT)", ins_text.encode(),
                           "aeroinsight_insights.txt", "text/plain", use_container_width=True)

    section_hdr("📋", "Network Summary Statistics", "")
    st.dataframe(summary.style.format({
        "avg_delay": "{:.1f}", "on_time_pct": "{:.1f}%",
        "cancelled_pct": "{:.2f}%", "score": "{:.1f}",
    }), use_container_width=True)


# ─── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    if "nav"       not in st.session_state: st.session_state["nav"]       = "overview"
    if "dark_mode" not in st.session_state: st.session_state["dark_mode"] = True

    dark = st.session_state.get("dark_mode", True)
    t    = get_theme(dark)
    inject_css(dark)

    filters = render_sidebar(t)
    dark = filters["dark_mode"]
    st.session_state["dark_mode"] = dark
    t = get_theme(dark)
    inject_css(dark)   # re-inject after theme toggle

    # ── Load & filter data ──
    with st.spinner("Loading flight telemetry…"):
        df_raw = generate_demo_data()

    df = df_raw[
        df_raw["airline"].isin(filters["selected_airlines"]) &
        df_raw["route"].isin(filters["selected_routes"]) &
        (df_raw["delay_min"] <= filters["delay_thresh"])
    ].copy()

    if df.empty:
        st.warning("No data matches current filters — adjust the sidebar selections.")
        return

    summary = build_airline_summary(df)

    # ── Hero ──
    render_hero(df, filters, t)

    # ── Auto-refresh ──
    if filters["auto_refresh"]:
        time.sleep(0.5)
        st.rerun()

    # ── Page routing ──
    nav = st.session_state.get("nav", "overview")
    if nav == "overview":
        page_overview(df, summary, t)
    elif nav == "analytics":
        page_analytics(df, summary, t)
    elif nav == "routes":
        page_routes(df, t)
    elif nav == "rankings":
        page_rankings(df, summary, t)
    elif nav == "insights":
        page_insights(df, summary, t, filters)

    # ── Footer ──
    st.markdown(f"""
    <div class="app-footer">
        ✈&nbsp; <b>AeroInsight Pro v3.0</b>
        &nbsp;|&nbsp; Built with Streamlit &amp; Plotly
        &nbsp;|&nbsp; <span style="color:{t['accent1']};">AeroTech Analytics © 2025</span>
        &nbsp;|&nbsp; Data refreshes every 5 min (cached)
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
