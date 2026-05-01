# configs/config.py

import os

class DatabaseConfig:
    """
    SQL Server 2016 Configuration using SQLAlchemy
    数据库配置 (Database Configuration, DB Config)
    """
    DRIVER = "ODBC Driver 17 for SQL Server"
    SERVER = os.environ.get("DB_SERVER", "localhost")
    DATABASE = os.environ.get("DB_NAME", "GeoStatsDB")
    USER = os.environ.get("DB_USER", "admin")
    PASSWORD = os.environ.get("DB_PASSWORD", "password")

    @classmethod
    def get_connection_string(cls):
        """Returns the SQLAlchemy connection string"""
        return f"mssql+pyodbc://{cls.USER}:{cls.PASSWORD}@{cls.SERVER}/{cls.DATABASE}?driver={cls.DRIVER.replace(' ', '+')}"

class UIConfig:
    """
    UI/UX Configuration focusing on Morandi aesthetic
    用户界面配置 (User Interface Configuration, UI Config)
    """
    # Morandi Color Palette
    MORANDI_TEAL = "#7B8B88"
    MORANDI_DUSTY_ROSE = "#B89B9B"
    MORANDI_GREY = "#9C9E9D"
    MORANDI_LIGHT_GREY = "#E0E0E0"
    MORANDI_CREAM = "#F2EFEB"
    MORANDI_DARK = "#000000"

    # Font Settings
    FONT_FAMILY = "Yuyuan, sans-serif"
    
    # CSS for Streamlit global aesthetics (Rounded Rectangles & Fonts)
    STREAMLIT_CUSTOM_CSS = f"""
    <style>
        html, body, [class*="css"], p, span, h1, h2, h3, h4, h5, h6, label, div {{
            font-family: {FONT_FAMILY};
            color: #000000 !important;
        }}
        
        body {{
            background-color: {MORANDI_CREAM};
        }}
        
        .stApp {{
            background-color: {MORANDI_CREAM};
        }}
        
        /* Rounded rectangles for all layout containers */
        div[data-testid="stMetric"], div.stCard, div.element-container > div {{
            border-radius: 12px;
            background-color: white;
            padding: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }}
        
        /* Sidebar styling */
        section[data-testid="stSidebar"] {{
            background-color: {MORANDI_LIGHT_GREY};
        }}
        
        /* Button styling */
        button[kind="primary"] {{
            background-color: {MORANDI_TEAL} !important;
            border-color: {MORANDI_TEAL} !important;
            border-radius: 8px !important;
            color: white !important;
        }}
    </style>
    """
