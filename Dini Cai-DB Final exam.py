{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: sqlalchemy in /Users/dylanbai/Library/Python/3.9/lib/python/site-packages (2.0.19)\n",
      "Requirement already satisfied: typing-extensions>=4.2.0 in /Users/dylanbai/Library/Python/3.9/lib/python/site-packages (from sqlalchemy) (4.5.0)\n",
      "\u001b[33mWARNING: You are using pip version 21.2.4; however, version 23.2.1 is available.\n",
      "You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.\u001b[0m\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install sqlalchemy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: psycopg2-binary in /Users/dylanbai/Library/Python/3.9/lib/python/site-packages (2.9.7)\n",
      "\u001b[33mWARNING: You are using pip version 21.2.4; however, version 23.2.1 is available.\n",
      "You should consider upgrading via the '/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip' command.\u001b[0m\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install psycopg2-binary"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import sqlalchemy as sa\n",
    "from sqlalchemy import create_engine\n",
    "from sqlalchemy import text\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "db_secret = {\n",
    "    'drivername': 'postgresql+psycopg2',\n",
    "    'host':'mmai5100postgres.canadacentral.cloudapp.azure.com',\n",
    "    'port':'5432',\n",
    "    'user':'cindycai',\n",
    "    'password':'2023!Schulich',\n",
    "    'database':'mban_db'\n",
    "    \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [],
   "source": [
    "db_connection_url = sa.engine.URL.create(\n",
    "    drivername= db_secret['drivername'],\n",
    "    username= db_secret['user'],\n",
    "    password= db_secret['password'],\n",
    "    host= db_secret['host'],\n",
    "    port= db_secret['port'],\n",
    "    database= db_secret['database']\n",
    "    \n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = sa.create_engine(db_connection_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "with engine.connect() as connection:\n",
    "    data=pd.read_sql(sql='SELECT * FROM dimensions.date_dimension;',con=connection)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "db_secret = {\n",
    "    'drivername': 'postgresql+psycopg2',\n",
    "    'host':'mmai5100postgres.canadacentral.cloudapp.azure.com',\n",
    "    'port':'5432',\n",
    "    'user':'cindycai',\n",
    "    'password':'2023!Schulich',\n",
    "    'database':'cindycai_db'\n",
    "    \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "db_connection_url = sa.engine.URL.create(\n",
    "    drivername= db_secret['drivername'],\n",
    "    username= db_secret['user'],\n",
    "    password= db_secret['password'],\n",
    "    host= db_secret['host'],\n",
    "    port= db_secret['port'],\n",
    "    database= db_secret['database'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = sa.create_engine(db_connection_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "create_table_query=sa.text('''\n",
    "CREATE TABLE IF NOT EXISTS final_exam.date_dimension(\n",
    "   sk_date INT,\n",
    "   date DATE,\n",
    "   day_name VARCHAR(25),\n",
    "   day_of_month INT,\n",
    "   day_of_year INT,\n",
    "   month INT,\n",
    "   month_name VARCHAR(25),\n",
    "   year INT,\n",
    "   year_week VARCHAR(25),\n",
    "   week VARCHAR(25),\n",
    "   running_week INT,\n",
    "   year_quarter VARCHAR(25),\n",
    "   quarter VARCHAR(25),\n",
    "   running_quarter INT\n",
    ");\n",
    "''')\n",
    "\n",
    "with engine.connect() as connection:\n",
    "    connection.execute (sa.text('CREATE SCHEMA IF NOT EXISTS final_exam'))\n",
    "    connection.execute(create_table_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1826"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.to_sql(\n",
    "   name='date_dimension',\n",
    "   schema='final_exam',\n",
    "   con=engine,\n",
    "   if_exists='replace',\n",
    "    index=False,\n",
    "    method='multi',\n",
    "    dtype={\n",
    "        'sk_date':sa.types.INTEGER,\n",
    "        'date':sa.types.DATE,\n",
    "        'day_name': sa.types.VARCHAR(25),\n",
    "        'day_of_month':sa.types.INTEGER,\n",
    "        'day_of_year':sa.types.INTEGER,\n",
    "        'month':sa.types.INTEGER,\n",
    "'month_name':sa.types.VARCHAR(25),\n",
    "'year': sa.types.INTEGER,\n",
    "'year_week':sa.types.VARCHAR(25),\n",
    "'week': sa.types.VARCHAR(25),\n",
    "'running_week':sa.types.INTEGER,\n",
    "'year_quarter': sa.types.VARCHAR(25),\n",
    "'quarter': sa.types.VARCHAR(25),\n",
    "'running_quarter': sa.types.INTEGER\n",
    "    }\n",
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
