## introduction
Meterspere is a popular test case management tool, while DataEase is the assorted tool to generate test report, 
but DataEase is based on Metersphare origin database table and hard to generate common used report. So dj_metersphere provide APIs to 
to generate test report including test case summary and test execution summary.

## setup dj_meterspere
clone code and run cmds `cd dj_meterspere && poetry install`

## run dj_meterspere
`python3 manage.py runserver 0.0.0.0:28000`

## API Docs
### redoc
http://0.0.0.0:28000/redoc/
### swagger
http://0.0.0.0:28000/swagger/