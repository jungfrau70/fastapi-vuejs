# from sched.config import common as _cfg
import os
import configparser
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Specify the path to the INI file containing user sections
ini_file_path = 'env/.env'

# Read the INI file
config = configparser.ConfigParser()
config.read(ini_file_path)

# Schedule the task for each specified section to run every minute
section_name = 'common'
section = config[section_name]

COUNTRY = section.get('COUNTRY')
DATABASE_URL = section.get('DATABASE_URL')

DATABASE_HOST = section.get('DATABASE_HOST')
DATABASE_NAME = section.get('DATABASE_NAME')
DATABASE_USER = section.get('DATABASE_USER')
DATABASE_PASSWORD = section.get('DATABASE_PASSWORD')
DATABASE_PORT = section.get('DATABASE_PORT')

DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
# SSQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

# Create an SQLite database engine and session
engine = create_engine(DATABASE_URL, pool_size=100, max_overflow=200)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Signals(Base):
    __tablename__ = 'signals'
    id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String)
    sym = Column(String)
    datetime = Column(DateTime)
    buy_position = Column(String)


class BackTest(Base):
    __tablename__ = 'backtest'
    id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String)
    sym = Column(String)
    pur_p = Column(Float)
    sl_p = Column(Float)
    tp_p = Column(Float)
    total_return = Column(Float)
    benchmark_return = Column(Float)
    win_rate = Column(Float)
    sharpe_ratio = Column(Float)
    sortino_ratio = Column(Float)
    sl = Column(Float)
    tp = Column(Float)
    position = Column(String)
    position_time = Column(DateTime)
    owner = Column(String)


class BalanceSheet(Base):
    __tablename__ = 'balance_sheet'
    id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String)
    sym = Column(String)
    pur_p = Column(Float)
    sl_p = Column(Float)
    tp_p = Column(Float)
    # total_return = Column(Float)
    # benchmark_return = Column(Float)
    # win_rate = Column(Float)
    # sharpe_ratio = Column(Float)
    # sortino_ratio = Column(Float)
    # sl = Column(Float)
    # tp = Column(Float)
    position = Column(String)
    position_time = Column(DateTime)
    owner = Column(String)

# Define the TradeHistory table


class Trading(Base):
    __tablename__ = 'trading'
    id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String)
    sym = Column(String)
    signal = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    status = Column(Boolean)
    buy_fee = Column(Float)
    sell_fee = Column(Float)
    accumulated_profit_loss = Column(Float)
    completed = Column(Boolean, default=False)
    timestamp = Column(DateTime)
    owner = Column(String)
    comment = Column(String)


# Create the table in the database
Base.metadata.create_all(engine)
