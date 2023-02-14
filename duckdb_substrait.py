import duckdb
from dask_sql import Context
import pandas as pd

con = duckdb.connect()
con.install_extension("substrait")
con.load_extension("substrait")

con.execute(query='CREATE TABLE crossfit (exercise text,dificulty_level int);')
con.execute(query="INSERT INTO crossfit VALUES ('Push Ups', 3), ('Pull Ups', 5) , (' Push Jerk', 7), ('Bar Muscle Up', 10);")
proto_bytes = con.get_substrait(query="select count(exercise) as exercise from crossfit where dificulty_level <=5").fetchone()[0]

with open("./substrait/crossfit/proto/crossfit.proto", "wb") as f:
    f.write(proto_bytes)

sub_json = con.get_substrait_json(query="select count(exercise) as exercise from crossfit where dificulty_level <=5").fetchone()[0]
with open("./substrait/crossfit/json/crossfit.json", "w") as f:
    f.write(sub_json)


# Now run the Substrait plan against Dask-SQL
c = Context()
crossfit_df = pd.DataFrame({"exercise": ['Push Ups', 'Pull Ups', 'Push Jerk', 'Bar Muscle Up'], "dificulty_level": [3, 5, 7, 10]})
c.create_table("crossfit", crossfit_df)

df = c.sql("./substrait/crossfit/proto//crossfit.proto", substrait=True)
