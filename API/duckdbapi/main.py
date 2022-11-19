from fastapi import FastAPI
import duckdb

def duckdb_connect():
    return duckdb.connect(database=':memory:')

conn = duckdb_connect();
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/count")
def count():
    return  { "rows" : conn.execute("SELECT count(*) from read_parquet('/Users/manuelvargas/Documents/ITBA/data/VAST-Challenge-2022/Datasets/parquet/ParticipantStatusLogs*.parquet');").fetchone()[0] }



#    /Users/manuelvargas/Documents/ITBA/covid/Covid19Casos.csv
#    /Users/manuelvargas/Documents/ITBA/data/VAST-Challenge-2022/Datasets/parquet


@app.get("/al_cmode_count")
def count():
    return  { "rows" : conn.execute("SELECT currentMode, count(*) from read_parquet('/Users/manuelvargas/Documents/ITBA/data/VAST-Challenge-2022/Datasets/parquet/ParticipantStatusLogs*.parquet') group by 1;")
    .fetchone()[0]
    }


#
@app.get("/al_cmode_count-v2")
def al_cmode_count():
    query= """
          SELECT currentMode, count(*)
          from read_parquet('/Users/manuelvargas/Documents/ITBA/data/VAST-Challenge-2022/Datasets/parquet/ParticipantStatusLogs*.parquet')
          group by 1;
          """
    return conn.execute(query).fetchall()


#date_trunc('month', timestamp)
@app.get("/FinancialJournal_wage_by_month")
def inancialJournal_wage_by_month():
    query= """
        select    timestamp::timestamp   , sum(amount)
        from
        '/Users/manuelvargas/Documents/ITBA/data/VAST-Challenge-2022/Datasets/parquet/FinancialJournal.parquet'
        where category = 'Wage' group by 1 order by 1;
        """
    return conn.execute(query).fetchall()

# select timestamp::timestamp from '/Users/manuelvargas/Documents/ITBA/data/VAST-Challenge-2022/Datasets/parquet/FinancialJournal.parquet' limit 10;

@app.get("/FinancialJournal_test")
def inancialJournal_wage_test():
    query= """
        select timestamp::timestamp
        from
        '/Users/manuelvargas/Documents/ITBA/data/VAST-Challenge-2022/Datasets/parquet/FinancialJournal.parquet'
        limit 10;
        """
    return conn.execute(query).fetchall()

@app.get("/bla")
def bla():
    return {"otra": "data"}
