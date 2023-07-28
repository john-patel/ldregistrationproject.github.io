# build_files.sh
pip install Django
pip install psycopg2-binary
python3.9 manage.py collectstatic
