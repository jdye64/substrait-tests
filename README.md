# substrait-tests

# Create a Conda environment to run all the test files
```conda env create -f ./conda/environment.yaml && conda activate substrait-tests```

## We install Dask-SQL from source to make sure we have the latest changes from both Dask-SQL and DataFusion

```
git clone https://github.com/dask-contrib/dask-sql.git
cd dask-sql
git fetch origin pull/1041/head:execute_substrait_plans
git checkout execute_substrait_plans
conda activate substrait-tests
pip install -e . && python ./setup.py install
cd ../
```

# Run Script

There will eventually be several tests for now its just some hacky scripts for testing functionality

```conda activate substrait-tests && python ./duckdb_substrait.py```
